from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    ingredients = models.ManyToManyField(
        Ingredient, through='RecipeIngredient')

    def __str__(self):
        return self.name

    def get_ingredients(self):
        return ', '.join([i.name for i in self.ingredients.all()])


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique_ingredient_in_recipe'
            )
        ]
