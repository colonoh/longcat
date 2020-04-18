import random

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from sluggen import views
from sluggen.models import Slug
from sluggen.utils import generate_new_slug


class GeneratorTests(TestCase):
    def test_generate_working_at_all(self):
        self.assertIsNotNone(generate_new_slug(3))

    def test_generate_with_collisions(self):
        # original slug
        random.seed(0)
        first_slug = generate_new_slug(3)
        Slug.objects.create(url='http://www.lol.com/', slug=first_slug)

        # first duplicate
        random.seed(0)
        second_slug = generate_new_slug(3)
        Slug.objects.create(url='http://www.lol.com/', slug=second_slug)
        self.assertNotEqual(first_slug, second_slug)

        # second duplicate
        random.seed(0)
        third_slug = generate_new_slug(3)
        Slug.objects.create(url='http://www.lol.com/', slug=third_slug)
        self.assertNotEqual(second_slug, third_slug)


class APITests(APITestCase):
    def test_create_account(self):
        url = reverse('slug-create')
        data = {'url': 'http://www.google.com/'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Slug.objects.count(), 1)
        self.assertEqual(Slug.objects.get().url, data['url'])
        self.assertIsNotNone(Slug.objects.get().slug)
