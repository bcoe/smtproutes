import unittest, email
from smtproutes.sender_auth import SPFAuth

class TestSPFAuth(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_valid_ip_address_returns_true(self):
        auth = SPFAuth()
        message = email.message_from_string('From: Benjamin Coe <bcoe@uoguelph.ca>')
        self.assertTrue(auth.auth(str(message), '131.104.91.44', message))
        
    def test_invalid_ip_address_returns_false(self):
        auth = SPFAuth()
        message = email.message_from_string('From: Benjamin Coe <bcoe@uoguelph.ca>')
        self.assertFalse(auth.auth(str(message), '0.0.0.0', message))