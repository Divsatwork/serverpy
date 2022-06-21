from .models import Configuration, MetaInfo, Processor, Setting
from .constants import POLLING_METHOD_CHOICES as polling_method_choices
import logging
import json
import yaml

log = logging.getLogger()
# TODO: Implement constants here
class InputProcessor(Processor):
    '''
    ---------------
    Input Processor
    ---------------

    Processes the input JSON/YAML file and maps all the details accordingly.

    In the input file, each service will have it's own listing. For example:
    {
        "service 1": { service 1 details }
    }\\
    The details for each service contain the following things:
    1. Service instance url (host)
    2. Polling coinfugration for that service instance.
    3. List of APIs that the instances of the service listen to.

    The service instance urls can be passed in two ways:
    1. Using dictionary style to seperate out all the instances and provide different polling
    configuration for each instance.
    2. Using list to provide all the instance, the same polling configuration.

    For more examples see:
    1. https://github.com/Divsatwork/servpy/blob/main/test.json
    2. https://github.com/Divsatwork/servpy/blob/main/test.yaml

    '''
    def __init__(self, processor_name: str, filename: str, *args, **kwargs):
        super().__init__(processor_name=processor_name, *args, **kwargs)
        self.config_file = filename
        self.__check_input_file()

    def __process(self):
        '''
        The main config file processing method.
        Here we are considering two cases of input files - json and yaml.

        Returns:
        --------
        config = the configuration after processing

        '''
        try:
            if(self.config_file.endswith('json')):
                with open(self.config_file) as f:
                    config = json.load(f)
            elif(self.config_file.endswith('yaml')):
                with open(self.config_file) as f:
                    config = yaml.safe_load(f)
        except Exception as e:
            log.error(f'Error occured while reading file: {self.config_file}')
            raise Exception(f'Error occured while reading file: {self.config_file}')
        
        self.setting, errors = self.validate_config(config)
        
        if errors:
            raise Exception(f'Errors: {errors}')
        log.info(f"Settings loaded, {self.setting}")
        return self.setting, errors
    
    def process(self):
        return self.__process()

    def __check_input_file(self):
        try:
            open(self.config_file)
        except:
            log.error(f'Error occurred while attempting to open config file. {self.config_file}')
            raise Exception(f'Error occurred while opening file: {self.config_file}. Please make sure the path is correct.')

    def verify_config(self, config):
        errors = list()
        if type(config) is not dict:
            errors.append("Configuration not of type dict")
            return errors
        for key, value in config.items():
            if key == "meta-info":
                continue
            if type(key) is not str:
                errors.append(f"Not a service name. Check the service name: {key}")
                continue
            if type(value) is not dict:
                errors.append(f"Please check the configuration values for {key}")
                continue
            if value.get('server') is None:
                errors.append(f"No server urls found for service: {key}")
            if value.get('polling') is None:
                errors.append(f"No polling definition found for service: {key}")
            if value.get('apis') is None:
                errors.append(f"No APIs provided for service: {key}")

            if value.get('server'):
                server = value.get('server')
                if type(server) is not list or len(server) == 0:
                    errors.append(f"Please check server urls for service: {key}")
            if value.get('polling'):
                polling = value.get('polling')
                if type(polling) is not dict or polling == {}:
                    errors.append(f"Please check the polling section for service: {key}")
                if polling.get('method') not in polling_method_choices:
                    errors.append(f"Incorrect polling method specified for service: {key}")
                method = polling.get('method')
                if (method == "health" and polling.get('endpoint') is None) or (method == "health" and type(polling.get('endpoint')) is not str):
                    errors.append(f"Please specify health endpoint for service: {key}")
                
            if value.get('apis'):
                apis = value.get('apis')
                if type(apis) is not list or len(apis) == 0:
                    errors.append(f"Please specify apis for service: {key}")
        return errors

    def populate_defaults(self, config):
        for key, value in config.items():
            if key == "meta-info":
                continue
            if not value.get('polling').get('frequency'):
                value['polling']['frequency'] = 10

    def validate_config(self, config):
        if config is None:
            return {}, None
        
        errors = self.verify_config(config)
        if errors:
            log.error(errors)
            return {}, errors

        self.populate_defaults(config)

        setting = Setting()
        for key, value in config.items():
            if key == "meta-info":
                # Processing the meta info here
                meta = MetaInfo(**value)
                setting.update_meta_info(meta)
                continue
            # For each configuration, get a new Configuration obj
            configuration = Configuration(key, 
            value.get('server'), value.get('polling').get('method'), value.get('polling').get('endpoint'), value.get('apis'),
            value.get('polling').get('retries'), value.get('polling').get('retry_delay'), value.get('polling').get('frequency'), 
            value.get('polling').get('packet_limit'))
            setting.add(configuration)
        return setting, None
