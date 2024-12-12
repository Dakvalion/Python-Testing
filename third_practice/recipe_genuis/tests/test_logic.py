from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from recipe_genius.models import Recipe, Ingredient, RecipeIngredient
from recipe_genius.forms import RecipeForm, RecipeIngredientForm, RecipeIngredientFormSet, IngredientForm


class RecipeModelTestCase(TestCase):
    @classmethod
    def setUp(self):
        self.author = User.objects.create_user(
            username='dakva', password='password123')
        self.other_user = User.objects.create_user(
            username='other_user', password='password123')

        self.ingredient1 = Ingredient.objects.create(name='Flour')
        self.ingredient2 = Ingredient.objects.create(name='Sugar')
        self.recipe = Recipe.objects.create(
            author='dakva', name='Cake', url='cake.jpg')
        self.recipe.ingredients.add(self.ingredient1, self.ingredient2)
        self.recipe.save()

    def test_create_recipe_authenticated(self):
        response = self.client.get(reverse('create_recipe'))
        self.assertEqual(response.status_code, 302)

        self.client.force_login(self.author)
        response = self.client.get(reverse('create_recipe'))
        self.assertEqual(response.status_code, 200)

    def test_add_ingredient_authenticated_user(self):
        self.client.force_login(self.other_user)
        add_ingredient_url = reverse('add_ingredient')

        response = self.client.get(add_ingredient_url)
        self.assertEqual(response.status_code, 200)

        self.client.logout()
        response = self.client.get(add_ingredient_url)
        self.assertEqual(response.status_code, 302)

    def test_delete_recipe_author(self):
        delete_url = reverse('delete_recipe', kwargs={'i': self.recipe.pk})

        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)

        self.client.force_login(self.other_user)
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 404)

        self.client.force_login(self.author)
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)

    def test_update_recipe_author(self):
        update_url = reverse('update_recipe', kwargs={'i': self.recipe.pk})

        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 302)

        self.client.force_login(self.other_user)
        response = self.client.get(update_url)
        self.assertEqual(response.status_code, 404)

        self.client.force_login(self.author)
        response = self.client.post(update_url)
        self.assertEqual(response.status_code, 200)
