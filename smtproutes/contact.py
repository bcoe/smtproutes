from email.utils import parseaddr

class Contact(object):
    
    def __init__(self, raw_addr):
        parsed_raw_addr = parseaddr( raw_addr )
        self.name = parsed_raw_addr[0]
        self.email = parsed_raw_addr[1]
    
    def __str__(self):
        return '%s <%s>' % (self.name, self.email)
    
    @classmethod
    def create_contacts_from_message_field(cls, field_name, message):
        contacts = []
        raw_addrs = message.get_all(field_name, [])
        for raw_addr in raw_addrs:
            contacts.append( Contact(raw_addr) )
        return contacts