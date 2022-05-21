from django.test import Client, SimpleTestCase,TestCase
from django.urls import resolve, reverse

# from login.views import registerProcess
from .forms import *

# Create your tests here.

class TestForm(TestCase):
    def test_register_form_valid_data(self):
        valid_form = CreateUserForm(data={
            'username': 'test',
            'email': 'test@test.com',
            'first_name': 'test',
            'password1': 'test@123',
            'password2': 'test@123',
        })
        print(valid_form.errors)
        self.assertTrue(valid_form.is_valid())

class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.register_page_url = reverse('register')

    def setUp(self):
        pass

    def test_register_page(self):
        response = self.client.get(self.register_page_url)
        self.assertEquals(response.status_code, 200)