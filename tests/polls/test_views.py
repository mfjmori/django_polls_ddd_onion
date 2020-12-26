import uuid
from django.urls import reverse_lazy
from django.test import Client
from tests.test_setting.base import CustomTestCase as TestCase


class TestIndexView(TestCase):

    def test_get(self):
        c = Client()
        request_path = reverse_lazy('polls:index')
        response = c.get(request_path)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['latest_question_list']), 5)
        self.assertEqual(
            response.context['latest_question_list'][0].id, uuid.UUID("00000000-0000-0000-0000-000000000005"))
        self.assertEqual(
            response.context['latest_question_list'][4].id, uuid.UUID("00000000-0000-0000-0000-000000000001"))
