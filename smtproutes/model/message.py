import re, base64
import email.message
from attachment import Attachment

class Message(email.message.Message):

    @property
    def attachments(self):
        attachments = []
        
        for part in self.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            
            filename = part.get_filename()
            
            if not filename:
                continue
            
            data = part.get_payload(decode=True)
            attachments.append(Attachment(filename=self._decode_string( filename ), data=data, mime_type=part.get_content_type()))
        return attachments
    
    @property
    def body(self):
        for part in self.walk():
            if part.get_content_maintype() == 'text':
                return part.get_payload()
        return ''
    
    def _decode_string(self, filename):
        try:
            if '?B?' in filename:
                match = re.match(r'=\?(?P<encoding>.*)\?B\?(?P<text>.*)\?=', filename)
                codes = base64.b64decode(match.group( 'text' ))
                return codes.decode( match.group('encoding') )
        except Exception:
            pass
        return filename