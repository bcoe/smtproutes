import inspect

class SMTPRoute(object):
    
    def __init__(self):
        self._register_routes()
    
    def _register_routes(self):
        self._routes = {}
        
        for attr_name in self.__class__.__dict__:
            if attr_name[0:1] == '_':
                continue
            
            method = getattr(self, attr_name)
            if type(method) == type(self._register_routes):
                default_qwargs = self._extract_default_qwargs(method)
                if default_qwargs.get('route'):
                    self._routes[default_qwargs.get('route')] = method
                
    def _extract_default_qwargs(self, method):
        argspec = inspect.getargspec(method)
        argspec_defaults = list( argspec.defaults )
        default_qwargs = {}
        for arg in argspec.args:
            default_qwargs[arg] = argspec_defaults.pop(0)
        return default_qwargs