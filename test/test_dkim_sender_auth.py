import unittest, email
from smtproutes import Route
from smtproutes.sender_auth import DKIMSenderAuth

class TestDKIMSenderAuth(unittest.TestCase):
    
    def setUp(self):
        self.valid_dkim_eml = file('test/fixtures/valid_dkim.eml').read()
        self.invalid_dkim_eml = file('test/fixtures/invalid_dkim.eml').read()
    
    def test_auth_returns_true_for_message_with_valid_dkim_signature(self):
        dkim_sender_auth = DKIMSenderAuth()
        self.assertTrue(dkim_sender_auth.auth(self.valid_dkim_eml))
        
    def test_auth_returns_false_for_message_with_invalid_dkim_signature(self):
        dkim_sender_auth = DKIMSenderAuth()
        self.assertFalse(dkim_sender_auth.auth(self.invalid_dkim_eml))