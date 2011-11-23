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