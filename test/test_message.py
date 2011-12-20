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
    
    def test_body_returns_text_body_of_message(self):
        message = email.message_from_string(self.attachment_eml, Message)
        self.assertEqual(message.body, 'message with attachments.\n')
    
    def test_decode_filename_decodes_non_ascii_filenames(self):
        message = email.message_from_string(self.attachment_eml, Message)
        self.assertEqual(message._decode_string('=?Big5?B?xKy7t6fTsdCxwsKyvvoucGRm?='), u'\u8607\u9060\u5FD7\u6559\u6388\u7C21\u6B77.pdf')