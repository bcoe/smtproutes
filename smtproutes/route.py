import smtproutes
import re, email, inspect, logging

from model import Contact, Message
from routing_exception import RoutingException
from sender_auth import SenderAuthException

class Route(object):
    
    def _initialize(self, peer_ip='0.0.0.0'):
        self._peer_ip = peer_ip
        self.logger = logging.getLogger( smtproutes.LOG_NAME )
        self._register_routes()
    
    def _route(self, message_data=None):
        self.raw_message_data = message_data
        self.message = email.message_from_string(message_data, Message)
        self.mailfrom = Contact.create_contacts_from_message_field('from', self.message)[0]
        self.tos = Contact.create_contacts_from_message_field('to', self.message)
        self.ccs = Contact.create_contacts_from_message_field('cc', self.message)
        self.bccs = Contact.create_contacts_from_message_field('bcc', self.message)
        self._call_routes()
    
    def _call_routes(self):
        route_found = False
        
        recipients = []
        recipients.extend(self.tos)
        recipients.extend(self.ccs)
        recipients.extend(self.bccs)
        
        for recipient in recipients:
            for route in self._routes.keys():
                if re.match(route, recipient.email):
                    self.logger.info('Route %s matched email %s' % (route, recipient.email))
                    route_found = True
                    self._auth_sender(route)
                    self._populate_instance_variables_from_named_capture_groups(route, recipient.email)
                    self._routes[route]['method']()
        
        if not route_found:
            raise RoutingException('No matching route found for %s.' % ', '.join(str(r) for r in recipients) )
    
    def _auth_sender(self, route):
        auth_instance = self._routes[route].get('sender_auth')
        if auth_instance:
            
            auth_approaches = []
            if type(auth_instance) == list:
                auth_approaches.extend(auth_instance)
            else:
                auth_approaches.append(auth_instance)
            
            authed = False
            for auth_approach in auth_approaches:
                if auth_approach().auth(self.raw_message_data, self._peer_ip, self.message):
                    authed = True
                    break
            
            if not authed:
                raise SenderAuthException('Sender %s authentication failed.' % self.mailfrom)            
    
    def _populate_instance_variables_from_named_capture_groups(self, regex, addr):
        match = re.match(regex, addr)
        for k, v in match.groupdict().items():
            self.__dict__[k] = v
        
    def _register_routes(self):
        self._routes = {}
        
        for attr_name in self.__class__.__dict__:
            if attr_name[0:1] == '_':
                continue
            
            method = getattr(self, attr_name)
            if type(method) == type(self._register_routes):
                default_kwargs = self._extract_default_kwargs(method)
                if default_kwargs.get('route'):
                    self._routes[default_kwargs.get('route')] = {
                        'method': method,
                        'sender_auth': default_kwargs.get('sender_auth')
                    }
        
    def _extract_default_kwargs(self, method):
        argspec = inspect.getargspec(method)
        
        argspec_defaults = list( argspec.defaults )
        default_kwargs = {}
        for arg in argspec.args:
            if arg == 'self':
                continue
                
            default_kwargs[arg] = argspec_defaults.pop(0)
        return default_kwargs