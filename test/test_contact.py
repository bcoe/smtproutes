import unittest, email
from smtproutes.model import Contact, Message

class TestContact(unittest.TestCase):
    
    def setUp(self):
        self.attachment_eml = file('test/fixtures/valid_dkim.eml').read()
        self.message = email.message_from_string(self.attachment_eml, Message)
    
    def test_create_contacts_from_message_field_successfully_creates_contact_object(self):
        contacts = Contact.create_contacts_from_message_field('to', self.message)
        self.assertEqual(contacts[0].email, 'bcoe@uoguelph.ca')
        self.assertEqual(contacts[0].name, 'ben coe')