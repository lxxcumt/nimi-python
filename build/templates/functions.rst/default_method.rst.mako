<%page args="function, config, method_template, indent"/>\
<%
    import build.helper as helper
%>\
${helper.get_function_rst(function, method_template=method_template, numpy=False, config=config, indent=indent)}
