from .models import Processor, Setting


class RequestProcessor(Processor):
    """
    1. Map urls to server urls.
    2. pick an instance and forward your request there.
    3. if request fails due to server unreachable, give custom response, else forward the response from the service.
    """
    def __init__(self, request_processor_name: str, settings: Setting, *args, **kwargs) -> None:
        super().__init__(processor_name=request_processor_name, *args, **kwargs)
        self.settings = settings

    def __process(self):
        pass

    def __get_url_mappings(self):
        pass

    def process(self):
        self.__process()