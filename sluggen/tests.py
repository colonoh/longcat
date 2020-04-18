from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from sluggen import views
from sluggen.models import Slug
from sluggen.utils import generate_new_slug


class GeneratorTests(TestCase):
    def test_generate_anything(self):
        self.assertIsNotNone(generate_new_slug('http://www.google.com/', 3))

    def test_generate_with_collision(self):
        pass


class APITests(APITestCase):
    def test_create_account(self):
        """
        Create a new account
        """
        url = reverse('slug-create')
        data = {'url': 'http://www.google.com/'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Slug.objects.count(), 1)
        self.assertEqual(Slug.objects.get().url, data['url'])
        self.assertIsNotNone(Slug.objects.get().slug)
