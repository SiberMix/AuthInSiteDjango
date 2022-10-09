from unittest import TestCase

from store.logic import operations


class LoginTestCase(TestCase):
    def test_plus(self):
        result = operations(6, 13, '+')
        self.assertEqual(19, result)