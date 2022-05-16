
from django.test import Client, SimpleTestCase,TestCase
from django.urls import resolve, reverse

from register.views import registerProcess

# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_register_url(self):
        url=reverse('register')
        print(url)
        self.assertEqual(resolve(url).func,registerProcess)


# class TestViews(TestCase):
#     def setUp(self):
#         self.registerUrl=reverse('register')
#         self.client = Client()
#         self.client.register( fistName='test' username='test' , email='test@example.com', password='test')

#     def test_login(self):
#         response = self.client.get(self.registerUrl)
#         self.assertEqual(response.status_code,200)