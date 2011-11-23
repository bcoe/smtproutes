from example_route import ExampleRoute
from smtproutes import Server

server = Server(('0.0.0.0', 25), None)
server.add_route(ExampleRoute)
server.start()