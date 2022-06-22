from models import Configuration


class _ServiceInstanceConfiguration(Configuration):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service_name = service_name
        self.server_urls = server_urls
        self.poll_method = poll_method
        self.poll_endpoint = poll_endpoint
        self.poll_retries = poll_retries
        self.poll_delay = poll_delay
        self.poll_freq = poll_frequency
        self.packet_limit: int = packet_limit
        self.apis = apis


class _ServiceConfiguration:
    
    def __init__(self):
        self.service_configuration = []

    def add(self, config: _ServiceInstanceConfiguration):
        self.service_configuration.append(config)
        

