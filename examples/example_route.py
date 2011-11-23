from smtproutes import Route

class ExampleRoute(Route):
    
    def echo_route(self, route=r'(?P<prefix>[^@]*)@(?P<suffix>.*)'):
        print "%s at %s sent the message: \n\n %s" % (
            self.prefix,
            self.suffix,
            self.message
        )