from example_route import ExampleRoute
from smtproutes import Server

Server(('0.0.0.0', 25), None).add_route(ExampleRoute).start()