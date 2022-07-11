import json
import logging
from threading import Thread

from flask import Flask

from .utils import make_json_response

from .constants import SUCCESS_RESPONSE, ERROR_RESPONSE, DEFAULT_DISCOVERY_SERVER_PORT

from .watchdog import WatchDog
from .models import Server, ServiceStatistics

class _DiscoveryServer(Server):
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
        """
        Initialize the following things:
        1. For each Configuration, create a watchdog thread
        2. For each Configuration, create a ServerStatistics object and assign it to global Statistics object
        """
        if not self.settings:
            raise Exception('Cannot start the application as no settings were found!')
        watchdogs = list()
        for config in self.settings:
            # create watchdog here
            url = config.server_urls
            service_stats = ServiceStatistics(config, url)
            self.statistics.service_statistics.append(service_stats)
            watchdogs.append(WatchDog(statistics=service_stats, **config.__dict__))
        self.watchdogs = watchdogs
        logging.info("All components of discovery service have been initialized")

    def run(self):
        self.__initialize_components()
        self.__start_discovery_server()
        
    def __start_discovery_server(self):
        """
        Here we make use of web.py library to build a small server which exposes APIs to query discovery server.
        """
        self.threads = [Thread(target=watchdog.watch) for watchdog in self.watchdogs]
        logging.info("Starting watchdogs")
        for t in self.threads:
            t.start()
        logging.info("All watchdogs have been started")
        
        port = self.settings.meta_info.discovery_server_port if self.settings.meta_info else DEFAULT_DISCOVERY_SERVER_PORT
        app = Flask(__name__)

        # Serve React App
        @app.route('/health')
        def health():
            return make_json_response(app, {"status": "Discovery Server running"})

        @app.route('/stats')
        def stats():
            """
            1. Iterate in the service_statistics section
            2. Get all different service_name and group objects accordingly
            """
            polished_stats = dict()
            service_names = set([i.service_name for i in self.statistics.service_statistics])
            for service in service_names:
                polished_stats[service] = [i.__dict__ for i in list(filter(lambda x: x.service_name == service, self.statistics.service_statistics))]
            return make_json_response(app, polished_stats)

        @app.route('/dump')
        def dump():
            try:
                with open('stats.dump', 'w') as f:
                    json.dump(self.statistics, f)
                return make_json_response(app, SUCCESS_RESPONSE)
            except:
                return make_json_response(app, ERROR_RESPONSE)
        

        logging.info(f"Starting Discovery Service at localhost:{port}")
        deamon = Thread(name='ui_server', target=app.run, kwargs={"use_reloader":False, "port":port})
        deamon.setDaemon(True)
        deamon.start()
        logging.info(f"UI Service daemon started. PID = {deamon.native_id}")

class DiscoveryServer(_DiscoveryServer):
    pass
