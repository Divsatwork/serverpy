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
"""
import argparse
from discovery_server import DiscoveryServer

from input_processor import InputProcessor
from request_processor import RequestProcessor

def main(args):
    """
    The main driver function which will spawn all the nodes and servers based on the input file provided
    by the user.
    """
    input_processor = InputProcessor('Input Processor', args.c)
    settings, _ = input_processor.process()
    discovery_server = DiscoveryServer('Discovery Server', settings=settings)
    request_processor = RequestProcessor('Request Processor', settings=settings)
    discovery_server.run()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Welcome to servpy!")
    parser.add_argument('-c', metavar='config_file', type=str, help='Input YML or JSON file', required=True)
    parser.add_argument('-l', metavar='logging_level', help='Logging level for the application', required=False, default='DEBUG')

    args = parser.parse_args()
    main(args)
    
    