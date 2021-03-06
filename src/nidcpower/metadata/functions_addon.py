# These dictionaries are merged with the extracted function metadata at build time.
# Changes to the metadata should be made here, because functions.py is generated thus any changes get overwritten.

# By default all functions in functions.py are "public".
# This will override that with private (prefixes name with '_'), or don't generate at all
functions_codegen_method = {
    'InitializeWithChannels':          { 'codegen_method': 'private',  },
    'InitWithOptions':                 { 'codegen_method': 'no',       },
    'Initiate':                        { 'codegen_method': 'private',  },
    'close':                           { 'codegen_method': 'private',  },
    '.etAttribute.+':                  { 'codegen_method': 'private',  },  # All Set/Get Attribute functions are private
    'init':                            { 'codegen_method': 'no',       },
    'error_message':                   { 'codegen_method': 'private',  },
    'GetError':                        { 'codegen_method': 'private',  },
    'ClearError':                      { 'codegen_method': 'no',       },
    'LockSession':                     { 'codegen_method': 'no',       },
    'UnlockSession':                   { 'codegen_method': 'no',       },
    'ChangeExtCalPassword':            { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'CloseExtCal':                     { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'InitExtCal':                      { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'CalAdjust.+':                     { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'CalSelfCalibrate':                { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    'ConnectInternalReference':        { 'codegen_method': 'no',       },  # External Calibration is not supported by the Python API
    '.+UserDefined.+':                 { 'codegen_method': 'no',       },
    'SetAttributeViSession':           { 'codegen_method': 'no',       },
    'GetAttributeViSession':           { 'codegen_method': 'no',       },
    'GetNextInterchangeWarning':       { 'codegen_method': 'no',       },  # Not applicable to Python API
    'ResetInterchangeCheck':           { 'codegen_method': 'no',       },  # Not applicable to Python API
    'ClearInterchangeWarnings':        { 'codegen_method': 'no',       },  # Not applicable to Python API
    'GetNextCoercionRecord':           { 'codegen_method': 'no',       },  # Not applicable to Python API
    'error_query':                     { 'codegen_method': 'no',       },
    'ConfigureAutoZero':               { 'codegen_method': 'no',       },
    'ConfigureCurrent.+':              { 'codegen_method': 'no',       },
    'ConfigureOutput.+':               { 'codegen_method': 'no',       },
    'ConfigurePowerLineFrequency':     { 'codegen_method': 'no',       },
    'ConfigurePulse.+':                { 'codegen_method': 'no',       },
    'ConfigureSense':                  { 'codegen_method': 'no',       },
    'ConfigureVoltageL.+':             { 'codegen_method': 'no',       },
    'ConfigureSourceMode':             { 'codegen_method': 'no',       },
    'ConfigureSoftwareEdge.+Trigger':  { 'codegen_method': 'no',       },
    'Disable.+Trigger':                { 'codegen_method': 'no',       },
    'revision_query':                  { 'codegen_method': 'no',       },
    'GetExtCalLastDateAndTime':        { 'codegen_method': 'private',  },  # Public wrapper to allow datetime
    'GetSelfCalLastDateAndTime':       { 'codegen_method': 'private',  },  # Public wrapper to allow datetime
}

# Attach the given parameter to the given enum from enums.py
functions_enums = {
    'ConfigureAutoZero':                            { 'parameters': { 2: { 'enum': 'AutoZero',                    }, }, },
    'ConfigureApertureTime':                        { 'parameters': { 3: { 'enum': 'ApertureTimeUnits',           }, }, },
    'ConfigureDigitalEdgeMeasureTrigger':           { 'parameters': { 2: { 'enum': 'DigitalEdge',                 }, }, },
    'ConfigureDigitalEdgePulseTrigger':             { 'parameters': { 2: { 'enum': 'DigitalEdge',                 }, }, },
    'ConfigureDigitalEdgeSequenceAdvanceTrigger':   { 'parameters': { 2: { 'enum': 'DigitalEdge',                 }, }, },
    'ConfigureDigitalEdgeSourceTrigger':            { 'parameters': { 2: { 'enum': 'DigitalEdge',                 }, }, },
    'ConfigureDigitalEdgeStartTrigger':             { 'parameters': { 2: { 'enum': 'DigitalEdge',                 }, }, },
    'SendSoftwareEdgeTrigger':                      { 'parameters': { 1: { 'enum': 'SendSoftwareEdgeTriggerType', }, }, },
    'WaitForEvent':                                 { 'parameters': { 1: { 'enum': 'Event',                       }, }, },
    'Measure':                                      { 'parameters': { 2: { 'enum': 'MeasurementTypes',            }, }, },
    'QueryOutputState':                             { 'parameters': { 2: { 'enum': 'OutputStates',                }, }, },
    'ExportSignal':                                 { 'parameters': { 1: { 'enum': 'ExportSignal',                }, }, },
	# @TODO add all enums
}

# This is the additional metadata needed by the code generator in order create code that can properly handle buffer allocation.
functions_buffer_info = {
    'GetError':                     { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'BufferSize'}, }, }, },
    'self_test':                    { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'GetAttributeViString':         { 'parameters': { 4: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'GetCalUserDefinedInfo':        { 'parameters': { 1: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From LabVIEW VI, even though niDMM_GetCalUserDefinedInfoMaxSize() exists.
    'error_message':                { 'parameters': { 2: { 'size': {'mechanism':'fixed', 'value':256}, }, }, }, # From documentation
    'GetChannelName':               { 'parameters': { 3: { 'size': {'mechanism':'ivi-dance', 'value':'bufferSize'}, }, }, },
    'SetSequence':                  { 'parameters': { 2: { 'size': {'mechanism':'len', 'value':'Size'}, }, }, },
    'CreateAdvancedSequence':       { 'parameters': { 3: { 'size': {'mechanism':'len', 'value':'attributeIdCount'}, }, }, },
    'FetchMultiple':                { 'parameters': { 4: { 'size': {'mechanism':'passed-in', 'value':'Count'}, },
                                                      5: { 'size': {'mechanism':'passed-in', 'value':'Count'}, },
                                                      6: { 'size': {'mechanism':'passed-in', 'value':'Count'}, }, }, },
    'MeasureMultiple':              { 'parameters': { 2: { 'size': {'mechanism':'python-code', 'value':'self._parse_channel_count()'}, },
                                                      3: { 'size': {'mechanism':'python-code', 'value':'self._parse_channel_count()'}, }, }, }
}

# These are functions we mark as "error_handling":True. The generator uses this information to
# change how error handling is done within those functions themselves - basically, if an error occurs,
# dont try to handle it, since the functions are only used within the context of error handling.
functions_is_error_handling = {
    'error_message':                { 'is_error_handling': True },
    'GetError':                     { 'is_error_handling': True },
}

# There are some parameters that are needed in the C function call we use under the hood, but that we do not want in the Python API
functions_remove_from_python_api = {
    'FetchMultiple':                { 'parameters': { 7: { 'use_in_python_api': False, }, }, },
}

# Default values for method parameters
functions_default_value = {
    'InitializeWithChannels':                        { 'parameters': { 1: { 'default_value': '""', },
                                                                       2: { 'default_value': False, },
                                                                       3: { 'default_value': '""', }, }, },
    'ConfigureApertureTime':                         { 'parameters': { 3: { 'default_value': 'ApertureTimeUnits.SECONDS', }, }, },
    'SetSequence':                                   { 'parameters': { 2: { 'default_value': None, }, }, },
    'ConfigureDigitalEdgeMeasureTrigger':            { 'parameters': { 2: { 'default_value': 'DigitalEdge.RISING', }, }, },
    'ConfigureDigitalEdgePulseTrigger':              { 'parameters': { 2: { 'default_value': 'DigitalEdge.RISING', }, }, },
    'ConfigureDigitalEdgeSequenceAdvanceTrigger':    { 'parameters': { 2: { 'default_value': 'DigitalEdge.RISING', }, }, },
    'ConfigureDigitalEdgeSourceTrigger':             { 'parameters': { 2: { 'default_value': 'DigitalEdge.RISING', }, }, },
    'ConfigureDigitalEdgeStartTrigger':              { 'parameters': { 2: { 'default_value': 'DigitalEdge.RISING', }, }, },
    'CreateAdvancedSequence':                        { 'parameters': { 4: { 'default_value': True, }, }, },
    'CreateAdvancedSequenceStep':                    { 'parameters': { 1: { 'default_value': True, }, }, },
    'ExportSignal':                                  { 'parameters': { 2: { 'default_value': '""', }, }, },
    'SendSoftwareEdgeTrigger':                       { 'parameters': { 1: { 'default_value': 'SendSoftwareEdgeTriggerType.START', }, }, },
    'WaitForEvent':                                  { 'parameters': { 2: { 'default_value': 'datetime.timedelta(seconds=10.0)', },}, },
    'FetchMultiple':                                 { 'parameters': { 1: { 'default_value': 1.0, },
                                                                       2: { 'default_value': 'datetime.timedelta(seconds=1.0)', }, }, },
}

# Parameter that need to be array.array
functions_array = {
    'FetchMultiple':                        { 'parameters': { 4: { 'use_array': True, }, 
                                                              5: { 'use_array': True, }, }, },
}

# Functions not in original metadata.
functions_additional_functions = {
    # What is this function? I've never seen it in niDCPower.h!
    # It's a secret, undocumented NI-DCPower function and the key to the Python API figuring out how many points to return from nidcpower.Session.measure_multiple.
    # Don't tell anyone about it, and don't ever use it directly in your programs. Thank you.
    'ParseChannelCount': {
        'codegen_method': 'private',
        'returns': 'ViStatus',
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
            },
            {
                'direction': 'in',
                'name': 'channelsString',
                'type': 'ViConstString',
            },
            {
                'direction': 'out',
                'name': 'numberOfChannels',
                'type': 'ViUInt32',
            },
        ],
        'documentation': {
            'description': 'Returns the number of channels.',
        },
    },
    # Public function that wraps driver function but returns datetime object instead of individual items
    'GetLastExtCalLastDateAndTime': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'python_name': 'get_ext_cal_last_date_and_time',
        'real_datetime_call': 'GetExtCalLastDateAndTime',
        'method_templates': [
            { 'session_filename': 'datetime_wrappers', 'documentation_filename': 'default_method', 'method_python_name_suffix': '', },
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session. **vi** is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.',
                },
            },
            {
                'direction': 'out',
                'name': 'Month',
                'type': 'datetime.datetime',
                'documentation': {
                    'description': 'Indicates date and time of the last calibration.',
                },
            },
        ],
        'documentation': {
            'description': 'Returns the date and time of the last successful calibration.',
        },
    },
    'GetLastSelfCalLastDateAndTime': {
        'codegen_method': 'public',
        'returns': 'ViStatus',
        'python_name': 'get_self_cal_last_date_and_time',
        'real_datetime_call': 'GetSelfCalLastDateAndTime',
        'method_templates': [
            { 'session_filename': 'datetime_wrappers', 'documentation_filename': 'default_method', 'method_python_name_suffix': '', },
        ],
        'parameters': [
            {
                'direction': 'in',
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session. **vi** is obtained from the niDCPower_InitExtCal or niDCPower_InitializeWithChannels function.',
                },
            },
            {
                'direction': 'out',
                'name': 'Month',
                'type': 'datetime.datetime',
                'documentation': {
                    'description': 'Returns the date and time the device was last calibrated.',
                },
            },
        ],
        'documentation': 
        {
            'description': 'Returns the date and time of the oldest successful self-calibration from among the channels in the session.',
            'note': 'This function is not supported on all devices.',
        },
    },
}

# Converted parameters
functions_converters = {
    'FetchMultiple':                    { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds', 
                                                               'python_type': 'datetime.timedelta', }, }, },
    'WaitForEvent':                     { 'parameters': { 2: { 'python_api_converter_name': 'convert_timedelta_to_seconds', 
                                                               'python_type': 'datetime.timedelta', }, }, },
    'InitializeWithChannels':           { 'parameters': { 3: { 'python_api_converter_name': 'convert_init_with_options_dictionary', 
                                                               'python_type': 'dict', }, }, },
}


