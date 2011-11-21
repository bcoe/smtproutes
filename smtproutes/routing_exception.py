class RoutingException(Exception):
    
    def __init__(self, message):
        Exception.__init__(self, "No route found for To: %s" % message.get('to'))