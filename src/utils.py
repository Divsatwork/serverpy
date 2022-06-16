from datetime import datetime
import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import uuid

def __get_dict__(obj):
    if isinstance(obj, datetime):
        # return dict(year=obj.year, month=obj.month, day=obj.day, hour=obj.hour, minute=obj.minute, second=obj.second)
        return str(obj)
    else:
        return obj.__dict__

get_unique_id = lambda : str(uuid.uuid4())

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

def process_url(url: str):
    if not url or type(url) is not str:
        return
    processed_url = ''
    if not url.startswith('https'):
        processed_url+='https://'
    splits = url.split(':')
    hostname = splits[0]
    processed_url+=hostname

    return processed_url