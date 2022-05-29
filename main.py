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

from discovery_server import DiscoveryServer

if __name__ == "__main__":
    # TODO: Get arguments here
    server = DiscoveryServer()
    server.start()