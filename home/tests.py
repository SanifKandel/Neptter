from django.test import Client, SimpleTestCase,TestCase
from django.urls import resolve, reverse

from home.views import HomeProcess

# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_home_url(self):
        url=reverse('home')
        print(url)
        self.assertEqual(resolve(url).func,HomeProcess)