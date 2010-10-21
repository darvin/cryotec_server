from django.shortcuts import render_to_response
from django.template import RequestContext

def render_to(tmpl):
    def renderer(func):
        def wrapper(request, *args, **kw):
            output = func(request, *args, **kw)
            if not isinstance(output, dict):
                return output
            return render_to_response(tmpl, output,
                                      context_instance=RequestContext(request))
        return wrapper
    return renderer

