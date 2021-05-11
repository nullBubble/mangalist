from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
# Basic tests to check the functionality of the Django application.

class AddViewTests(TestCase):

    def test_add_view(self):
        client = Client()
        response = self.client.get('/add_manga/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,"Enter the Mangadex Link")

    def test_check_if_wrong_url(self):
        # Check if the supplied url is a Mangadex link and not some other website link
        client = Client()
        response = self.client.post(reverse('list:add_manga'), {'new_manga': 'test', 'chapter': 33, 'url':'https://google.com'}, follow=True)
        self.assertRedirects(response, '/add_manga/')

    def test_check_if_correct_url(self):
        # Check if the supplied url is a Mangadex link and not some other website link
        client = Client()
        response = self.client.post('/add_manga/', {'new_manga': 'test', 'chapter': 33, 'url':'https://mangadex.org'},follow=True)
        self.assertRedirects(response, '/')


        

class DeleteViewTests(TestCase):

    def test_delete_view(self):
        client = Client()
        response = self.client.get('/delete_manga/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'name="deleted_manga"')

class DefaultViewTests(TestCase):

    def test_check_for_add_button(self):
        client = Client()
        response = self.client.get('/')
        self.assertContains(response, 'form action="add_manga/"')

    def test_check_for_delete_button(self):
        client = Client()
        response = self.client.get('/')
        self.assertContains(response, 'form action="delete_manga/"')