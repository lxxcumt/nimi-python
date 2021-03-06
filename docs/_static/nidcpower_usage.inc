Usage
------

The following is a basic example of using the **nidcpower** module to open a session to a Source Meter Unit and measure voltage and current.

.. code-block:: python

    import nidcpower
    # Configure the session.
    session.measure_record_length = 20
    session.measure_record_length_is_finite = True
    session.measure_when = nidcpower.MeasureWhen.AUTOMATICALLY_AFTER_SOURCE_COMPLETE
    session.voltage_level = 5.0

    session.commit()
    print('Effective measurement rate: {0} S/s'.format(session.measure_record_delta_time / 1))

    samples_acquired = 0
    print('  #    Voltage    Current    In Compliance')
    row_format = '{0:3d}:   {1:8.6f}   {2:8.6f}   {3}'
    with session.initiate():
        while samples_acquired < 20:
            voltage_measurements, current_measurements, in_compliance = session.fetch_multiple(count=session.fetch_backlog)
            samples_acquired += len(voltage_measurements)
            for i in zip(range(len(voltage_measurements)), voltage_measurements, current_measurements, in_compliance):
                print(row_format.format(i[0], i[1], i[2], i[3]))

Additional examples for NI-DCPower are located in src/nidcpower/examples/ directory.

