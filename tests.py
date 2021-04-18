from unittest import TestCase
from API import API
from config import *
import logging
from love_parser import *


class Tester(TestCase):
    def setUp(self) -> None:
        self.api = API()
        logging.basicConfig(level=logging.DEBUG)

    def test_get_random_msg(self):
        msg = self.api.get_random_msg(endpoints=[ENDPOINTS["her"]["love"]])
        print(msg)

    def test_get_all_msgs(self):
        msgs = self.api.get_all_msgs_group(endpoint=ENDPOINTS["him"]["morning"])
        print(len(msgs))

    def test_get_link(self):
        link="http://test_link.ru/page"
        self.assertEqual(get_page_link(link, 2), "http://test_link.ru/page_2")