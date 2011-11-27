class route(object):
    
    def __init__(self, route, sender_auth=None):
        self.route = route
        self.sender_auth = sender_auth
    
    def __call__(self, f):
        def wrapped_f(self, route=self.route, sender_auth=self.sender_auth, *args, **kwargs):
            f(self, *args, **kwargs)
        return wrapped_f