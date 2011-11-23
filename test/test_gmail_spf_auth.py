import unittest, email
from smtproutes.sender_auth import GmailSPFAuth

class TestGmailSPFAuth(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_valid_google_ip_address_returns_true(self):
        auth = GmailSPFAuth()
        self.assertTrue(auth.auth(None, '209.85.213.46'))
        
    def test_invalid_google_ip_address_returns_false(self):
        auth = GmailSPFAuth()
        self.assertFalse(auth.auth(None, '0.0.0.0'))