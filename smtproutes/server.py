import ssl, asyncore
from secure_smtpd import SMTPServer

class Server(SMTPServer):
    
    def __init__(self, localaddr, remoteaddr, ssl=False, certfile=None, keyfile=None, ssl_version=ssl.PROTOCOL_SSLv23, require_authentication=False, credential_validator=None, debug=False):
        SMTPServer.__init__(self, localaddr, remoteaddr, ssl, certfile, keyfile, ssl_version, require_authentication, credential_validator, debug)
        self.routes = []
    
    def add_route(self, RouteClass):
        self.routes.append(RouteClass)
    
    def process_message(self, peer, mailfrom, rcpttos, message_data):
        for RouteClass in self.routes:
            try:
                route = RouteClass(peer_ip=peer[0])
                route._route(message_data)
            except Exception, e:
                print e
    
    def start(self):
        asyncore.loop()