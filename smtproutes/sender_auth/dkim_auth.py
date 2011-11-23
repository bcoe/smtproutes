import dkim

class DKIMAuth(object):
    
    def auth(self, message_data, peer_ip):
        return dkim.verify(message_data)