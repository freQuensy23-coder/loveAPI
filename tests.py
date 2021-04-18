from unittest import TestCase
from API import API
from config import *
import logging

class Tester(TestCase):
    def setUp(self) -> None:
        self.api = API()
        logging.basicConfig(level=logging.DEBUG)

    def test_get_random_msg(self):
        msg = self.api.get_random_msg(endpoints=[ENDPOINTS["her"]["quit"], ENDPOINTS["her"]["18+"]])
        print(msg)

    def test_get_all_msgs(self):
        msgs = self.api.get_all_msgs_group(endpoint=ENDPOINTS["him"]["morning"])
        print(msgs[0])