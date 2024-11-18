from django.test import TestCase
from django.urls import reverse
from recipe_genius.models import Recipe


class TestUrls(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.recipe = Recipe.objects.create(
            name='Test Recipe',
            url='img/nuga.jpg'
        )

    def test_catalog_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog.html')

    def test_about_page(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_recipe_detail_page(self):
        response = self.client.get('/recipe/1')
        self.assertEqual(response.status_code, 200)

    def test_catalog_page_url(self):
        url = reverse('catalog_page')
        self.assertEqual(url, '/')

    def test_about_page_url(self):
        url = reverse('about_page')
        self.assertEqual(url, '/about')

    def test_recipe_detail_url(self):
        url = reverse('recipe_detail', args=[1])
        self.assertEqual(url, '/recipe/1')
