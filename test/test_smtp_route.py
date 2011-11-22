import unittest
from smtproutes import SMTPRoute


class TestSMTPRoute(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def test_route_regexes_extracted_from_methods_on_class_inheriting_from_smtproute(self):
        
        class SMTPRouteImpl(SMTPRoute):
            
            def route1(awesome=5, route=r'ben@example.com'):
                pass
            
            def route2(route=r'ben2@example.com', cool=5):
                pass
            
        
        route = SMTPRouteImpl()
        self.assertTrue('ben@example.com' in route._routes)
        self.assertTrue('ben2@example.com' in route._routes)