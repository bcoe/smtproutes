import unittest
from smtproutes import SMTPRoute, RoutingException

class TestSMTPRoute(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def test_route_regexes_extracted_from_methods_on_class_inheriting_from_smtproute(self):
        
        class SMTPRouteImpl(SMTPRoute):
            
            def route1(self, awesome=5, route=r'ben@example.com'):
                pass
            
            def route2(self, route=r'ben2@example.com', cool=5):
                pass
            
        
        route = SMTPRouteImpl()
        self.assertTrue('ben@example.com' in route._routes)
        self.assertTrue('ben2@example.com' in route._routes)
    
    def test_calling_route_with_a_matching_regex_results_in_the_appropriate_route_being_invoked(self):

        class SMTPRouteImpl(SMTPRoute):
            
            def route1(self, awesome=5, route=r'ben@example.com'):
                self.bar = 'bar'
            
            def route2(self, route=r'ben2@example.com', cool=5):
                self.bar = 'foo'
            
        message =  """To: Benjamin <ben@example.com>, eric@foo.com, Eric <eric2@example.com>"""

        route = SMTPRouteImpl()
        route._route(
            message_data=message
        )
        self.assertEqual('bar', route.bar)
    
    def test_a_routing_exception_should_be_raised_if_the_route_is_not_found(self):
        class SMTPRouteImpl(SMTPRoute):
            pass
            
        message =  """To: Benjamin <ben@example.com>, eric@foo.com, Eric <eric2@example.com>"""
        route = SMTPRouteImpl()
        try:
            route._route(
                message_data=message
            )
            self.assertTrue(False)
        except RoutingException:
            self.assertTrue(True)
    
    def test_named_groups_stored_as_instance_variables_on_route(self):
        class SMTPRouteImpl(SMTPRoute):
            
            def route(self, route=r'(?P<user>[^-]*)-(?P<folder>.*)@.*'):
                self.called = True
        
        message =  """To: Benjamin <bencoe-awesome-folder@example.com>"""
        route = SMTPRouteImpl()
        route._route(message_data=message)
        self.assertEqual(route.user, 'bencoe')
        self.assertEqual(route.folder, 'awesome-folder')
        self.assertEqual(route.called, True)