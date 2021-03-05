from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def test_harvests_GET(self):
        client = Client()
        response = client.get(reverse('harvests'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'harvests.html')


