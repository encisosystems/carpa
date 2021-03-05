from django.test import TestCase
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

from . import views


# Create your tests here.

class LoginPageTests(SimpleTestCase):

    def test_login_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_login_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<form class="user">')
