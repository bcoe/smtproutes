import unittest, email
from smtproutes.sender_auth import DKIMAuth

class TestDKIMAuth(unittest.TestCase):
    
    def setUp(self):
        self.valid_dkim_eml = file('test/fixtures/valid_dkim.eml').read()
        self.invalid_dkim_eml = file('test/fixtures/invalid_dkim.eml').read()
    
    def test_auth_returns_true_for_message_with_valid_dkim_signature(self):
        dkim_auth = DKIMAuth()
        self.assertTrue(dkim_auth.auth(self.valid_dkim_eml, '0.0.0.0'))
        
    def test_auth_returns_false_for_message_with_invalid_dkim_signature(self):
        dkim_auth = DKIMAuth()
        self.assertFalse(dkim_auth.auth(self.invalid_dkim_eml, '0.0.0.0'))