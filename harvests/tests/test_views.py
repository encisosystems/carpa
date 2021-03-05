from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def test_people_GET(self):
        client = Client()
        response = client.get(reverse('people'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'people.html')