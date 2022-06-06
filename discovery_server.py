import json
from models import Server
import web

class DiscoveryServer(Server):
    '''
    ----------------
    Discovery Server
    ----------------
    Class which will be responsible for collecting info about the services as
    provided in the input json/yaml. This server will use the polling methods to keep a track of the 
    runtime of the services.

    Functions:
    ----------
    1. Poll each and every service at specified time interval. (If no interval is specified, then default is 10 mins)
    2. Expose endpoints to query stats for each service.
    3. Expose endpoints to manage the properties of discovery server.
    '''
    def __init__(self, server_name: str, *args, **kwargs) -> None:
        super().__init__(server_name = server_name, *args, **kwargs)

    def __initialize_components(self):
        if not self.settings:
            raise Exception('Cannot start the application as no settings were found!')


    def run(self):
        self.__initialize_components()
        self.__start_discovery_server()
        
    def __start_discovery_server(self):
        """
        Here we make use of web.py library to build a small server which exposes APIs to query discovery server.
        """
        urls = (
            '/health', 'health'
        )

        app = web.application(urls, globals())        
        
        web.httpserver.runsimple(app.wsgifunc(), ("0.0.0.0", 8888))

class health:
    def GET(self):
        return json.dumps({"status": "Discovery Server running"})