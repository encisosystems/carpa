from django.test import TestCase, Client
from django.urls import reverse
from harvests.urls import people, harvests


class TestViews(TestCase):

    def test_vehicles_GET(self):
        client = Client()
        response = client.get(reverse('vehicles'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'vehicles.html')

    def test_origin_GET(self):
        client = Client()
        response = client.get(reverse('origin'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'origin.html')


