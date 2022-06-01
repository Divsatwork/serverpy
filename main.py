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
from curses import meta

from input_processor import InputProcessor

def main(*args, **kwargs):
    """
    The main driver function which will spawn all the nodes and servers based on the input file provided
    by the user.
    """
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Welcome to servpy!")
    parser.add_argument('-c', metavar='config_file', type=str, help='Input YML or JSON file', required=True)
    parser.add_argument('-l', metavar='logging_level', help='Logging level for the application', required=False, default='DEBUG')

    args = parser.parse_args()
    # main(args)

    p = InputProcessor('Input Processor', 'test.json')
    settings, errors = p.process()
    print(settings)
    print(errors)
