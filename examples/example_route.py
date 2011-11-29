from smtproutes import Route, Server
from smtproutes.sender_auth import DKIMAuth, GmailSPFAuth, SPFAuth
from smtproutes.decorators import route

class ExampleRoute(Route):
    
    @route(r'(?P<prefix>open)@(?P<suffix>.*)')
    def open_route(self):
        print "%s at %s sent the message: \n\n %s" % (
            self.prefix,
            self.suffix,
            self.message
        )
    
    @route(r'(?P<prefix>dkim)@(?P<suffix>.*)', sender_auth=DKIMAuth)
    def dkim_route(self):
        print "%s at %s sent the message: \n\n %s" % (
            self.prefix,
            self.suffix,
            self.message
        )

    @route(r'(?P<prefix>spf)@(?P<suffix>.*)', sender_auth=SPFAuth)
    def spf_route(self):
        print "%s at %s sent the message: \n\n %s" % (
            self.prefix,
            self.suffix,
            self.message
        )

    @route(r'(?P<prefix>spf_google)@(?P<suffix>.*)', sender_auth=[SPFAuth, GmailSPFAuth])
    def google_apps_spf_route(self):
        print "%s at %s sent the message: \n\n %s" % (
            self.prefix,
            self.suffix,
            self.message
        )

Server(('0.0.0.0', 25), None).add_route(ExampleRoute).start()