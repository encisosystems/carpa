from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def test_bunch_GET(self):
        client = Client()
        response = client.get(reverse('bunch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bunch.html')

    def test_bunchbatch_GET(self):
        client = Client()
        response = client.get(reverse('bunchbatch'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bunchbatch.html')

    def test_bunchcategory_GET(self):
        client = Client()
        response = client.get(reverse('bunchcategory'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bunchcategory.html')

    def test_sensor_GET(self):
        client = Client()
        response = client.get(reverse('sensor'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sensor.html')



