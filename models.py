class Server:
    def __init__(self, server_name: str, *args, **kwargs):
        self.server_name = server_name
        for item,value in kwargs.items():
            self.__setattr__(item, value)
        
    def run(self):
        """ Override this method for the server to run"""
        pass

class Processor:
    def __init__(self, processor_name: str, *args, **kwargs):
        self.processor_name = processor_name

    def process(self):
        """ Override this method for the processor to process on some entity"""
        pass

class Configuration:
    def __init__(self, service_name, server_urls, poll_method, poll_endpoint, apis,
    *args, **kwargs):
        self.service_name = service_name
        self.server_urls = server_urls
        self.poll_method = poll_method
        self.poll_endpoint = poll_endpoint
        self.apis = apis
    
    def __str__(self) -> str:
        return f"Config(name={self.service_name}, urls={self.server_urls}, poll_method={self.poll_method}, poll_endpoint={self.poll_endpoint}, apis={self.apis})"
        

class Setting:
    def __init__(self, *args, **kwargs):
        self.settings = []

    def add(self, config: Configuration):
        self.settings.append(config)

    def __len__(self):
        return len(self.settings)

    def __str__(self):
        return f"Settings(settings = {[str(i) for i in self.settings]})"


