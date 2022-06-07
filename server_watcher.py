from models import Watcher
from utils import ping


class ServerWatcher(Watcher):
    def __init__(self, server_url, polling_method, polling_url, statistics, *args, **kwargs) -> None:
        super().__init__(server_url, polling_method, polling_url, statistics, *args, **kwargs)

    def __watch(self):
        if self.polling_method == 'ping':
            if ping(self.server_url):
                self.statistics.get('server_url')


    def watch(self):
        self.__watch()