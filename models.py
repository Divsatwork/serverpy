from collections import deque
import json

from constants import STATS_PACKET_LIMIT
class Server:
    '''
    Base class for Servers.
    Each server must be assigned a server_name.
    '''
    def __init__(self, server_name: str, *args, **kwargs) -> None:
        self.server_name = server_name
        for item,value in kwargs.items():
            self.__setattr__(item, value)
        
    def run(self) -> None:
        """ Override this method for the server to run"""
        pass

class Processor:
    '''
    Base class for Processors.
    Each processor must be assigned a processor_name.
    '''
    def __init__(self, processor_name: str, *args, **kwargs):
        self.processor_name = processor_name
        for item,value in kwargs.items():
            self.__setattr__(item, value)

    def process(self):
        """ Override this method for the processor to process on some entity"""
        pass

class Configuration:
    '''
    Smallest module of the input configuration file.
    One configuration is equivalent to One service details in the input json/yaml.
    '''
    def __init__(self, service_name, server_urls, poll_method, poll_endpoint, apis,
    *args, **kwargs) -> None:
        self.service_name = service_name
        self.server_urls = server_urls
        self.poll_method = poll_method
        self.poll_endpoint = poll_endpoint
        self.apis = apis
    
    def __str__(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, indent=2)


class Setting:
    '''
    Class to model the settings provided in the input json/yaml.
    Each setting can have it's own number of configurations.
    '''
    def __init__(self, *args, **kwargs) -> None:
        self.settings = []

    def add(self, config: Configuration) -> None:
        self.settings.append(config)

    def __len__(self) -> int:
        return len(self.settings)

    def __str__(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, indent=2)


class MetaInfo:
    '''
    Class to store the meta information passed within the input json/yaml.
    
    Fields:
    1. discovery_server_name -> Default = "Discovery Server"
    2. request_processor_name -> Default = "Request Processor"
    3. discovery_server_port -> Default = 8888
    '''
    def __init__(self, *args, **kwargs) -> None:
        for i,v in kwargs:
            self.__setattr__(i, v)

    def __str__(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, indent=2)


class StatisticsPacket:
    '''
    '''
    def __init__(self) -> None:
        self.start_time = None
        self.end_time = None
        self.final_status = None
        self.response = None

    def __str__(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, indent=2)


class ServiceStatistics:
    '''
    '''
    def __init__(self, service, *args, **kwargs) -> None:
        self.service = service
        self.uptime = 0
        self.last_checked_at = None
        self.last_failure = None
        self.stats_packets = deque(maxlen=STATS_PACKET_LIMIT)

    def __str__(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, indent=2)

    def register_stats_packet(self, packet: StatisticsPacket) -> None:
        self.stats_packets.append(packet)


class Statistics:
    '''
    '''
    def __init__(self, *args, **kwargs) -> None:
        self.services = []
        self.service_stats = []

    def __str__(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, indent=2)


class Watcher:
    '''
    Model class for watcher.
    '''
    def __init__(self, server_url, polling_method, polling_url, statistics, *args, **kwargs) -> None:
        self.server_url = server_url
        self.polling_method = polling_method
        self.polling_url = polling_url
        self.statistics = statistics

    def __str__(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__, indent=2)
    

