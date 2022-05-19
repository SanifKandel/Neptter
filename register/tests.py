from django.test import Client, SimpleTestCase,TestCase
from django.urls import resolve, reverse

from login.views import registerProcess

# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_register_url(self):
        url=reverse('register')
        print(url)
        self.assertEqual(resolve(url).func,registerProcess)