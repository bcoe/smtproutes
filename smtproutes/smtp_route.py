import re, email, inspect
from contact import Contact
from routing_exception import RoutingException

class SMTPRoute(object):
    
    def __init__(self):
        self._register_routes()
        
    def route(self, mailfrom=None, message_data=None):
        self.message = email.message_from_string(message_data)
        self.mailfrom = Contact(mailfrom)
        self.tos = Contact.create_contacts_from_message_field('to', self.message)
        self.ccs = Contact.create_contacts_from_message_field('cc', self.message)
        self.bccs = Contact.create_contacts_from_message_field('bcc', self.message)
        self._call_routes()
    
    def _call_routes(self):
        route_found = False
        for to in self.tos:
            for route in self._routes.keys():
                if re.match(route, to.email):
                    route_found = True
                    self._routes[route]()
        
        if not route_found:
            raise RoutingException(self.message)
            
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
            if arg == 'self':
                continue
                
            default_qwargs[arg] = argspec_defaults.pop(0)
        return default_qwargs