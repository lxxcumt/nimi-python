# Useful functions for use in the metadata modules

from .documentation_helper import add_notes_re_links
from .documentation_helper import square_up_tables
from .documentation_snippets import options_table_body
from .documentation_snippets import options_table_header
from .documentation_snippets import options_text
from .documentation_snippets import session_return_text
from .helper import camelcase_to_snakecase
from .helper import get_numpy_type_for_api_type
from .helper import get_python_type_for_api_type
from .metadata_filters import filter_codegen_attributes
from .metadata_filters import filter_codegen_functions
from .metadata_find import find_custom_type
from .metadata_find import find_size_parameter
from .metadata_merge_dicts import merge_helper

import codecs
import copy
import os
import pprint

pp = pprint.PrettyPrinter(indent=4, width=80)

# Functions to add information to metadata structures that are specific to our codegen needs.


# These functions can be used by any type, function, attribute or enum


def _add_name(n, name):
    '''Adds a name' key/value pair to the function metadata'''
    assert 'name' not in n, "'name' is already populated which means issue #372 is closed, rendering _add_name() redundant."
    n['name'] = name
    return n


def _add_codegen_method(n):
    '''Add 'codegen_method' as public if it isn't already there'''
    if 'codegen_method' not in n:
        n['codegen_method'] = 'public'


def _add_enum(n):
    '''Add 'enum' as None if it isn't already there'''
    if 'enum' not in n:
        n['enum'] = None


def _add_python_method_name(function, name):
    '''Adds a python_name' key/value pair to the function metadata if not already specified'''
    if 'python_name' not in function:
        if function['codegen_method'] == 'private':
            function['python_name'] = '_' + camelcase_to_snakecase(name)
        else:
            function['python_name'] = camelcase_to_snakecase(name)
    return function


def _add_python_parameter_name(parameter):
    '''Adds a python_name key/value pair to the parameter metadata'''
    if 'python_name' not in parameter:
        parameter['python_name'] = camelcase_to_snakecase(parameter['name'])
    return parameter


def _add_python_type(item, config):
    '''Adds the type to use in the Python API to the item metadata, if not already there'''
    if 'python_type' not in item:
        if item['enum'] is None:
            item['python_type'] = get_python_type_for_api_type(item['type'], config)
        else:
            item['python_type'] = 'enums.' + item['enum']
    return item


def _add_ctypes_variable_name(parameter):
    '''Adds a ctypes_variable_name key/value pair to the parameter metadata for a corresponding ctypes variable'''
    parameter['ctypes_variable_name'] = parameter['python_name'] + '_ctype'
    return parameter


def _add_ctypes_type(parameter, config):
    '''Adds a ctypes_type key/value pair to the parameter metadata for calling into the library'''
    parameter['ctypes_type'] = parameter['type']
    module_name = ''
    custom_type = find_custom_type(parameter, config)
    if custom_type is not None:
        module_name = custom_type['file_name'] + '.'

    if parameter['is_string']:
        parameter['ctypes_type_library_call'] = 'ctypes.POINTER(ViChar)'
    elif parameter['direction'] == 'out' or parameter['is_buffer'] is True:
        parameter['ctypes_type_library_call'] = "ctypes.POINTER(" + module_name + parameter['ctypes_type'] + ")"
    else:
        parameter['ctypes_type_library_call'] = module_name + parameter['ctypes_type']

    return parameter


def _add_numpy_info(parameter, parameters, config):
    '''Adds the following numpy-related information:

             numpy: Default to False unless already set. True for buffers that allow being passed as a numpy.ndarray.
        numpy_type: The name of the element type to use in the numpy.ndarray.
    '''

    if 'numpy' not in parameter:
        parameter['numpy'] = False

    if parameter['numpy']:
        parameter['numpy_type'] = get_numpy_type_for_api_type(parameter['type'], config)

        if parameter['size']['mechanism'] == 'passed-in':
            size_param = find_size_parameter(parameter, parameters)
            if size_param:
                size_param['use_in_python_api'] = False

    return parameter


def _add_is_error_handling(f):
    '''Adds is_error_handling information to the function metadata if it isn't already defined. Defaults to False.'''
    # TODO(marcoskirsch): The information is added in functions_addon.py. I think we can instead infer from method
    # name but I am not sure if it's a good idea (heuristics vs being explicit - both error prone in different ways).
    if 'is_error_handling' not in f:
        # Not populated, assume False
        f['is_error_handling'] = False
    return f


def _add_buffer_info(parameter, config):
    '''Adds buffer information to the parameter metadata

    These are the pieces of information that will be added to metadata:
        'is_string' - Used for any string type - see below for complete list
        'use_list'  - Used for an array of custom types. We are not putting custom types into array.array or numpy.array
        'use_array' - Used for arrays of simple types
        'is_buffer' - True when either 'use_list' or 'use_array' is True
        'size'      - set to default value of {'mechanism': 'fixed', 'value': 1} if it doesn't already exist
    '''

    assert 'is_buffer' not in parameter or not parameter['is_buffer'], "if 'is_buffer' is in metadata then it must be set to False"
    assert 'is_string' not in parameter, "'is_string' should not be set by metadata or in addons"
    assert 'use_list' not in parameter, "'use_list' should not be set by metadata or in addons"

    is_string = False
    use_array = False
    use_list = False
    original_type = parameter['type']

    # We set all string types to ViString, and say it is NOT a buffer/array
    string_types = ['ViConstString', 'ViRsrc', 'ViString', 'ViChar[]', ]
    if original_type in string_types:
        is_string = True
    elif original_type.find('[]') > 0:
        parameter['type'] = original_type.replace('[]', '')  # TODO(marcoskirsch) Don't change metadata, add new key
        parameter['original_type'] = original_type

        if 'use_array' not in parameter or parameter['use_array'] is False:
            use_list = True
        else:
            use_array = True

    # If 'is_buffer' is in the parameter information and False, we also force 'use_list' and 'use_array' to False
    use_list = parameter['is_buffer'] if 'is_buffer' in parameter else use_list
    use_array = parameter['is_buffer'] if 'is_buffer' in parameter else use_array

    # If not populated, assume {'mechanism': 'fixed', 'value': 1}
    parameter['size'] = parameter['size'] if 'size' in parameter else {'mechanism': 'fixed', 'value': 1}

    parameter['use_array'] = parameter['use_array'] if 'use_array' in parameter else use_array
    parameter['use_list'] = parameter['use_list'] if 'use_list' in parameter else use_list
    parameter['is_string'] = parameter['is_string'] if 'is_string' in parameter else is_string
    parameter['is_buffer'] = parameter['is_buffer'] if 'is_buffer' in parameter else (use_array or use_list)

    assert parameter['is_buffer'] is False or parameter['is_string'] is False

    return parameter


def _add_library_method_call_snippet(parameter):
    '''Code snippet for calling a method of Library for this parameter.'''
    if parameter['direction'] == 'out' and not parameter['is_buffer'] and not parameter['is_string']:
        parameter['library_method_call_snippet'] = 'None if {0} is None else (ctypes.pointer({0}))'.format(parameter['ctypes_variable_name'])
    else:
        parameter['library_method_call_snippet'] = parameter['ctypes_variable_name']


def _add_default_value_name(parameter):
    '''Declaration with default value, if set'''
    if 'default_value' in parameter:
        if 'enum' in parameter and parameter['enum'] is not None:
            name_with_default = parameter['python_name'] + "=enums." + parameter['default_value']
        else:
            name_with_default = parameter['python_name'] + "=" + str(parameter['default_value'])

        if 'python_api_converter_name' in parameter:
            name_for_init = '_converters.{0}({1}, self._encoding)'.format(parameter['python_api_converter_name'], parameter['python_name'])
        elif parameter['use_in_python_api']:
            name_for_init = parameter['python_name']
        else:
            name_for_init = parameter['default_value']

    else:
        name_with_default = parameter['python_name']
        name_for_init = parameter['python_name']

    parameter['python_name_with_default'] = name_with_default
    parameter['python_name_or_default_for_init'] = str(name_for_init)


def _add_default_value_name_for_docs(parameter, module_name):
    '''Declaration with default value, if set'''
    if 'default_value' in parameter:
        if 'enum' in parameter and parameter['enum'] is not None:
            name = parameter['python_name'] + "=" + module_name + '.' + parameter['default_value']
        else:
            name = parameter['python_name'] + "=" + repr(parameter['default_value'])

    else:
        name = parameter['python_name']

    parameter['python_name_with_doc_default'] = name


# Parameter names denoting channel/repeated capabilities was compiled by looking at public header files for different MI drivers.
_repeated_capability_parameter_names = ['channelName', 'channelList', 'channel', 'channelNameList', 'channelsString']


def _add_method_templates(f):
    '''Adds a list of 'method_template_filenames' value to function metadata if not found. This are the mako templates that will be used to render the method.'''
    if 'method_templates' not in f:
        f['method_templates'] = [{'session_filename': '/default_method', 'documentation_filename': '/default_method', 'method_python_name_suffix': '', }, ]
    # Prefix the templates with a / so mako can find them. Not sure mako it works this way.
    for method_template in f['method_templates']:
        method_template['session_filename'] = '/' + method_template['session_filename'] if method_template['session_filename'][0] != '/' else method_template['session_filename']
        # Some functions don't get code-generated documentation (i.e. private methods) so no need to specify template for those.
        if 'documentation_filename' in method_template and method_template['documentation_filename'] is not None:
            method_template['documentation_filename'] = '/' + method_template['documentation_filename'] if method_template['documentation_filename'][0] != '/' else method_template['documentation_filename']


def _add_has_repeated_capability(f):
    '''Adds a boolean 'has_repeated_capability' to the function metadata by inferring it from its parameter names, if not previously populated.'''
    if 'has_repeated_capability' not in f:
        f['has_repeated_capability'] = False
        for p in f['parameters']:
            f['has_repeated_capability'] = f['has_repeated_capability'] or p['name'] in _repeated_capability_parameter_names


def _add_render_in_session_base(f):
    '''Adds a boolean 'render_in_session_base' to the function metadata if not previously populated.

    This tells the code generator to render those methods in _SessionBase class and not Session.
    By default, we want all functions that have repeated capability input and all error handling related functions in _SessionBase but there are exceptions to this rule.
    '''
    if 'render_in_session_base' not in f:
        f['render_in_session_base'] = f['has_repeated_capability'] or f['is_error_handling']


def _add_is_repeated_capability(parameter):
    '''Adds a boolean 'is_repeated_capability' to the parameter metadata by inferring it from its name, if not previously populated.'''
    if 'is_repeated_capability' not in parameter:
        parameter['is_repeated_capability'] = parameter['name'] in _repeated_capability_parameter_names


def _add_is_session_handle(parameter):
    '''Adds a boolean 'is_session_handle' to the parameter metadata by inferring it from its type, if not previously populated.'''
    if 'is_session_handle' not in parameter:
        parameter['is_session_handle'] = parameter['type'] == 'ViSession' and parameter['direction'] == 'in'


def _fix_type(parameter):
    '''Replace any spaces in the parameter type with an underscore.'''
    parameter['type'] = parameter['type'].replace('[ ]', '[]').replace(' ', '_')


def _add_use_in_python_api(p, parameters):
    '''Add 'use_in_python_api' if not there with value of True'''
    if 'use_in_python_api' not in p:
        p['use_in_python_api'] = True

    if p['size']['mechanism'] == 'len' or p['size']['mechanism'] == 'ivi-dance':
        size_param = find_size_parameter(p, parameters)
        size_param['use_in_python_api'] = False


def _setup_init_function(functions, config):
    '''Copy the selected init function to a known name and update information about it for documentation purposes'''
    try:
        init_function = copy.deepcopy(functions[config['init_function']])
        init_function['codegen_method'] = 'no'

        # Change the init_function information for generating the docstring
        # We are assuming the last parameter is vi out
        for p in init_function['parameters']:
            if p['name'] == 'vi':
                p['documentation']['description'] = session_return_text
                p['python_type'] = config['module_name'] + '.Session'
                p['python_name'] = 'session'
            elif p['python_name'] == 'option_string':
                p['python_name'] = 'options'
                p['python_name_with_default'] = 'options={}'
                p['documentation']['description'] = options_text
                p['documentation']['table_header'] = options_table_header
                p['documentation']['table_body'] = options_table_body
                # Additional options documentation may be added in metadata __init__ if it is driver specific

        functions['_init_function'] = init_function
    except KeyError:
        pass


def add_all_function_metadata(functions, config):
    '''Merges and Adds all codegen-specific metada to the function metadata list'''
    functions = merge_helper(functions, 'functions', config, use_re=True)

    for f in functions:
        _add_codegen_method(functions[f])

    for f in filter_codegen_functions(functions):
        _add_name(functions[f], f)
        _add_python_method_name(functions[f], f)
        _add_is_error_handling(functions[f])
        _add_has_repeated_capability(functions[f])
        _add_render_in_session_base(functions[f])
        _add_method_templates(functions[f])
        for p in functions[f]['parameters']:
            _add_enum(p)
            _fix_type(p)
            _add_buffer_info(p, config)
            _add_use_in_python_api(p, functions[f]['parameters'])
            _add_python_parameter_name(p)
            _add_python_type(p, config)
            _add_ctypes_variable_name(p)
            _add_ctypes_type(p, config)
            _add_numpy_info(p, functions[f]['parameters'], config)
            _add_default_value_name(p)
            _add_default_value_name_for_docs(p, config['module_name'])
            _add_is_repeated_capability(p)
            _add_is_session_handle(p)
            _add_library_method_call_snippet(p)

    _setup_init_function(functions, config)

    return functions


def _add_python_name(a, attributes):
    '''Adds 'python_name' - lower case + leading '_' if first character is a digit'''
    n = attributes[a]['name'].lower()
    if attributes[a]['name'][0].isdigit():
        n = '_' + n
    attributes[a]['python_name'] = n


def _add_default_attribute_class(a, attributes):
    '''Set 'attribute_class' if not set.

    By default, the 'attribute_class' is only based on the 'type'.
    It can be set in attributes_addon if we want to convert to/from a different datatype, such as datetime.timedelta
    '''
    if 'attribute_class' not in attributes[a]:
        attributes[a]['attribute_class'] = 'Attribute' + attributes[a]['type']


def add_all_attribute_metadata(attributes, config):
    '''Merges and Adds all codegen-specific metada to the function metadata list'''
    attributes = merge_helper(attributes, 'attributes', config, use_re=False)

    for a in attributes:
        _add_codegen_method(attributes[a])
        _add_enum(attributes[a])
        _add_python_name(a, attributes)
        _add_python_type(attributes[a], config)
        _add_default_attribute_class(a, attributes)

    return attributes


def _add_enum_codegen_method(enums, config):
    '''Adds 'codegen_method' that will determine whether and how the enum is code genned. Default is public

    Set all to 'no', then go through all functions and attributes and set to least restrictive use
    '''
    for e in enums:
        if 'codegen_method' not in enums[e]:
            enums[e]['codegen_method'] = 'no'

    # Iterate through all codegen functions and set any enum parameters to the same level
    for f in filter_codegen_functions(config['functions']):
        f_codegen_method = config['functions'][f]['codegen_method']
        if f_codegen_method != 'no':
            for p in config['functions'][f]['parameters']:
                e = p['enum']
                if e is not None and e not in enums:
                    print('Missing enum {0} referenced by function {1}'.format(e, f))
                elif e is not None:
                    if f_codegen_method == 'private' and enums[e]['codegen_method'] == 'no':
                        enums[e]['codegen_method'] = f_codegen_method
                    elif f_codegen_method == 'public':
                        enums[e]['codegen_method'] = f_codegen_method

    # Iterate through all codegen attributes and set any enum parameters to the same level
    for a in filter_codegen_attributes(config['attributes']):
        a_codegen_method = config['attributes'][a]['codegen_method']
        if a_codegen_method != 'no':
            e = config['attributes'][a]['enum']
            if e is not None and e not in enums:
                print('Missing enum {0} referenced by attribute {1}'.format(e, a['name']))
            elif e is not None:
                if a_codegen_method == 'private' and enums[e]['codegen_method'] == 'no':
                    enums[e]['codegen_method'] = a_codegen_method
                elif a_codegen_method == 'public':
                    enums[e]['codegen_method'] = a_codegen_method


def _add_enum_value_python_name(enum_info, config):
    '''Add 'python_name' for all values, removing any common prefixes and suffixes'''
    for v in enum_info['values']:
        v['python_name'] = v['name'].replace('{0}_VAL_'.format(config['module_name'].upper()), '')

    # We are using an os.path function do find any common prefix. So that we don't
    # get 'O' in 'ON' and 'OFF' we remove characters at the end until they are '_'
    names = [v['python_name'] for v in enum_info['values']]
    prefix = os.path.commonprefix(names)
    while len(prefix) > 0 and prefix[-1] != '_':
        prefix = prefix[:-1]

    # If the prefix is in the whitelist, we don't want to remove it so set to empty string
    if 'enum_whitelist_prefix' in config and prefix in config['enum_whitelist_prefix']:
        prefix = ''

    # We only remove the prefix if there is one and it isn't '_'.
    # '_' only means the name starts with a number
    if len(prefix) > 0 and prefix != '_':
        for v in enum_info['values']:
            assert v['python_name'].startswith(prefix), '{0} does not start with {1}'.format(v['name'], prefix)
            v['prefix'] = prefix
            v['python_name'] = v['python_name'].replace(prefix, '')

    # Now we need to look for common suffixes
    # Using the slow method of reversing a string for readability
    rev_names = [''.join(reversed(v['python_name'])) for v in enum_info['values']]
    suffix = os.path.commonprefix(rev_names)
    while len(suffix) > 0 and suffix[-1] != '_':
        suffix = suffix[:-1]

    # Unreverse the suffix
    suffix = ''.join(reversed(suffix))

    # If the suffix is in the whitelist, we don't want to remove it so set to empty string
    if 'enum_whitelist_suffix' in config and suffix in config['enum_whitelist_suffix']:
        suffix = ''

    # We only remove the suffix if there is one.
    # '_' only means the name starts with a number
    if len(suffix) > 0:
        for v in enum_info['values']:
            assert v['python_name'].endswith(suffix), '{0} does not end with {1}'.format(v['name'], suffix)
            v['suffix'] = suffix
            v['python_name'] = v['python_name'].replace(suffix, '')

    # We need to check again to see if we need a leading '_' due to the first character of the name being a number
    for v in enum_info['values']:
        if v['python_name'][0].isdigit():
            v['python_name'] = '_' + v['python_name']

    return enum_info


def add_all_enum_metadata(enums, config):
    '''Merges and Adds all codegen-specific metada to the function metadata list'''
    enums = merge_helper(enums, 'enums', config, use_re=False)

    # Workaround for NI Internal CAR #675174
    try:
        replacement_enums = config['modules']['metadata.enums_addon'].__getattribute__('replacement_enums')
        for e in replacement_enums:
            enums[e] = replacement_enums[e]
    except AttributeError:
        pass

    _add_enum_codegen_method(enums, config)
    for e in enums:
        enums[e] = _add_enum_value_python_name(enums[e], config)
        enums[e]['python_name'] = enums[e]['python_name'] if 'python_name' in enums[e] else e

    return enums


def add_all_metadata(functions, attributes, enums, config):
    '''merge and add all additional metadata_dir

    Updates all parameters
        functions, attributes, enums - addon data merged, additional metadata
        config - functions, attributes, enums added
    '''
    functions = add_all_function_metadata(functions, config)
    config['functions'] = functions

    attributes = add_all_attribute_metadata(attributes, config)
    config['attributes'] = attributes

    enums = add_all_enum_metadata(enums, config)
    config['enums'] = enums

    add_notes_re_links(config)

    square_up_tables(config)

    pp_persist = pprint.PrettyPrinter(indent=4, width=200)
    metadata_dir = os.path.join('bin', 'processed_metadata')
    if not os.path.exists(metadata_dir):
        os.makedirs(metadata_dir)

    with codecs.open(os.path.join(metadata_dir, config['module_name'] + '_functions.py'), "w", "utf-8") as text_file:
        text_file.write("function =\n{0}".format(pp_persist.pformat(functions)))

    with codecs.open(os.path.join(metadata_dir, config['module_name'] + '_attributes.py'), "w", "utf-8") as text_file:
        text_file.write("attributes =\n{0}".format(pp_persist.pformat(attributes)))

    with codecs.open(os.path.join(metadata_dir, config['module_name'] + '_enums.py'), "w", "utf-8") as text_file:
        text_file.write("enums =\n{0}".format(pp_persist.pformat(enums)))


# Unit Tests
def _compare_values(actual, expected, k):
    if type(actual) is dict:
        _compare_dicts(actual, expected)
    elif type(actual) is list:
        _compare_lists(actual, expected)
    else:
        assert actual == expected, "Value mismatch with key/index '{0}', {1} != {2}".format(k, actual, expected)


def _compare_lists(actual, expected):
    assert type(actual) == type(expected), 'Type mismatch, {0} != {1}'.format(type(actual), type(expected))
    assert len(actual) == len(expected), 'Length mismatch, {0} != {1}'.format(len(actual), len(expected))
    for k in range(len(actual)):
        _compare_values(actual[k], expected[k], k)


def _compare_dicts(actual, expected):
    assert type(actual) == type(expected), 'Type mismatch, {0} != {1}'.format(type(actual), type(expected))
    for k in actual:
        assert k in expected, 'Key {0} not in expected'.format(k)
        _compare_values(actual[k], expected[k], k)
    for k in expected:
        assert k in actual, 'Key {0} not in actual'.format(k)


config_for_testing = {
    'session_handle_parameter_name': 'vi',
    'module_name': 'nifake',
    'functions': {},
    'attributes': {},
    'modules': {
        'metadata.enums_addon': {}
    },
    'custom_types': [],
    'init_function': None,
}


def _do_the_test_add_all_metadata(functions, expected):
    actual = copy.deepcopy(functions)
    actual = add_all_function_metadata(actual, config_for_testing)
    _compare_dicts(actual, expected)


def test_add_all_metadata_simple():
    functions = {
        'MakeAFoo': {
            'codegen_method': 'public',
            'returns': 'ViStatus',
            'method_templates': [{'session_filename': '/cool_template', 'documentation_filename': '/cool_template', 'method_python_name_suffix': '', }, ],
            'parameters': [
                {
                    'direction': 'in',
                    'enum': None,
                    'name': 'vi',
                    'type': 'ViSession',
                    'documentation': {
                        'description': 'Identifies a particular instrument session.',
                    },
                },
                {
                    'direction': 'in',
                    'enum': None,
                    'name': 'channelName',
                    'type': 'ViString',
                    'documentation': {
                        'description': 'The channel to call this on.',
                    },
                },
            ],
            'documentation': {
                'description': 'Performs a foo, and performs it well.',
            },
        },
        'MakeAPrivateMethod': {
            'codegen_method': 'private',
            'returns': 'ViStatus',
            'parameters': [
                {
                    'direction': 'in',
                    'enum': None,
                    'name': 'vi',
                    'type': 'ViSession',
                    'documentation': {
                        'description': 'Identifies a particular instrument session.',
                    },
                },
                {
                    'direction': 'out',
                    'enum': None,
                    'name': 'status',
                    'type': 'ViString',
                    'documentation': {
                        'description': 'Return a device status',
                    },
                }
            ],
            'documentation': {
                'description': 'Perform actions as method defined',
            },
        },
    }
    expected = {
        'MakeAFoo': {
            'name': 'MakeAFoo',
            'codegen_method': 'public',
            'documentation': {
                'description': 'Performs a foo, and performs it well.'
            },
            'has_repeated_capability': True,
            'is_error_handling': False,
            'render_in_session_base': True,
            'method_templates': [{'session_filename': '/cool_template', 'documentation_filename': '/cool_template', 'method_python_name_suffix': '', }, ],
            'parameters': [
                {
                    'ctypes_type': 'ViSession',
                    'ctypes_variable_name': 'vi_ctype',
                    'ctypes_type_library_call': 'ViSession',
                    'direction': 'in',
                    'documentation': {
                        'description': 'Identifies a particular instrument session.'
                    },
                    'is_repeated_capability': False,
                    'is_session_handle': True,
                    'enum': None,
                    'numpy': False,
                    'python_type': 'int',
                    'use_array': False,
                    'is_buffer': False,
                    'use_list': False,
                    'is_string': False,
                    'name': 'vi',
                    'python_name': 'vi',
                    'python_name_with_default': 'vi',
                    'python_name_with_doc_default': 'vi',
                    'size': {
                        'mechanism': 'fixed',
                        'value': 1
                    },
                    'type': 'ViSession',
                    'library_method_call_snippet': 'vi_ctype',
                    'use_in_python_api': True,
                    'python_name_or_default_for_init': 'vi',
                },
                {
                    'ctypes_type': 'ViString',
                    'ctypes_variable_name': 'channel_name_ctype',
                    'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
                    'direction': 'in',
                    'documentation': {
                        'description': 'The channel to call this on.'
                    },
                    'is_repeated_capability': True,
                    'is_session_handle': False,
                    'enum': None,
                    'numpy': False,
                    'python_type': 'str',
                    'use_array': False,
                    'is_buffer': False,
                    'use_list': False,
                    'is_string': True,
                    'name': 'channelName',
                    'python_name': 'channel_name',
                    'python_name_with_default': 'channel_name',
                    'python_name_with_doc_default': 'channel_name',
                    'size': {'mechanism': 'fixed', 'value': 1},
                    'type': 'ViString',
                    'library_method_call_snippet': 'channel_name_ctype',
                    'use_in_python_api': True,
                    'python_name_or_default_for_init': 'channel_name',
                },
            ],
            'python_name': 'make_a_foo',
            'returns': 'ViStatus',
        },
        'MakeAPrivateMethod': {
            'codegen_method': 'private',
            'returns': 'ViStatus',
            'method_templates': [{'session_filename': '/default_method', 'documentation_filename': '/default_method', 'method_python_name_suffix': '', }, ],
            'parameters': [{
                'direction': 'in',
                'enum': None,
                'numpy': False,
                'name': 'vi',
                'type': 'ViSession',
                'documentation': {
                    'description': 'Identifies a particular instrument session.'
                },
                'python_name': 'vi',
                'python_type': 'int',
                'ctypes_variable_name': 'vi_ctype',
                'ctypes_type': 'ViSession',
                'ctypes_type_library_call': 'ViSession',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': False,
                'python_name_with_default': 'vi',
                'python_name_with_doc_default': 'vi',
                'is_repeated_capability': False,
                'is_session_handle': True,
                'library_method_call_snippet': 'vi_ctype',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'vi',
            }, {
                'direction': 'out',
                'enum': None,
                'numpy': False,
                'name': 'status',
                'type': 'ViString',
                'documentation': {
                    'description': 'Return a device status'
                },
                'python_name': 'status',
                'python_type': 'str',
                'ctypes_variable_name': 'status_ctype',
                'ctypes_type': 'ViString',
                'ctypes_type_library_call': 'ctypes.POINTER(ViChar)',
                'size': {
                    'mechanism': 'fixed',
                    'value': 1
                },
                'use_array': False,
                'is_buffer': False,
                'use_list': False,
                'is_string': True,
                'python_name_with_default': 'status',
                'python_name_with_doc_default': 'status',
                'is_repeated_capability': False,
                'is_session_handle': False,
                'library_method_call_snippet': 'status_ctype',
                'use_in_python_api': True,
                'python_name_or_default_for_init': 'status',
            }],
            'documentation': {
                'description': 'Perform actions as method defined'
            },
            'name': 'MakeAPrivateMethod',
            'python_name': '_make_a_private_method',
            'is_error_handling': False,
            'render_in_session_base': False,
            'has_repeated_capability': False
        }
    }

    _do_the_test_add_all_metadata(functions=functions, expected=expected)


def _do_the_test_add_attributes_metadata(attributes, expected):
    actual = copy.deepcopy(attributes)
    actual = add_all_attribute_metadata(actual, config_for_testing)
    _compare_dicts(actual, expected)


def test_add_attributes_metadata_simple():
    attributes = {
        1000000: {
            'access': 'read-write',
            'channel_based': 'False',
            'enum': None,
            'lv_property': 'Fake attributes:Read Write Bool',
            'name': 'READ_WRITE_BOOL',
            'resettable': 'No',
            'type': 'ViBoolean',
            'documentation': {
                'description': 'An attribute of type bool with read/write access.',
            },
        },
    }
    expected = {
        1000000: {
            'access': 'read-write',
            'channel_based': 'False',
            'codegen_method': 'public',
            'documentation': {'description': 'An attribute of type bool with read/write access.'},
            'enum': None,
            'lv_property': 'Fake attributes:Read Write Bool',
            'name': 'READ_WRITE_BOOL',
            'python_name': 'read_write_bool',
            'resettable': 'No',
            'type': 'ViBoolean',
            'python_type': 'bool',
            'attribute_class': 'AttributeViBoolean',
        },
    }

    _do_the_test_add_attributes_metadata(attributes, expected)


def _do_the_test_add_enums_metadata(enums, expected):
    actual = copy.deepcopy(enums)
    actual = add_all_enum_metadata(actual, config_for_testing)
    _compare_dicts(actual, expected)


def test_add_enums_metadata_simple():
    enums = {
        'Color': {
            'values': [
                {
                    'name': 'RED',
                    'value': 1,
                    'documentation': {
                        'description': 'Like blood.',
                    }
                },
                {
                    'name': 'BLUE',
                    'value': 2,
                    'documentation': {
                        'description': 'Like the sky.',
                    }
                },
                {
                    'name': 'YELLOW',
                    'value': 2,
                    'documentation': {
                        'description': 'Like a banana.',
                    }
                },
                {
                    'name': 'BLACK',
                    'value': 2,
                    'documentation': {
                        'description': 'Like this developer\'s conscience.',
                    }
                },
            ],
        },
    }
    expected = {
        'Color': {
            'codegen_method': 'no',
            'python_name': 'Color',
            'values': [
                {'documentation': {'description': 'Like blood.'}, 'name': 'RED', 'value': 1, 'python_name': 'RED'},
                {'documentation': {'description': 'Like the sky.'}, 'name': 'BLUE', 'value': 2, 'python_name': 'BLUE'},
                {'documentation': {'description': 'Like a banana.'}, 'name': 'YELLOW', 'value': 2, 'python_name': 'YELLOW'},
                {'documentation': {'description': "Like this developer's conscience."}, 'name': 'BLACK', 'value': 2, 'python_name': 'BLACK'}
            ]
        },
    }

    _do_the_test_add_enums_metadata(enums, expected)


