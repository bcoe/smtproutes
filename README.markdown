SMTPRoutes
==========

SMTPRoutes is a light weight SMTP server built on top of Secure-SMTPD.

It's what you'd get if Sinatra and SMTP had a baby.

Routes
------

Routes are specified via a regex provided in the *route* kwarg.

```python
from smtproutes import Route

class ExampleRoute(Route):
    def my_route(self, route=r'myroute@.*'):
		pass
```

When invoked a route will have access to the following instance variables:

* _self.message_ the parsed email message.
* _self.mailfrom_ a contact object incdicating who the message was received from.
* _self.tos_ an array of contact objects extracted from the To field.
* _self.ccs_ an array of contact objects extracted from the CC field.
* _self.bccs_ an array of contact objects extracted from the BCC field.

Any named groups specified in the route regex will be availble as instance variables.

```python
class ExampleRoute(Route):
    
    def open_route(self, route=r'(?P<prefix>open)@(?P<suffix>.*)'):
        print "%s at %s sent the message: \n\n %s" % (
            self.prefix,
            self.suffix,
            self.message
        )
```

Sender Authentication
---------------------

Email is vulnerable to spoofing attacks. SMTPRoutes allows you to provide an authentication object to protect against these.

An authentication class can be provided in the *sender_auth* kwarg of a route.

```python
def spf_route(self, route=r'(?P<prefix>spf)@(?P<suffix>.*)', sender_auth=SPFAuth):
    print "%s at %s sent the message: \n\n %s" % (
        self.prefix,
        self.suffix,
        self.message
    )
```

Currently the following sender authentication methods are supported:

* _DKIMAuth_ authenticates using a DKIM signature.
* _SPFAuth_ authenticates using an SPF record.
* _GmailSPFAuth_ authenticates against Google's SPF records, regardless of sender (useful for Google Apps).

You can provide multiple authentication approaches in the *sender_auth* kwarg, if any pass the route will be called:

```python
def spf_google_apps_spf_route(self, route=r'(?P<prefix>spf_google)@(?P<suffix>.*)', sender_auth=[SPFAuth, GmailSPFAuth]):
    print "%s at %s sent the message: \n\n %s" % (
        self.prefix,
        self.suffix,
        self.message
    )
```