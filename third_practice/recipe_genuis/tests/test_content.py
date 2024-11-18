from django.test import TestCase
from django.urls import reverse
from recipe_genius.models import Recipe, Ingredient


class RecipeModelTestCase(TestCase):
    @classmethod
    def setUp(self):
        self.ingredient1 = Ingredient.objects.create(name='Flour')
        self.ingredient2 = Ingredient.objects.create(name='Sugar')
        self.recipe = Recipe.objects.create(name='Cake', url='cake.jpg')
        self.recipe2 = Recipe.objects.create(
            name='Apple Pie', url='apple_pie.jpg')
        self.recipe.ingredients.add(self.ingredient1, self.ingredient2)
        self.recipe.save()

    def test_ingredients_creation(self):
        self.assertEqual(self.ingredient1.name, 'Flour')
        self.assertEqual(self.ingredient2.name, 'Sugar')

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.name, 'Cake')
        self.assertEqual(self.recipe.url, 'cake.jpg')
        self.assertEqual(self.recipe.ingredients.count(), 2)

    def test_get_ingredients_method(self):
        expected_ingredients = 'Flour, Sugar'
        self.assertEqual(self.recipe.get_ingredients(), expected_ingredients)

    def test_recipe_detail_ingredients_order(self):
        response = self.client.get(
            reverse('recipe_detail', args=[self.recipe.id]))
        ingredients = response.context['ingredients']
        ingredient_names = [
            ingredient.ingredient.name for ingredient in ingredients]
        self.assertEqual(ingredient_names, sorted(ingredient_names))

    def test_catalog_page_ordering(self):
        response = self.client.get(reverse('catalog_page'))
        recipes = response.context['recipe_list']
        recipe_names = [recipe.name for recipe in recipes]
        self.assertEqual(recipe_names, sorted(recipe_names))
