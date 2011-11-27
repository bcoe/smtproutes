SMTPRoutes
==========

SMTPRoutes is a light weight SMTP server built on top of Secure-SMTPD.

It's what you'd get if Sinatra and SMTP had a baby.

Installation
------------

*easy_install smtproutes*

Routes
------

Routes are specified via a regex provided in the *route* decorator.

```python
from smtproutes import Route
from smtproutes.decorators import route

class ExampleRoute(Route):
	@route(r'myroute@.*')
    def my_route(self):
		print self.mailfrom.email
```

When invoked a route will have access to the following instance variables:

* _self.message_ the parsed email message.
* _self.mailfrom_ a contact object indicating who the message was received from.
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

* _DKIMAuth_ authenticates using a DKIM signature. (http://en.wikipedia.org/wiki/DomainKeys_Identified_Mail)
* _SPFAuth_ authenticates using an SPF record. (http://en.wikipedia.org/wiki/Sender_Policy_Framework)
* _GmailSPFAuth_ authenticates against Google's SPF records, regardless of sender (useful for Google Apps).

You can provide multiple authentication approaches in the *sender_auth* kwarg, if any pass the route will be called:

```python
def google_apps_spf_route(self, route=r'(?P<prefix>spf_google)@(?P<suffix>.*)', sender_auth=[SPFAuth, GmailSPFAuth]):
    print "%s at %s sent the message: \n\n %s" % (
        self.prefix,
        self.suffix,
        self.message
    )
```

Running a Server
----------------

The server is a thin abstraction on top of Secure-SMTPD (https://github.com/bcoe/secure-smtpd) hence:

* SSL is supported.
* Basic SMTP authentication is supported.

Create an instance of the server using the same options specified in the secure-smtpd project.

```python
from smtproutes import Server

server = Server(('0.0.0.0', 25), None)
```

Once the server is created, you can register routes with it and start it running:

```python
from example_route import ExampleRoute
server.add_route(ExampleRoute)
server.start()
```

The server will now be listening on port 25 for inbound SMTP messages.