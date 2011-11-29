import time
from smtproutes import Route, Server
from smtproutes.decorators import route

class BenchmarkRoute(Route):
    @route(r'(?P<prefix>[^@]*)@(?P<suffix>.*)')
    def benchmark_route(self):
        pass
        
Server(('0.0.0.0', 25), None).add_route(BenchmarkRoute).start()
