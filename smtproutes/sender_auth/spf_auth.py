import spf, re, email
from smtproutes.contact import Contact

class SPFAuth(object):
    
    def auth(self, message_data=None, peer_ip=None, message=None):
        mailfrom = Contact.create_contacts_from_message_field('from', message)[0]
        host = re.match('[^@]*@(.*)', mailfrom.email).group(1)
        result_status = spf.check(i=peer_ip, s=mailfrom.email, h=host)[0]
        if 'pass' in result_status:
            return True
        return False