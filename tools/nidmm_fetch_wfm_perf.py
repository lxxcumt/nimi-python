# !python
import nidmm

import argparse
import logging
import pprint
import sys

from functools import wraps
import time

PROF_DATA = {}
sentinel = object()


def profile(fn):
    @wraps(fn)
    def with_profiling(*args, **kwargs):
        start_time = time.time()

        ret = fn(*args, **kwargs)

        elapsed_time = time.time() - start_time

        if fn.__name__ not in PROF_DATA:
            PROF_DATA[fn.__name__] = [0, []]
        PROF_DATA[fn.__name__][0] += 1
        PROF_DATA[fn.__name__][1].append(elapsed_time)

        return ret

    return with_profiling


def print_prof_data():
    header_fmt = '{:25}  {:5}  {:5}  {:5}  {:5}'
    row_fmt = '{:25}  {:5}  {:0.3f}  {:0.3f}  {:0.3f}'
    print('\n')
    print(header_fmt.format("Function", 'Count', 'Total', 'Max', 'Avg'))
    print(header_fmt.format('-' * 25, '-' * 5, '-' * 5, '-' * 5, '-' * 5))
    for fname, data in PROF_DATA.items():
        max_time = max(data[1])
        total_time = sum(data[1])
        avg_time = total_time / len(data[1])
        print(row_fmt.format(fname, data[0], total_time, max_time, avg_time))


pp = pprint.PrettyPrinter(indent=4, width=100)


@profile
def nidmm_init(args):
    return nidmm.Session('FakeDevice', False, True, 'Simulate=1, DriverSetup=Model:4071; BoardType:PXI')


@profile
def nidmm_configure(session, args):
    session.configure_waveform_acquisition(nidmm.Function.WAVEFORM_VOLTAGE, args.range, args.rate, args.acq_size)


@profile
def nidmm_initiate(session, args):
    session._initiate()


@profile
def nidmm_wait_for_ready(session, args):
    backlog, acq_status = session.read_status()
    while backlog < args.acq_size and acq_status == nidmm.AcquisitionStatus.RUNNING:
        backlog, acq_status = session.read_status()


@profile
def nidmm_fetch_waveform(session, args, num_points=sentinel):
    if num_points is sentinel:
        num_points = args.acq_size
    if args.numpy:
        wfm_array, actual_num_points = session.fetch_waveform_numpy(num_points, maximum_time=100000)
    else:
        wfm_array, actual_num_points = session.fetch_waveform(num_points, maximum_time=100000)
    assert actual_num_points == num_points
    return wfm_array, actual_num_points


@profile
def nidmm_stream_waveform(session, args):
    if args.sleep > 0:
        time.sleep(args.sleep)
    total_points = 0
    backlog, acq_status = session.read_status()
    while total_points < args.acq_size and acq_status == nidmm.AcquisitionStatus.RUNNING:
        wfm_array, actual_num_points = nidmm_fetch_waveform(session, args, backlog)
        total_points += actual_num_points
        if args.sleep > 0:
            time.sleep(args.sleep)
        backlog, acq_status = session.read_status()


@profile
def nidmm_close(session, args):
    session.close()


def _main(args):  # pragma: no cover.
    print('Please wait, running...')
    session = nidmm_init(args)
    nidmm_configure(session, args)
    nidmm_initiate(session, args)
    if args.stream:
        nidmm_stream_waveform(session, args)
    else:
        nidmm_wait_for_ready(session, args)
        nidmm_fetch_waveform(session, args)
    nidmm_close(session, args)
    print_prof_data()
    return 0


def configure_logging(lvl=logging.WARNING, logfile=None):
    root = logging.getLogger()
    root.setLevel(lvl)

    formatter = logging.Formatter("[%(asctime)s] [%(levelname)8s] --- %(message)s (%(filename)s:%(funcName)s:%(lineno)s)", "%Y-%m-%d %H:%M:%S")
    if logfile is None:
        hndlr = logging.StreamHandler(sys.stdout)
    else:
        print("Logging to file %s" % logfile)
        hndlr = logging.FileHandler(logfile)
    hndlr.setFormatter(formatter)
    root.addHandler(hndlr)


def _parse_args(argv):

    # Setup the required arguments for this script
    usage = """
Test waveform acquisition performance
"""
    parser = argparse.ArgumentParser(description=usage)
    test_config_group = parser.add_argument_group("Test configuration")
    test_config_group.add_argument(
        "--range", type=float,
        action="store", default=10,
        help="Range")
    test_config_group.add_argument(
        "--rate", type=float,
        action="store", default=1800000,
        help="Rate")
    test_config_group.add_argument(
        "--acq-size", type=int,
        action="store", default=1000000,
        help="Acquisition size - number of points")
    test_config_group.add_argument(
        "--stream",
        action="store_true", default=False,
        help="Stream as points available - if not set, wait until complete and fetch all")
    test_config_group.add_argument(
        "--sleep", type=float,
        action="store", default=1.0,
        help="If streaming, how long to sleep between fetch")
    test_config_group.add_argument(
        "--numpy",
        action="store_true", default=False,
        help="Use numpy based fetch")

    verbosity_group = parser.add_argument_group("Verbosity, Logging & Debugging")
    verbosity_group.add_argument(
        "-v", "--verbose",
        action="count", default=0,
        help="Print debug information.  Can be repeated for more detailed output.")
    verbosity_group.add_argument(
        "-q", "--quiet",
        action="count", default=0,
        help="Print only essential information.  Can be repeated for quieter output.")
    verbosity_group.add_argument(
        "--test",
        action="store_true", default=False,
        help="Run doctests and quit")
    verbosity_group.add_argument(
        "--log-file",
        action="store", default=None,
        help="Send logging to listed file instead of stdout")
    args = parser.parse_args(argv)

    # We want to default to WARNING
    # Verbosity gives us granularity to control past that
    if 0 < args.verbose and 0 < args.quiet:
        parser.error("Mixing --verbose and --quiet is contradictory")
    verbosity = 2 + args.quiet - args.verbose
    verbosity = max(verbosity, 0)
    verbosity = min(verbosity, 4)
    args.logging_level = {
        0: logging.DEBUG,
        1: logging.INFO,
        2: logging.WARNING,
        3: logging.ERROR,
        4: logging.CRITICAL,
    }[verbosity]

    if args.test:
        return args

    # TODO(NI) Parameter checks here if applicable

    return args


def main():  # pragma: no cover
    import sys
    args = _parse_args(sys.argv[1:])

    configure_logging(args.logging_level, args.log_file)
    logging.info(pp.pformat(args))

    if args.test:
        import doctest
        print(doctest.testmod())
        return 0

    ret_code = _main(args)
    sys.exit(ret_code)


if __name__ == "__main__":  # pragma: no cover
    main()



