import spf

class GmailSPFAuth(object):
    
    ARBITRARY_GMAIL_ADDRESS = 'bencoe@gmail.com'
    
    def auth(self, message_data=None, peer_ip=None, message=None):
        result_status = spf.check(i=peer_ip, s=self.ARBITRARY_GMAIL_ADDRESS, h='google.com')[0]
        if 'pass' in result_status:
            return True
        return False