from unittest import TestCase
from API import API


class Tester(TestCase):
    def setUp(self) -> None:
        self.api = API()

    def test_get_random_msg(self):
        msg = self.api.get_random_msg(endpoints=["https://smsta.ru/m/sms/m_erotic", "https://smsta.ru/w/sms/erotic"])
        print(msg)
