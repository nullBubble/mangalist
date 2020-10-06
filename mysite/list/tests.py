from django.test import TestCase
from django.test.client import Client

# Create your tests here.

class AddViewTests(TestCase):

    def test_add_view(self):
        client = Client()
        response = self.client.get('/add_manga/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response,"Enter the Mangadex Link")

    def test_check_if_wrong_url(self):
        # Check if the supplied url is a Mangadex link and not some other website link
        client = Client()
        response = self.client.post('/add_manga/', {'new_manga': 'test', 'chapter': 33, 'url':'https://google.com'}, follow=True)
        print(response.redirect_chain)
        self.assertRedirects(response, '/add_manga/', status_code=301, target_status_code=200)

    def test_check_if_correct_url(self):
        # Check if the supplied url is a Mangadex link and not some other website link
        client = Client()
        response = self.client.post('/add_manga/', {'new_manga': 'test', 'chapter': 33, 'url':'https://mangadex.org'}, follow=True)
        print(response.redirect_chain)
        self.assertRedirects(response, '/', status_code=301, target_status_code=200)


        

class DeleteViewTests(TestCase):

    def test_delete_view(self):
        client = Client()
        response = self.client.get('/delete_manga/')

        self.assertEqual(response.status_code, 200)
        # print(response.content)
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