import unittest, email
from smtproutes.model import Message, Attachment

class TestAttachment(unittest.TestCase):
    
    def setUp(self):
        self.attachment_eml = file('test/fixtures/attachments.eml').read()
    
    def test_attachments_filenames_populated(self):
        message = email.message_from_string(self.attachment_eml, Message)
        self.assertEqual(message.attachments[0].filename, 'tokyo.jpg')
        self.assertEqual(message.attachments[1].filename, 'attachments_logo_fix_02_300.png')
    
    def test_attachments_data_right_number_of_bytes(self):
        message = email.message_from_string(self.attachment_eml, Message)
        self.assertEqual(len(message.attachments[0].data), 62116)
        self.assertEqual(len(message.attachments[1].data), 2475)
    
    def test_attachment_extension_populated(self):
        message = email.message_from_string(self.attachment_eml, Message)
        self.assertEqual(message.attachments[0].extension, 'jpg' )
        self.assertEqual(message.attachments[1].extension, 'png' )
        
    def test_attachment_mime_type_populated(self):
        message = email.message_from_string(self.attachment_eml, Message)
        self.assertEqual(message.attachments[0].mime_type, 'image/jpeg' )
        self.assertEqual(message.attachments[1].mime_type, 'image/png' )
        
