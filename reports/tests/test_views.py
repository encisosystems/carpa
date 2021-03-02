from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def test_query_report_GET(self):
        client = Client()
        response = client.get(reverse('query_report'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'query_report.html')
 