# This file was generated
import sys  # noqa: F401   - Not all mock_helpers will need this


class MockFunctionCallError(Exception):
    def __init__(self, function, param=None):
        self.function = function
        self.param = param
        msg = "{0} called without setting side_effect".format(self.function)
        if param is not None:
            msg += " or setting the {0} parameter return value".format(self.param)
        super(Exception, self).__init__(msg)


class SideEffectsHelper(object):
    def __init__(self):
        self._defaults = {}
        self._defaults['Abort'] = {}
        self._defaults['Abort']['return'] = 0
        self._defaults['Commit'] = {}
        self._defaults['Commit']['return'] = 0
        self._defaults['ConfigureApertureTime'] = {}
        self._defaults['ConfigureApertureTime']['return'] = 0
        self._defaults['ConfigureDigitalEdgeMeasureTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeMeasureTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgePulseTrigger'] = {}
        self._defaults['ConfigureDigitalEdgePulseTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgeSequenceAdvanceTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeSequenceAdvanceTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgeSourceTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeSourceTrigger']['return'] = 0
        self._defaults['ConfigureDigitalEdgeStartTrigger'] = {}
        self._defaults['ConfigureDigitalEdgeStartTrigger']['return'] = 0
        self._defaults['CreateAdvancedSequence'] = {}
        self._defaults['CreateAdvancedSequence']['return'] = 0
        self._defaults['CreateAdvancedSequenceStep'] = {}
        self._defaults['CreateAdvancedSequenceStep']['return'] = 0
        self._defaults['DeleteAdvancedSequence'] = {}
        self._defaults['DeleteAdvancedSequence']['return'] = 0
        self._defaults['Disable'] = {}
        self._defaults['Disable']['return'] = 0
        self._defaults['ExportSignal'] = {}
        self._defaults['ExportSignal']['return'] = 0
        self._defaults['FetchMultiple'] = {}
        self._defaults['FetchMultiple']['return'] = 0
        self._defaults['FetchMultiple']['voltageMeasurements'] = None
        self._defaults['FetchMultiple']['currentMeasurements'] = None
        self._defaults['FetchMultiple']['inCompliance'] = None
        self._defaults['FetchMultiple']['actualCount'] = None
        self._defaults['GetAttributeViBoolean'] = {}
        self._defaults['GetAttributeViBoolean']['return'] = 0
        self._defaults['GetAttributeViBoolean']['attributeValue'] = None
        self._defaults['GetAttributeViInt32'] = {}
        self._defaults['GetAttributeViInt32']['return'] = 0
        self._defaults['GetAttributeViInt32']['attributeValue'] = None
        self._defaults['GetAttributeViInt64'] = {}
        self._defaults['GetAttributeViInt64']['return'] = 0
        self._defaults['GetAttributeViInt64']['attributeValue'] = None
        self._defaults['GetAttributeViReal64'] = {}
        self._defaults['GetAttributeViReal64']['return'] = 0
        self._defaults['GetAttributeViReal64']['attributeValue'] = None
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViString']['attributeValue'] = None
        self._defaults['GetChannelName'] = {}
        self._defaults['GetChannelName']['return'] = 0
        self._defaults['GetChannelName']['channelName'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['Code'] = None
        self._defaults['GetError']['Description'] = None
        self._defaults['GetExtCalLastDateAndTime'] = {}
        self._defaults['GetExtCalLastDateAndTime']['return'] = 0
        self._defaults['GetExtCalLastDateAndTime']['Year'] = None
        self._defaults['GetExtCalLastDateAndTime']['Month'] = None
        self._defaults['GetExtCalLastDateAndTime']['Day'] = None
        self._defaults['GetExtCalLastDateAndTime']['Hour'] = None
        self._defaults['GetExtCalLastDateAndTime']['Minute'] = None
        self._defaults['GetExtCalLastTemp'] = {}
        self._defaults['GetExtCalLastTemp']['return'] = 0
        self._defaults['GetExtCalLastTemp']['Temperature'] = None
        self._defaults['GetExtCalRecommendedInterval'] = {}
        self._defaults['GetExtCalRecommendedInterval']['return'] = 0
        self._defaults['GetExtCalRecommendedInterval']['Months'] = None
        self._defaults['GetLastExtCalLastDateAndTime'] = {}
        self._defaults['GetLastExtCalLastDateAndTime']['return'] = 0
        self._defaults['GetLastExtCalLastDateAndTime']['Month'] = None
        self._defaults['GetLastSelfCalLastDateAndTime'] = {}
        self._defaults['GetLastSelfCalLastDateAndTime']['return'] = 0
        self._defaults['GetLastSelfCalLastDateAndTime']['Month'] = None
        self._defaults['GetSelfCalLastDateAndTime'] = {}
        self._defaults['GetSelfCalLastDateAndTime']['return'] = 0
        self._defaults['GetSelfCalLastDateAndTime']['Year'] = None
        self._defaults['GetSelfCalLastDateAndTime']['Month'] = None
        self._defaults['GetSelfCalLastDateAndTime']['Day'] = None
        self._defaults['GetSelfCalLastDateAndTime']['Hour'] = None
        self._defaults['GetSelfCalLastDateAndTime']['Minute'] = None
        self._defaults['GetSelfCalLastTemp'] = {}
        self._defaults['GetSelfCalLastTemp']['return'] = 0
        self._defaults['GetSelfCalLastTemp']['Temperature'] = None
        self._defaults['InitializeWithChannels'] = {}
        self._defaults['InitializeWithChannels']['return'] = 0
        self._defaults['InitializeWithChannels']['vi'] = None
        self._defaults['Initiate'] = {}
        self._defaults['Initiate']['return'] = 0
        self._defaults['Measure'] = {}
        self._defaults['Measure']['return'] = 0
        self._defaults['Measure']['Measurement'] = None
        self._defaults['MeasureMultiple'] = {}
        self._defaults['MeasureMultiple']['return'] = 0
        self._defaults['MeasureMultiple']['voltageMeasurements'] = None
        self._defaults['MeasureMultiple']['currentMeasurements'] = None
        self._defaults['ParseChannelCount'] = {}
        self._defaults['ParseChannelCount']['return'] = 0
        self._defaults['ParseChannelCount']['numberOfChannels'] = None
        self._defaults['QueryInCompliance'] = {}
        self._defaults['QueryInCompliance']['return'] = 0
        self._defaults['QueryInCompliance']['inCompliance'] = None
        self._defaults['QueryMaxCurrentLimit'] = {}
        self._defaults['QueryMaxCurrentLimit']['return'] = 0
        self._defaults['QueryMaxCurrentLimit']['maxCurrentLimit'] = None
        self._defaults['QueryMaxVoltageLevel'] = {}
        self._defaults['QueryMaxVoltageLevel']['return'] = 0
        self._defaults['QueryMaxVoltageLevel']['maxVoltageLevel'] = None
        self._defaults['QueryMinCurrentLimit'] = {}
        self._defaults['QueryMinCurrentLimit']['return'] = 0
        self._defaults['QueryMinCurrentLimit']['minCurrentLimit'] = None
        self._defaults['QueryOutputState'] = {}
        self._defaults['QueryOutputState']['return'] = 0
        self._defaults['QueryOutputState']['inState'] = None
        self._defaults['ReadCurrentTemperature'] = {}
        self._defaults['ReadCurrentTemperature']['return'] = 0
        self._defaults['ReadCurrentTemperature']['Temperature'] = None
        self._defaults['ResetDevice'] = {}
        self._defaults['ResetDevice']['return'] = 0
        self._defaults['ResetWithDefaults'] = {}
        self._defaults['ResetWithDefaults']['return'] = 0
        self._defaults['SendSoftwareEdgeTrigger'] = {}
        self._defaults['SendSoftwareEdgeTrigger']['return'] = 0
        self._defaults['SetAttributeViBoolean'] = {}
        self._defaults['SetAttributeViBoolean']['return'] = 0
        self._defaults['SetAttributeViInt32'] = {}
        self._defaults['SetAttributeViInt32']['return'] = 0
        self._defaults['SetAttributeViInt64'] = {}
        self._defaults['SetAttributeViInt64']['return'] = 0
        self._defaults['SetAttributeViReal64'] = {}
        self._defaults['SetAttributeViReal64']['return'] = 0
        self._defaults['SetAttributeViString'] = {}
        self._defaults['SetAttributeViString']['return'] = 0
        self._defaults['SetSequence'] = {}
        self._defaults['SetSequence']['return'] = 0
        self._defaults['WaitForEvent'] = {}
        self._defaults['WaitForEvent']['return'] = 0
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0
        self._defaults['error_message'] = {}
        self._defaults['error_message']['return'] = 0
        self._defaults['error_message']['errorMessage'] = None
        self._defaults['reset'] = {}
        self._defaults['reset']['return'] = 0
        self._defaults['self_test'] = {}
        self._defaults['self_test']['return'] = 0
        self._defaults['self_test']['selfTestResult'] = None
        self._defaults['self_test']['selfTestMessage'] = None

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niDCPower_Abort(self, vi):  # noqa: N802
        if self._defaults['Abort']['return'] != 0:
            return self._defaults['Abort']['return']
        return self._defaults['Abort']['return']

    def niDCPower_Commit(self, vi):  # noqa: N802
        if self._defaults['Commit']['return'] != 0:
            return self._defaults['Commit']['return']
        return self._defaults['Commit']['return']

    def niDCPower_ConfigureApertureTime(self, vi, channel_name, aperture_time, units):  # noqa: N802
        if self._defaults['ConfigureApertureTime']['return'] != 0:
            return self._defaults['ConfigureApertureTime']['return']
        return self._defaults['ConfigureApertureTime']['return']

    def niDCPower_ConfigureDigitalEdgeMeasureTrigger(self, vi, input_terminal, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeMeasureTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeMeasureTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeMeasureTrigger']['return']

    def niDCPower_ConfigureDigitalEdgePulseTrigger(self, vi, input_terminal, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgePulseTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgePulseTrigger']['return']
        return self._defaults['ConfigureDigitalEdgePulseTrigger']['return']

    def niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger(self, vi, input_terminal, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeSequenceAdvanceTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeSequenceAdvanceTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeSequenceAdvanceTrigger']['return']

    def niDCPower_ConfigureDigitalEdgeSourceTrigger(self, vi, input_terminal, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeSourceTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeSourceTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeSourceTrigger']['return']

    def niDCPower_ConfigureDigitalEdgeStartTrigger(self, vi, input_terminal, edge):  # noqa: N802
        if self._defaults['ConfigureDigitalEdgeStartTrigger']['return'] != 0:
            return self._defaults['ConfigureDigitalEdgeStartTrigger']['return']
        return self._defaults['ConfigureDigitalEdgeStartTrigger']['return']

    def niDCPower_CreateAdvancedSequence(self, vi, sequence_name, attribute_id_count, attribute_ids, set_as_active_sequence):  # noqa: N802
        if self._defaults['CreateAdvancedSequence']['return'] != 0:
            return self._defaults['CreateAdvancedSequence']['return']
        return self._defaults['CreateAdvancedSequence']['return']

    def niDCPower_CreateAdvancedSequenceStep(self, vi, set_as_active_step):  # noqa: N802
        if self._defaults['CreateAdvancedSequenceStep']['return'] != 0:
            return self._defaults['CreateAdvancedSequenceStep']['return']
        return self._defaults['CreateAdvancedSequenceStep']['return']

    def niDCPower_DeleteAdvancedSequence(self, vi, sequence_name):  # noqa: N802
        if self._defaults['DeleteAdvancedSequence']['return'] != 0:
            return self._defaults['DeleteAdvancedSequence']['return']
        return self._defaults['DeleteAdvancedSequence']['return']

    def niDCPower_Disable(self, vi):  # noqa: N802
        if self._defaults['Disable']['return'] != 0:
            return self._defaults['Disable']['return']
        return self._defaults['Disable']['return']

    def niDCPower_ExportSignal(self, vi, signal, signal_identifier, output_terminal):  # noqa: N802
        if self._defaults['ExportSignal']['return'] != 0:
            return self._defaults['ExportSignal']['return']
        return self._defaults['ExportSignal']['return']

    def niDCPower_FetchMultiple(self, vi, channel_name, timeout, count, voltage_measurements, current_measurements, in_compliance, actual_count):  # noqa: N802
        if self._defaults['FetchMultiple']['return'] != 0:
            return self._defaults['FetchMultiple']['return']
        # voltage_measurements
        if self._defaults['FetchMultiple']['voltageMeasurements'] is None:
            raise MockFunctionCallError("niDCPower_FetchMultiple", param='voltageMeasurements')
        test_value = self._defaults['FetchMultiple']['voltageMeasurements']
        try:
            voltage_measurements_ref = voltage_measurements.contents
        except AttributeError:
            voltage_measurements_ref = voltage_measurements
        assert len(voltage_measurements_ref) >= len(test_value)
        for i in range(len(test_value)):
            voltage_measurements_ref[i] = test_value[i]
        # current_measurements
        if self._defaults['FetchMultiple']['currentMeasurements'] is None:
            raise MockFunctionCallError("niDCPower_FetchMultiple", param='currentMeasurements')
        test_value = self._defaults['FetchMultiple']['currentMeasurements']
        try:
            current_measurements_ref = current_measurements.contents
        except AttributeError:
            current_measurements_ref = current_measurements
        assert len(current_measurements_ref) >= len(test_value)
        for i in range(len(test_value)):
            current_measurements_ref[i] = test_value[i]
        # in_compliance
        if self._defaults['FetchMultiple']['inCompliance'] is None:
            raise MockFunctionCallError("niDCPower_FetchMultiple", param='inCompliance')
        test_value = self._defaults['FetchMultiple']['inCompliance']
        try:
            in_compliance_ref = in_compliance.contents
        except AttributeError:
            in_compliance_ref = in_compliance
        assert len(in_compliance_ref) >= len(test_value)
        for i in range(len(test_value)):
            in_compliance_ref[i] = test_value[i]
        # actual_count
        if self._defaults['FetchMultiple']['actualCount'] is None:
            raise MockFunctionCallError("niDCPower_FetchMultiple", param='actualCount')
        actual_count.contents.value = self._defaults['FetchMultiple']['actualCount']
        return self._defaults['FetchMultiple']['return']

    def niDCPower_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        # attribute_value
        if self._defaults['GetAttributeViBoolean']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViBoolean", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViBoolean']['attributeValue']
        return self._defaults['GetAttributeViBoolean']['return']

    def niDCPower_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        # attribute_value
        if self._defaults['GetAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViInt32", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViInt32']['attributeValue']
        return self._defaults['GetAttributeViInt32']['return']

    def niDCPower_GetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt64']['return'] != 0:
            return self._defaults['GetAttributeViInt64']['return']
        # attribute_value
        if self._defaults['GetAttributeViInt64']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViInt64", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViInt64']['attributeValue']
        return self._defaults['GetAttributeViInt64']['return']

    def niDCPower_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # attribute_value
        if self._defaults['GetAttributeViReal64']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViReal64", param='attributeValue')
        attribute_value.contents.value = self._defaults['GetAttributeViReal64']['attributeValue']
        return self._defaults['GetAttributeViReal64']['return']

    def niDCPower_GetAttributeViString(self, vi, channel_name, attribute_id, buffer_size, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        if self._defaults['GetAttributeViString']['attributeValue'] is None:
            raise MockFunctionCallError("niDCPower_GetAttributeViString", param='attributeValue')
        if buffer_size.value == 0:
            return len(self._defaults['GetAttributeViString']['attributeValue'])
        attribute_value.value = self._defaults['GetAttributeViString']['attributeValue'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niDCPower_GetChannelName(self, vi, index, buffer_size, channel_name):  # noqa: N802
        if self._defaults['GetChannelName']['return'] != 0:
            return self._defaults['GetChannelName']['return']
        if self._defaults['GetChannelName']['channelName'] is None:
            raise MockFunctionCallError("niDCPower_GetChannelName", param='channelName')
        if buffer_size.value == 0:
            return len(self._defaults['GetChannelName']['channelName'])
        channel_name.value = self._defaults['GetChannelName']['channelName'].encode('ascii')
        return self._defaults['GetChannelName']['return']

    def niDCPower_GetError(self, vi, code, buffer_size, description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        # code
        if self._defaults['GetError']['Code'] is None:
            raise MockFunctionCallError("niDCPower_GetError", param='Code')
        code.contents.value = self._defaults['GetError']['Code']
        if self._defaults['GetError']['Description'] is None:
            raise MockFunctionCallError("niDCPower_GetError", param='Description')
        if buffer_size.value == 0:
            return len(self._defaults['GetError']['Description'])
        description.value = self._defaults['GetError']['Description'].encode('ascii')
        return self._defaults['GetError']['return']

    def niDCPower_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        if self._defaults['GetExtCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetExtCalLastDateAndTime']['return']
        # year
        if self._defaults['GetExtCalLastDateAndTime']['Year'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalLastDateAndTime", param='Year')
        year.contents.value = self._defaults['GetExtCalLastDateAndTime']['Year']
        # month
        if self._defaults['GetExtCalLastDateAndTime']['Month'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalLastDateAndTime", param='Month')
        month.contents.value = self._defaults['GetExtCalLastDateAndTime']['Month']
        # day
        if self._defaults['GetExtCalLastDateAndTime']['Day'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalLastDateAndTime", param='Day')
        day.contents.value = self._defaults['GetExtCalLastDateAndTime']['Day']
        # hour
        if self._defaults['GetExtCalLastDateAndTime']['Hour'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalLastDateAndTime", param='Hour')
        hour.contents.value = self._defaults['GetExtCalLastDateAndTime']['Hour']
        # minute
        if self._defaults['GetExtCalLastDateAndTime']['Minute'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalLastDateAndTime", param='Minute')
        minute.contents.value = self._defaults['GetExtCalLastDateAndTime']['Minute']
        return self._defaults['GetExtCalLastDateAndTime']['return']

    def niDCPower_GetExtCalLastTemp(self, vi, temperature):  # noqa: N802
        if self._defaults['GetExtCalLastTemp']['return'] != 0:
            return self._defaults['GetExtCalLastTemp']['return']
        # temperature
        if self._defaults['GetExtCalLastTemp']['Temperature'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalLastTemp", param='Temperature')
        temperature.contents.value = self._defaults['GetExtCalLastTemp']['Temperature']
        return self._defaults['GetExtCalLastTemp']['return']

    def niDCPower_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802
        if self._defaults['GetExtCalRecommendedInterval']['return'] != 0:
            return self._defaults['GetExtCalRecommendedInterval']['return']
        # months
        if self._defaults['GetExtCalRecommendedInterval']['Months'] is None:
            raise MockFunctionCallError("niDCPower_GetExtCalRecommendedInterval", param='Months')
        months.contents.value = self._defaults['GetExtCalRecommendedInterval']['Months']
        return self._defaults['GetExtCalRecommendedInterval']['return']

    def niDCPower_GetLastExtCalLastDateAndTime(self, vi, month):  # noqa: N802
        if self._defaults['GetLastExtCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetLastExtCalLastDateAndTime']['return']
        # month
        if self._defaults['GetLastExtCalLastDateAndTime']['Month'] is None:
            raise MockFunctionCallError("niDCPower_GetLastExtCalLastDateAndTime", param='Month')
        month.contents.value = self._defaults['GetLastExtCalLastDateAndTime']['Month']
        return self._defaults['GetLastExtCalLastDateAndTime']['return']

    def niDCPower_GetLastSelfCalLastDateAndTime(self, vi, month):  # noqa: N802
        if self._defaults['GetLastSelfCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetLastSelfCalLastDateAndTime']['return']
        # month
        if self._defaults['GetLastSelfCalLastDateAndTime']['Month'] is None:
            raise MockFunctionCallError("niDCPower_GetLastSelfCalLastDateAndTime", param='Month')
        month.contents.value = self._defaults['GetLastSelfCalLastDateAndTime']['Month']
        return self._defaults['GetLastSelfCalLastDateAndTime']['return']

    def niDCPower_GetSelfCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        if self._defaults['GetSelfCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetSelfCalLastDateAndTime']['return']
        # year
        if self._defaults['GetSelfCalLastDateAndTime']['Year'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime", param='Year')
        year.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Year']
        # month
        if self._defaults['GetSelfCalLastDateAndTime']['Month'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime", param='Month')
        month.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Month']
        # day
        if self._defaults['GetSelfCalLastDateAndTime']['Day'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime", param='Day')
        day.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Day']
        # hour
        if self._defaults['GetSelfCalLastDateAndTime']['Hour'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime", param='Hour')
        hour.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Hour']
        # minute
        if self._defaults['GetSelfCalLastDateAndTime']['Minute'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime", param='Minute')
        minute.contents.value = self._defaults['GetSelfCalLastDateAndTime']['Minute']
        return self._defaults['GetSelfCalLastDateAndTime']['return']

    def niDCPower_GetSelfCalLastTemp(self, vi, temperature):  # noqa: N802
        if self._defaults['GetSelfCalLastTemp']['return'] != 0:
            return self._defaults['GetSelfCalLastTemp']['return']
        # temperature
        if self._defaults['GetSelfCalLastTemp']['Temperature'] is None:
            raise MockFunctionCallError("niDCPower_GetSelfCalLastTemp", param='Temperature')
        temperature.contents.value = self._defaults['GetSelfCalLastTemp']['Temperature']
        return self._defaults['GetSelfCalLastTemp']['return']

    def niDCPower_InitializeWithChannels(self, resource_name, channels, reset, option_string, vi):  # noqa: N802
        if self._defaults['InitializeWithChannels']['return'] != 0:
            return self._defaults['InitializeWithChannels']['return']
        # vi
        if self._defaults['InitializeWithChannels']['vi'] is None:
            raise MockFunctionCallError("niDCPower_InitializeWithChannels", param='vi')
        vi.contents.value = self._defaults['InitializeWithChannels']['vi']
        return self._defaults['InitializeWithChannels']['return']

    def niDCPower_Initiate(self, vi):  # noqa: N802
        if self._defaults['Initiate']['return'] != 0:
            return self._defaults['Initiate']['return']
        return self._defaults['Initiate']['return']

    def niDCPower_Measure(self, vi, channel_name, measurement_type, measurement):  # noqa: N802
        if self._defaults['Measure']['return'] != 0:
            return self._defaults['Measure']['return']
        # measurement
        if self._defaults['Measure']['Measurement'] is None:
            raise MockFunctionCallError("niDCPower_Measure", param='Measurement')
        measurement.contents.value = self._defaults['Measure']['Measurement']
        return self._defaults['Measure']['return']

    def niDCPower_MeasureMultiple(self, vi, channel_name, voltage_measurements, current_measurements):  # noqa: N802
        if self._defaults['MeasureMultiple']['return'] != 0:
            return self._defaults['MeasureMultiple']['return']
        # voltage_measurements
        if self._defaults['MeasureMultiple']['voltageMeasurements'] is None:
            raise MockFunctionCallError("niDCPower_MeasureMultiple", param='voltageMeasurements')
        test_value = self._defaults['MeasureMultiple']['voltageMeasurements']
        try:
            voltage_measurements_ref = voltage_measurements.contents
        except AttributeError:
            voltage_measurements_ref = voltage_measurements
        assert len(voltage_measurements_ref) >= len(test_value)
        for i in range(len(test_value)):
            voltage_measurements_ref[i] = test_value[i]
        # current_measurements
        if self._defaults['MeasureMultiple']['currentMeasurements'] is None:
            raise MockFunctionCallError("niDCPower_MeasureMultiple", param='currentMeasurements')
        test_value = self._defaults['MeasureMultiple']['currentMeasurements']
        try:
            current_measurements_ref = current_measurements.contents
        except AttributeError:
            current_measurements_ref = current_measurements
        assert len(current_measurements_ref) >= len(test_value)
        for i in range(len(test_value)):
            current_measurements_ref[i] = test_value[i]
        return self._defaults['MeasureMultiple']['return']

    def niDCPower_ParseChannelCount(self, vi, channels_string, number_of_channels):  # noqa: N802
        if self._defaults['ParseChannelCount']['return'] != 0:
            return self._defaults['ParseChannelCount']['return']
        # number_of_channels
        if self._defaults['ParseChannelCount']['numberOfChannels'] is None:
            raise MockFunctionCallError("niDCPower_ParseChannelCount", param='numberOfChannels')
        number_of_channels.contents.value = self._defaults['ParseChannelCount']['numberOfChannels']
        return self._defaults['ParseChannelCount']['return']

    def niDCPower_QueryInCompliance(self, vi, channel_name, in_compliance):  # noqa: N802
        if self._defaults['QueryInCompliance']['return'] != 0:
            return self._defaults['QueryInCompliance']['return']
        # in_compliance
        if self._defaults['QueryInCompliance']['inCompliance'] is None:
            raise MockFunctionCallError("niDCPower_QueryInCompliance", param='inCompliance')
        in_compliance.contents.value = self._defaults['QueryInCompliance']['inCompliance']
        return self._defaults['QueryInCompliance']['return']

    def niDCPower_QueryMaxCurrentLimit(self, vi, channel_name, voltage_level, max_current_limit):  # noqa: N802
        if self._defaults['QueryMaxCurrentLimit']['return'] != 0:
            return self._defaults['QueryMaxCurrentLimit']['return']
        # max_current_limit
        if self._defaults['QueryMaxCurrentLimit']['maxCurrentLimit'] is None:
            raise MockFunctionCallError("niDCPower_QueryMaxCurrentLimit", param='maxCurrentLimit')
        max_current_limit.contents.value = self._defaults['QueryMaxCurrentLimit']['maxCurrentLimit']
        return self._defaults['QueryMaxCurrentLimit']['return']

    def niDCPower_QueryMaxVoltageLevel(self, vi, channel_name, current_limit, max_voltage_level):  # noqa: N802
        if self._defaults['QueryMaxVoltageLevel']['return'] != 0:
            return self._defaults['QueryMaxVoltageLevel']['return']
        # max_voltage_level
        if self._defaults['QueryMaxVoltageLevel']['maxVoltageLevel'] is None:
            raise MockFunctionCallError("niDCPower_QueryMaxVoltageLevel", param='maxVoltageLevel')
        max_voltage_level.contents.value = self._defaults['QueryMaxVoltageLevel']['maxVoltageLevel']
        return self._defaults['QueryMaxVoltageLevel']['return']

    def niDCPower_QueryMinCurrentLimit(self, vi, channel_name, voltage_level, min_current_limit):  # noqa: N802
        if self._defaults['QueryMinCurrentLimit']['return'] != 0:
            return self._defaults['QueryMinCurrentLimit']['return']
        # min_current_limit
        if self._defaults['QueryMinCurrentLimit']['minCurrentLimit'] is None:
            raise MockFunctionCallError("niDCPower_QueryMinCurrentLimit", param='minCurrentLimit')
        min_current_limit.contents.value = self._defaults['QueryMinCurrentLimit']['minCurrentLimit']
        return self._defaults['QueryMinCurrentLimit']['return']

    def niDCPower_QueryOutputState(self, vi, channel_name, output_state, in_state):  # noqa: N802
        if self._defaults['QueryOutputState']['return'] != 0:
            return self._defaults['QueryOutputState']['return']
        # in_state
        if self._defaults['QueryOutputState']['inState'] is None:
            raise MockFunctionCallError("niDCPower_QueryOutputState", param='inState')
        in_state.contents.value = self._defaults['QueryOutputState']['inState']
        return self._defaults['QueryOutputState']['return']

    def niDCPower_ReadCurrentTemperature(self, vi, temperature):  # noqa: N802
        if self._defaults['ReadCurrentTemperature']['return'] != 0:
            return self._defaults['ReadCurrentTemperature']['return']
        # temperature
        if self._defaults['ReadCurrentTemperature']['Temperature'] is None:
            raise MockFunctionCallError("niDCPower_ReadCurrentTemperature", param='Temperature')
        temperature.contents.value = self._defaults['ReadCurrentTemperature']['Temperature']
        return self._defaults['ReadCurrentTemperature']['return']

    def niDCPower_ResetDevice(self, vi):  # noqa: N802
        if self._defaults['ResetDevice']['return'] != 0:
            return self._defaults['ResetDevice']['return']
        return self._defaults['ResetDevice']['return']

    def niDCPower_ResetWithDefaults(self, vi):  # noqa: N802
        if self._defaults['ResetWithDefaults']['return'] != 0:
            return self._defaults['ResetWithDefaults']['return']
        return self._defaults['ResetWithDefaults']['return']

    def niDCPower_SendSoftwareEdgeTrigger(self, vi, trigger):  # noqa: N802
        if self._defaults['SendSoftwareEdgeTrigger']['return'] != 0:
            return self._defaults['SendSoftwareEdgeTrigger']['return']
        return self._defaults['SendSoftwareEdgeTrigger']['return']

    def niDCPower_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niDCPower_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niDCPower_SetAttributeViInt64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt64']['return'] != 0:
            return self._defaults['SetAttributeViInt64']['return']
        return self._defaults['SetAttributeViInt64']['return']

    def niDCPower_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niDCPower_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niDCPower_SetSequence(self, vi, channel_name, values, source_delays, size):  # noqa: N802
        if self._defaults['SetSequence']['return'] != 0:
            return self._defaults['SetSequence']['return']
        return self._defaults['SetSequence']['return']

    def niDCPower_WaitForEvent(self, vi, event_id, timeout):  # noqa: N802
        if self._defaults['WaitForEvent']['return'] != 0:
            return self._defaults['WaitForEvent']['return']
        return self._defaults['WaitForEvent']['return']

    def niDCPower_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niDCPower_error_message(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['error_message']['return'] != 0:
            return self._defaults['error_message']['return']
        # error_message
        if self._defaults['error_message']['errorMessage'] is None:
            raise MockFunctionCallError("niDCPower_error_message", param='errorMessage')
        test_value = self._defaults['error_message']['errorMessage']
        if sys.version_info.major > 2 and type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(error_message) >= len(test_value)
        for i in range(len(test_value)):
            error_message[i] = test_value[i]
        return self._defaults['error_message']['return']

    def niDCPower_reset(self, vi):  # noqa: N802
        if self._defaults['reset']['return'] != 0:
            return self._defaults['reset']['return']
        return self._defaults['reset']['return']

    def niDCPower_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        # self_test_result
        if self._defaults['self_test']['selfTestResult'] is None:
            raise MockFunctionCallError("niDCPower_self_test", param='selfTestResult')
        self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        # self_test_message
        if self._defaults['self_test']['selfTestMessage'] is None:
            raise MockFunctionCallError("niDCPower_self_test", param='selfTestMessage')
        test_value = self._defaults['self_test']['selfTestMessage']
        if sys.version_info.major > 2 and type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(self_test_message) >= len(test_value)
        for i in range(len(test_value)):
            self_test_message[i] = test_value[i]
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niDCPower_Abort.side_effect = MockFunctionCallError("niDCPower_Abort")
        mock_library.niDCPower_Abort.return_value = 0
        mock_library.niDCPower_Commit.side_effect = MockFunctionCallError("niDCPower_Commit")
        mock_library.niDCPower_Commit.return_value = 0
        mock_library.niDCPower_ConfigureApertureTime.side_effect = MockFunctionCallError("niDCPower_ConfigureApertureTime")
        mock_library.niDCPower_ConfigureApertureTime.return_value = 0
        mock_library.niDCPower_ConfigureDigitalEdgeMeasureTrigger.side_effect = MockFunctionCallError("niDCPower_ConfigureDigitalEdgeMeasureTrigger")
        mock_library.niDCPower_ConfigureDigitalEdgeMeasureTrigger.return_value = 0
        mock_library.niDCPower_ConfigureDigitalEdgePulseTrigger.side_effect = MockFunctionCallError("niDCPower_ConfigureDigitalEdgePulseTrigger")
        mock_library.niDCPower_ConfigureDigitalEdgePulseTrigger.return_value = 0
        mock_library.niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger.side_effect = MockFunctionCallError("niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger")
        mock_library.niDCPower_ConfigureDigitalEdgeSequenceAdvanceTrigger.return_value = 0
        mock_library.niDCPower_ConfigureDigitalEdgeSourceTrigger.side_effect = MockFunctionCallError("niDCPower_ConfigureDigitalEdgeSourceTrigger")
        mock_library.niDCPower_ConfigureDigitalEdgeSourceTrigger.return_value = 0
        mock_library.niDCPower_ConfigureDigitalEdgeStartTrigger.side_effect = MockFunctionCallError("niDCPower_ConfigureDigitalEdgeStartTrigger")
        mock_library.niDCPower_ConfigureDigitalEdgeStartTrigger.return_value = 0
        mock_library.niDCPower_CreateAdvancedSequence.side_effect = MockFunctionCallError("niDCPower_CreateAdvancedSequence")
        mock_library.niDCPower_CreateAdvancedSequence.return_value = 0
        mock_library.niDCPower_CreateAdvancedSequenceStep.side_effect = MockFunctionCallError("niDCPower_CreateAdvancedSequenceStep")
        mock_library.niDCPower_CreateAdvancedSequenceStep.return_value = 0
        mock_library.niDCPower_DeleteAdvancedSequence.side_effect = MockFunctionCallError("niDCPower_DeleteAdvancedSequence")
        mock_library.niDCPower_DeleteAdvancedSequence.return_value = 0
        mock_library.niDCPower_Disable.side_effect = MockFunctionCallError("niDCPower_Disable")
        mock_library.niDCPower_Disable.return_value = 0
        mock_library.niDCPower_ExportSignal.side_effect = MockFunctionCallError("niDCPower_ExportSignal")
        mock_library.niDCPower_ExportSignal.return_value = 0
        mock_library.niDCPower_FetchMultiple.side_effect = MockFunctionCallError("niDCPower_FetchMultiple")
        mock_library.niDCPower_FetchMultiple.return_value = 0
        mock_library.niDCPower_GetAttributeViBoolean.side_effect = MockFunctionCallError("niDCPower_GetAttributeViBoolean")
        mock_library.niDCPower_GetAttributeViBoolean.return_value = 0
        mock_library.niDCPower_GetAttributeViInt32.side_effect = MockFunctionCallError("niDCPower_GetAttributeViInt32")
        mock_library.niDCPower_GetAttributeViInt32.return_value = 0
        mock_library.niDCPower_GetAttributeViInt64.side_effect = MockFunctionCallError("niDCPower_GetAttributeViInt64")
        mock_library.niDCPower_GetAttributeViInt64.return_value = 0
        mock_library.niDCPower_GetAttributeViReal64.side_effect = MockFunctionCallError("niDCPower_GetAttributeViReal64")
        mock_library.niDCPower_GetAttributeViReal64.return_value = 0
        mock_library.niDCPower_GetAttributeViString.side_effect = MockFunctionCallError("niDCPower_GetAttributeViString")
        mock_library.niDCPower_GetAttributeViString.return_value = 0
        mock_library.niDCPower_GetChannelName.side_effect = MockFunctionCallError("niDCPower_GetChannelName")
        mock_library.niDCPower_GetChannelName.return_value = 0
        mock_library.niDCPower_GetError.side_effect = MockFunctionCallError("niDCPower_GetError")
        mock_library.niDCPower_GetError.return_value = 0
        mock_library.niDCPower_GetExtCalLastDateAndTime.side_effect = MockFunctionCallError("niDCPower_GetExtCalLastDateAndTime")
        mock_library.niDCPower_GetExtCalLastDateAndTime.return_value = 0
        mock_library.niDCPower_GetExtCalLastTemp.side_effect = MockFunctionCallError("niDCPower_GetExtCalLastTemp")
        mock_library.niDCPower_GetExtCalLastTemp.return_value = 0
        mock_library.niDCPower_GetExtCalRecommendedInterval.side_effect = MockFunctionCallError("niDCPower_GetExtCalRecommendedInterval")
        mock_library.niDCPower_GetExtCalRecommendedInterval.return_value = 0
        mock_library.niDCPower_GetLastExtCalLastDateAndTime.side_effect = MockFunctionCallError("niDCPower_GetLastExtCalLastDateAndTime")
        mock_library.niDCPower_GetLastExtCalLastDateAndTime.return_value = 0
        mock_library.niDCPower_GetLastSelfCalLastDateAndTime.side_effect = MockFunctionCallError("niDCPower_GetLastSelfCalLastDateAndTime")
        mock_library.niDCPower_GetLastSelfCalLastDateAndTime.return_value = 0
        mock_library.niDCPower_GetSelfCalLastDateAndTime.side_effect = MockFunctionCallError("niDCPower_GetSelfCalLastDateAndTime")
        mock_library.niDCPower_GetSelfCalLastDateAndTime.return_value = 0
        mock_library.niDCPower_GetSelfCalLastTemp.side_effect = MockFunctionCallError("niDCPower_GetSelfCalLastTemp")
        mock_library.niDCPower_GetSelfCalLastTemp.return_value = 0
        mock_library.niDCPower_InitializeWithChannels.side_effect = MockFunctionCallError("niDCPower_InitializeWithChannels")
        mock_library.niDCPower_InitializeWithChannels.return_value = 0
        mock_library.niDCPower_Initiate.side_effect = MockFunctionCallError("niDCPower_Initiate")
        mock_library.niDCPower_Initiate.return_value = 0
        mock_library.niDCPower_Measure.side_effect = MockFunctionCallError("niDCPower_Measure")
        mock_library.niDCPower_Measure.return_value = 0
        mock_library.niDCPower_MeasureMultiple.side_effect = MockFunctionCallError("niDCPower_MeasureMultiple")
        mock_library.niDCPower_MeasureMultiple.return_value = 0
        mock_library.niDCPower_ParseChannelCount.side_effect = MockFunctionCallError("niDCPower_ParseChannelCount")
        mock_library.niDCPower_ParseChannelCount.return_value = 0
        mock_library.niDCPower_QueryInCompliance.side_effect = MockFunctionCallError("niDCPower_QueryInCompliance")
        mock_library.niDCPower_QueryInCompliance.return_value = 0
        mock_library.niDCPower_QueryMaxCurrentLimit.side_effect = MockFunctionCallError("niDCPower_QueryMaxCurrentLimit")
        mock_library.niDCPower_QueryMaxCurrentLimit.return_value = 0
        mock_library.niDCPower_QueryMaxVoltageLevel.side_effect = MockFunctionCallError("niDCPower_QueryMaxVoltageLevel")
        mock_library.niDCPower_QueryMaxVoltageLevel.return_value = 0
        mock_library.niDCPower_QueryMinCurrentLimit.side_effect = MockFunctionCallError("niDCPower_QueryMinCurrentLimit")
        mock_library.niDCPower_QueryMinCurrentLimit.return_value = 0
        mock_library.niDCPower_QueryOutputState.side_effect = MockFunctionCallError("niDCPower_QueryOutputState")
        mock_library.niDCPower_QueryOutputState.return_value = 0
        mock_library.niDCPower_ReadCurrentTemperature.side_effect = MockFunctionCallError("niDCPower_ReadCurrentTemperature")
        mock_library.niDCPower_ReadCurrentTemperature.return_value = 0
        mock_library.niDCPower_ResetDevice.side_effect = MockFunctionCallError("niDCPower_ResetDevice")
        mock_library.niDCPower_ResetDevice.return_value = 0
        mock_library.niDCPower_ResetWithDefaults.side_effect = MockFunctionCallError("niDCPower_ResetWithDefaults")
        mock_library.niDCPower_ResetWithDefaults.return_value = 0
        mock_library.niDCPower_SendSoftwareEdgeTrigger.side_effect = MockFunctionCallError("niDCPower_SendSoftwareEdgeTrigger")
        mock_library.niDCPower_SendSoftwareEdgeTrigger.return_value = 0
        mock_library.niDCPower_SetAttributeViBoolean.side_effect = MockFunctionCallError("niDCPower_SetAttributeViBoolean")
        mock_library.niDCPower_SetAttributeViBoolean.return_value = 0
        mock_library.niDCPower_SetAttributeViInt32.side_effect = MockFunctionCallError("niDCPower_SetAttributeViInt32")
        mock_library.niDCPower_SetAttributeViInt32.return_value = 0
        mock_library.niDCPower_SetAttributeViInt64.side_effect = MockFunctionCallError("niDCPower_SetAttributeViInt64")
        mock_library.niDCPower_SetAttributeViInt64.return_value = 0
        mock_library.niDCPower_SetAttributeViReal64.side_effect = MockFunctionCallError("niDCPower_SetAttributeViReal64")
        mock_library.niDCPower_SetAttributeViReal64.return_value = 0
        mock_library.niDCPower_SetAttributeViString.side_effect = MockFunctionCallError("niDCPower_SetAttributeViString")
        mock_library.niDCPower_SetAttributeViString.return_value = 0
        mock_library.niDCPower_SetSequence.side_effect = MockFunctionCallError("niDCPower_SetSequence")
        mock_library.niDCPower_SetSequence.return_value = 0
        mock_library.niDCPower_WaitForEvent.side_effect = MockFunctionCallError("niDCPower_WaitForEvent")
        mock_library.niDCPower_WaitForEvent.return_value = 0
        mock_library.niDCPower_close.side_effect = MockFunctionCallError("niDCPower_close")
        mock_library.niDCPower_close.return_value = 0
        mock_library.niDCPower_error_message.side_effect = MockFunctionCallError("niDCPower_error_message")
        mock_library.niDCPower_error_message.return_value = 0
        mock_library.niDCPower_reset.side_effect = MockFunctionCallError("niDCPower_reset")
        mock_library.niDCPower_reset.return_value = 0
        mock_library.niDCPower_self_test.side_effect = MockFunctionCallError("niDCPower_self_test")
        mock_library.niDCPower_self_test.return_value = 0
