import spf

class GmailSPFAuth(object):
    def auth(self, message_data=None, peer_ip=None, message=None):
        result_status = spf.check(i=peer_ip, s='@gmail.com', h='google.com')[0]
        if 'pass' in result_status:
            return True
        return False