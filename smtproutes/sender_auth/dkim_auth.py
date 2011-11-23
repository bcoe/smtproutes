import dkim

class DKIMAuth(object):
    
    def auth(self, message_data=None, peer_ip=None, message=None):
        return dkim.verify(message_data)