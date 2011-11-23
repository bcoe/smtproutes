from smtproutes import Route
from smtproutes.sender auth import DKIMAuth, GmailSPFAuth, SPFAuth

class ExampleRoute(Route):
    
    def open_route(self, route=r'(?P<prefix>open)@(?P<suffix>.*)'):
        print "%s at %s sent the message: \n\n %s" % (
            self.prefix,
            self.suffix,
            self.message
        )

    def dkim_route(self, route=r'(?P<prefix>dkim)@(?P<suffix>.*)', sender_auth=DKIMAuth):
        print "%s at %s sent the message: \n\n %s" % (
            self.prefix,
            self.suffix,
            self.message
        )

    def spf_route(self, route=r'(?P<prefix>spf)@(?P<suffix>.*)', sender_auth=SPFAuth):
        print "%s at %s sent the message: \n\n %s" % (
            self.prefix,
            self.suffix,
            self.message
        )

    def spf_google_apps_spf_route(self, route=r'(?P<prefix>spf)@(?P<suffix>.*)', sender_auth=[SPFAuth, GmailSPFAuth]):
        print "%s at %s sent the message: \n\n %s" % (
            self.prefix,
            self.suffix,
            self.message
        )