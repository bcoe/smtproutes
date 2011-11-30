import unittest, email
from smtproutes.model import Message

class TestMessage(unittest.TestCase):
    
    def setUp(self):
        self.attachment_eml = file('test/fixtures/attachments.eml').read()
    
    def test_parsing_message_with_custom_message_class(self):
        message = email.message_from_string(self.attachment_eml, Message)
        self.assertEqual(message.get('to'), 'bencoe@gmail.com')
    
    def test_attachments_returned_by_messages_attachments_property(self):
        message = email.message_from_string(self.attachment_eml, Message)
        self.assertEqual(len(message.attachments), 2)        