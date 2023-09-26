"""
Python Library to quickly deploy a Service Discovery Web App.
Feel free to use it when handling several microservices becomes a pain.

Created By:
===========
Divs

Mainainted By:
==============
Divs

Github Link:
============
https://github.com/Divsatwork/servpy

LinkedIn Link:
==============
https://www.linkedin.com/in/divyansh-chopra
"""
import argparse
import logging

from .models import Statistics

from .ui_server import UIServer
from .constants import LOGGING_FILE_NAME, SERVPY_LOGO
from .discovery_server import DiscoveryServer

from .input_processor import InputProcessor
from .request_processor import RequestProcessor

def main():
    """
    The main driver function which will spawn all the nodes and servers based on the input file provided
    by the user.

    """
    parser = argparse.ArgumentParser(description=SERVPY_LOGO)
    parser.add_argument('-c', metavar='config_file', type=str, help='Input YML or JSON file', required=True)
    parser.add_argument('-l', metavar='logging_level', help='Logging level for the application', required=False, default='DEBUG')

    args = parser.parse_args()
    logging.basicConfig(filename=LOGGING_FILE_NAME, filemode='a', format='%(name)s - %(asctime)s - %(levelname)s - %(message)s', 
    level=logging.DEBUG)

    logging.info(SERVPY_LOGO)
    logging.info("Initializing components")
    #testing
    input_processor = InputProcessor('Input Processor', args.c)
    settings, _ = input_processor.process() 
    statistics = Statistics(service_statistics=list())
    discovery_server = DiscoveryServer('Discovery Server', settings=settings, statistics=statistics)
    request_processor = RequestProcessor('Request Processor', settings=settings, statistics=statistics)
    ui_server = UIServer(settings=settings, statistics=statistics)
    discovery_server.run()
    request_processor.process()
    ui_server.run()
    