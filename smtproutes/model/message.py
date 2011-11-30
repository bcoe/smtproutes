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
            attachments.append(Attachment(filename=filename, data=data, mime_type=part.get_content_type()))
        return attachments