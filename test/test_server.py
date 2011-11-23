import unittest
from smtproutes import Server, Route

class TestServer(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_process_message_should_delegate_to_a_route_registered_with_it(self):
        class RouteImpl(Route):
            
            def route(self, route=r'ben@example.com'):
                self.called = True
        
        message =  'To: Benjamin <ben@example.com>, eric@foo.com, Eric <eric2@example.com>\nFrom: Ben Coe <bencoe@example.com>'

        server = Server(('0.0.0.0', 465), None)
        server.add_route(RouteImpl)
        server.process_message(('0.0.0.0', '333'), 'mailfrom@example.com', 'rcpttos@example.com', message)
        