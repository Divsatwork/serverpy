SERVPY_LOGO = """                      
  ___  ___ _ ____   ___ __  _   _ 
 / __|/ _ \ '__\ \ / / '_ \| | | |
 \__ \  __/ |   \ V /| |_) | |_| |
 |___/\___|_|    \_/ | .__/ \__, |
                     |_|    |___/ 
"""

POLLING_PING = 'ping'
POLLING_HEALTH = 'health'

ACTIVE_STATUS = 'active'
INACTIVE_STATUS = 'inactive'
SERVER_ERROR_STATUS = 'discovery server error'
SERVER_UNREACHABLE_STATUS = 'service unreachable'

POLLING_METHOD_CHOICES = (
    'ping', 'health'
)

STATS_PACKET_LIMIT = 5000
DEFAULT_DISCOVERY_SERVER_PORT = 8008

ERROR_RESPONSE = {"status": "An error occurred while processing your request"}
SUCCESS_RESPONSE = {"status": "Success"}