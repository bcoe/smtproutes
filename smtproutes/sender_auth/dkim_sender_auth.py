import dkim
from smtproutes import Contact

class DKIMSenderAuth(object):
    
    def auth(self, message_data):
        return dkim.verify(message_data)