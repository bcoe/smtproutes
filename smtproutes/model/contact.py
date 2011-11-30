from email.utils import parseaddr, getaddresses

class Contact(object):
    
    def __init__(self, raw_addr=None, parsed_raw_addr=None):
        if raw_addr:
            parsed_raw_addr = parseaddr( raw_addr )
        self.name = parsed_raw_addr[0]
        self.email = parsed_raw_addr[1]
    
    def __str__(self):
        return '%s <%s>' % (self.name, self.email)
    
    @classmethod
    def create_contacts_from_message_field(cls, field_name, message):
        contacts = []
        raw_addrs = message.get_all(field_name, [])
        for parsed_raw_addr in getaddresses( raw_addrs ):
            contacts.append( Contact(parsed_raw_addr=parsed_raw_addr) )
        return contacts