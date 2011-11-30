import re

class Attachment(object):
    
    def __init__(self, filename=None, data=None, mime_type=None):
        self.filename = filename
        self.data = data
        self.mime_type = mime_type
        self._populate_extension()
    
    def _populate_extension(self):
        self.extension = None
        match = re.match('.*\.(?P<extension>.*)', self.filename)
        if match:
            self.extension = match.group('extension')