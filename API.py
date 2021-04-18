from parser import *
from random import choice
from logging import getLogger

class API:
    def __init__(self):
        self._log = getLogger("API")

    def get_all_msgs(self, endpoint):
        self._log.debug(f"Getting all msgs from group {endpoint}")
        msgs = get_group_msgs(endpoint)
        self._log.debug(f"Get {msgs}")
        return msgs

    def get_random_msg(self, endpoint):
        self._log.debug(f"Getting random msg from group {endpoint}")
        msg = choice(self.get_all_msgs(endpoint))
        self._log.debug(f"Get {msg}")
        return msg
