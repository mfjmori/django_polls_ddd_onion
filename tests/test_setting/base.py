import inject
from tests.test_setting.inject_config import test_config
from django.test import TestCase


class CustomTestCase(TestCase):

    def setUp(self):
        inject.clear_and_configure(test_config)
