from django.shortcuts import render
from .models import Recipe

recipe_list = [
    {'title': "Pizza", 'recipe_id': 0},
    {'title': "Pahlava", 'recipe_id': 1},
    {'title': "Birthday Cake", 'recipe_id': 2}
]

# Create your views here.


def about_page(request):
    return render(request, 'main_page.html')


def catalog_page(request):
    recipes = Recipe.objects.all()

    context = {
        'recipe_list': recipes.order_by('name')
    }

    return render(request, 'catalog.html', context)


def recipe_detail(request, i):
    recipe = Recipe.objects.get(pk=i)
    ingredients = recipe.recipeingredient_set.all().order_by('ingredient__name')

    context = {
        'title': recipe.name,
        'recipe_id': i,
        'recipe_img': recipe.url,
        'ingredients': ingredients
    }

    return render(request, 'recipe_detail.html', context)
