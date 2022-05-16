from django.test import Client, SimpleTestCase,TestCase
from django.urls import resolve, reverse

from login.views import loginProcess

# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_login_url(self):
        url=reverse('login')
        print(url)
        self.assertEqual(resolve(url).func,loginProcess)

class TestViews(TestCase):
    def setUp(self):
        self.loginUrl=reverse('login')
        self.client = Client()
        self.client.login(username='test' , password='test')

    def test_login(self):
        response = self.client.get(self.loginUrl)
        self.assertEqual(response.status_code,200)