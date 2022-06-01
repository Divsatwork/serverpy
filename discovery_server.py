from models import Server

class DiscoveryServer:
    # TODO: Implement service mapping, status visibility, interval polling, health monitoring stats
    def __init__(self, *args, **kwargs):
        pass

    def start(self):
        self.web_server.start()

class UIServer:
    def __init__(self) -> None:
        pass

class DiscoveryServer(Server):

    def __init__(self, *args, **kwargs):
        super().__init__(server_name = "Discovery Server", *args, **kwargs)

    def run(self):
        pass

d = DiscoveryServer(capacity = 10)
print(d.server_name)
print(d.capacity)
