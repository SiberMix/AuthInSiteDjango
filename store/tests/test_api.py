from django.urls import reverse
from rest_framework.test import APITestCase

class BookApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('book-list')
        print(url)
        responce = self.client.get(url)
        print(responce.data)