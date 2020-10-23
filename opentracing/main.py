



# Access to the active span is straightforward.
from opentracing import tracer
scope=tracer.scope_manager.active()
if scope is not None:
    scope.span.set_tag('...','...')
