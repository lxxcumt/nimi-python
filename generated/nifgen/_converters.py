from nifgen import visatype

import datetime
import six


def convert_repeated_capabilities(repeated_capability, prefix=''):
    # First look for a string
    if isinstance(repeated_capability, six.text_type) or isinstance(repeated_capability, six.string_types):
        rep_cap_list = [repeated_capability if repeated_capability.lower().startswith(prefix.lower()) else prefix + repeated_capability]
    else:
        # if not a string, try it as an iterable
        try:
            rep_cap_list = [str(r) if str(r).lower().startswith(prefix.lower()) else prefix + str(r) for r in repeated_capability]
        except TypeError:
            # If that doesn't work, then try it as a slice
            try:
                def ifnone(a, b):
                    return b if a is None else a
                # Turn the slice into a list so we can iterate over it
                rep_cap_list = list(range(ifnone(repeated_capability.start, 0), repeated_capability.stop, ifnone(repeated_capability.step, 1)))
                # Now it is a list, so we call ourselves
                return convert_repeated_capabilities(rep_cap_list, prefix)
            # Otherwise it must be a single item that is not a string
            except (TypeError, AttributeError):
                rep_cap_list = [str(repeated_capability) if str(repeated_capability).lower().startswith(prefix.lower()) else prefix + str(repeated_capability)]

    return ','.join(rep_cap_list)


def _convert_timedelta(value, library_type, scaling):
    scaled_value = value.total_seconds() * scaling

    # ctype integer types don't convert to int from float so we need to
    if library_type in [visatype.ViInt64, visatype.ViInt32, visatype.ViUInt32, visatype.ViInt16, visatype.ViUInt16, visatype.ViInt8]:
        scaled_value = int(scaled_value)

    return library_type(scaled_value)


def convert_timedelta_to_seconds(value, library_type):
    return _convert_timedelta(value, library_type, 1)


def convert_timedelta_to_milliseconds(value, library_type):
    return _convert_timedelta(value, library_type, 1000)


def convert_timedelta_to_microseconds(value, library_type):
    return _convert_timedelta(value, library_type, 1000000)


# This converter is not called from the normal codegen path for function. Instead it is
# call from init and is a special case. Also, it just returns a string rather than a ctype object
def convert_init_with_options_dictionary(values, encoding):
    if type(values) is str:
        init_with_options_string = values
    else:
        good_keys = {
            'rangecheck': 'RangeCheck',
            'queryinstrstatus': 'QueryInstrStatus',
            'cache': 'Cache',
            'simulate': 'Simulate',
            'recordcoercions': 'RecordCoercions',
            'interchangecheck': 'InterchangeCheck',
            'driversetup': 'DriverSetup',
            'range_check': 'RangeCheck',
            'query_instr_status': 'QueryInstrStatus',
            'record_coercions': 'RecordCoercions',
            'interchange_check': 'InterchangeCheck',
            'driver_setup': 'DriverSetup',
        }
        init_with_options = []
        for k in sorted(values.keys()):
            value = None
            if k.lower() in good_keys and not good_keys[k.lower()] == 'DriverSetup':
                value = good_keys[k.lower()] + ('=1' if values[k] is True else '=0')
            elif k.lower() in good_keys and good_keys[k.lower()] == 'DriverSetup':
                if not isinstance(values[k], dict):
                    raise TypeError('DriverSetup must be a dictionary')
                value = 'DriverSetup=' + (';'.join([key + ':' + values[k][key] for key in sorted(values[k])]))
            else:
                value = k + ('=1' if values[k] is True else '=0')

            init_with_options.append(value)

        init_with_options_string = ','.join(init_with_options)

    return init_with_options_string


# Let's run some tests
def test_convert_init_with_options_dictionary():
    assert convert_init_with_options_dictionary('', 'ascii') == ''
    assert convert_init_with_options_dictionary('Simulate=1', 'ascii') == 'Simulate=1'
    assert convert_init_with_options_dictionary({'Simulate': True, }, 'ascii') == 'Simulate=1'
    assert convert_init_with_options_dictionary({'Simulate': False, }, 'ascii') == 'Simulate=0'
    assert convert_init_with_options_dictionary({'Simulate': True, 'Cache': False}, 'ascii') == 'Cache=0,Simulate=1'
    assert convert_init_with_options_dictionary({'DriverSetup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}, 'ascii') == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH)'
    assert convert_init_with_options_dictionary({'Simulate': True, 'DriverSetup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}, 'ascii') == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH),Simulate=1'
    assert convert_init_with_options_dictionary({'simulate': True, 'cache': False}, 'ascii') == 'Cache=0,Simulate=1'
    assert convert_init_with_options_dictionary({'driver_setup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}, 'ascii') == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH)'
    assert convert_init_with_options_dictionary({'simulate': True, 'driver_setup': {'Model': '5162 (4CH)', 'Bitfile': 'CustomProcessing'}}, 'ascii') == 'DriverSetup=Bitfile:CustomProcessing;Model:5162 (4CH),Simulate=1'


# Tests - time
def test_convert_timedelta_to_seconds_double():
    test_result = convert_timedelta_to_seconds(datetime.timedelta(seconds=10), visatype.ViReal64)
    assert test_result.value == 10.0
    assert isinstance(test_result, visatype.ViReal64)
    test_result = convert_timedelta_to_seconds(datetime.timedelta(seconds=-1), visatype.ViReal64)
    assert test_result.value == -1
    assert isinstance(test_result, visatype.ViReal64)


def test_convert_timedelta_to_seconds_int():
    test_result = convert_timedelta_to_seconds(datetime.timedelta(seconds=10), visatype.ViInt32)
    assert test_result.value == 10
    assert isinstance(test_result, visatype.ViInt32)
    test_result = convert_timedelta_to_seconds(datetime.timedelta(seconds=-1), visatype.ViInt32)
    assert test_result.value == -1
    assert isinstance(test_result, visatype.ViInt32)


def test_convert_timedelta_to_milliseconds_double():
    test_result = convert_timedelta_to_milliseconds(datetime.timedelta(seconds=10), visatype.ViReal64)
    assert test_result.value == 10000.0
    assert isinstance(test_result, visatype.ViReal64)
    test_result = convert_timedelta_to_milliseconds(datetime.timedelta(seconds=-1), visatype.ViReal64)
    assert test_result.value == -1000.0
    assert isinstance(test_result, visatype.ViReal64)


def test_convert_timedelta_to_milliseconds_int():
    test_result = convert_timedelta_to_milliseconds(datetime.timedelta(seconds=10), visatype.ViInt32)
    assert test_result.value == 10000
    assert isinstance(test_result, visatype.ViInt32)
    test_result = convert_timedelta_to_milliseconds(datetime.timedelta(seconds=-1), visatype.ViInt32)
    assert test_result.value == -1000
    assert isinstance(test_result, visatype.ViInt32)


def test_convert_timedelta_to_microseconds_double():
    test_result = convert_timedelta_to_microseconds(datetime.timedelta(seconds=10), visatype.ViReal64)
    assert test_result.value == 10000000.0
    assert isinstance(test_result, visatype.ViReal64)
    test_result = convert_timedelta_to_microseconds(datetime.timedelta(seconds=-1), visatype.ViReal64)
    assert test_result.value == -1000000.0
    assert isinstance(test_result, visatype.ViReal64)


def test_convert_timedelta_to_microseconds_int():
    test_result = convert_timedelta_to_microseconds(datetime.timedelta(seconds=10), visatype.ViInt32)
    assert test_result.value == 10000000
    assert isinstance(test_result, visatype.ViInt32)
    test_result = convert_timedelta_to_microseconds(datetime.timedelta(seconds=-1), visatype.ViInt32)
    assert test_result.value == -1000000
    assert isinstance(test_result, visatype.ViInt32)


# Tests - repeated capabilities
def test_repeated_capabilies_string_channel():
    test_result = convert_repeated_capabilities('0')
    assert test_result == '0'
    test_result = convert_repeated_capabilities('0,1')
    assert test_result == '0,1'


def test_repeated_capabilies_string_prefix():
    test_result = convert_repeated_capabilities('0', prefix='ScriptTrigger')
    assert test_result == 'ScriptTrigger0'


def test_repeated_capabilies_list_channel():
    test_result = convert_repeated_capabilities(['0'])
    assert test_result == '0'
    test_result = convert_repeated_capabilities(['0,1'])
    assert test_result == '0,1'
    test_result = convert_repeated_capabilities(['0', '1'])
    assert test_result == '0,1'
    test_result = convert_repeated_capabilities([0, 1])
    assert test_result == '0,1'
    test_result = convert_repeated_capabilities([0, 1, '3'])
    assert test_result == '0,1,3'


def test_repeated_capabilies_list_prefix():
    test_result = convert_repeated_capabilities(['ScriptTrigger0,ScriptTrigger1'], prefix='ScriptTrigger')
    assert test_result == 'ScriptTrigger0,ScriptTrigger1'
    test_result = convert_repeated_capabilities(['0'], prefix='ScriptTrigger')
    assert test_result == 'ScriptTrigger0'
    test_result = convert_repeated_capabilities(['0', '1'], prefix='ScriptTrigger')
    assert test_result == 'ScriptTrigger0,ScriptTrigger1'
    test_result = convert_repeated_capabilities([0, 1], prefix='ScriptTrigger')
    assert test_result == 'ScriptTrigger0,ScriptTrigger1'


def test_repeated_capabilies_slice_channel():
    test_result = convert_repeated_capabilities(slice(0, 1))
    assert test_result == '0'
    test_result = convert_repeated_capabilities(slice(0, 2))
    assert test_result == '0,1'
    test_result = convert_repeated_capabilities(slice(None, 2))
    assert test_result == '0,1'


def test_repeated_capabilies_slice_prefix():
    test_result = convert_repeated_capabilities(slice(0, 1), prefix='ScriptTrigger')
    assert test_result == 'ScriptTrigger0'
    test_result = convert_repeated_capabilities(slice(0, 2), prefix='ScriptTrigger')
    assert test_result == 'ScriptTrigger0,ScriptTrigger1'
    test_result = convert_repeated_capabilities(slice(None, 2), prefix='ScriptTrigger')
    assert test_result == 'ScriptTrigger0,ScriptTrigger1'

