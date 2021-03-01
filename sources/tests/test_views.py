from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def test_vehicles_GET(self):
        client = Client()
        response = client.get(reverse('vehicles'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'vehicles.html')

    def test_parcel_GET(self):
        client = Client()
        response = client.get(reverse('parcel'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'parcel.html')


