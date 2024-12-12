from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import IngredientForm, RecipeForm, RecipeIngredientFormSet
from django.http import Http404
from .models import Recipe

recipe_list = [
    {'title': "Pizza", 'recipe_id': 0},
    {'title': "Pahlava", 'recipe_id': 1},
    {'title': "Birthday Cake", 'recipe_id': 2}
]

# Create your views here.


def about_page(request):
    return render(request, 'main_page.html')


@login_required
def profile(request):
    recipes = Recipe.objects.all()

    context = {
        'recipe_list': recipes.order_by('name')
    }

    return render(request, 'profile.html', context)


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


@login_required
def create_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        ingredient_formset = RecipeIngredientFormSet(request.POST)

        if recipe_form.is_valid() and ingredient_formset.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user.username
            recipe.save()

            for ingredient_form in ingredient_formset:
                if ingredient_form.is_valid():
                    ingredient = ingredient_form.save(commit=False)
                    ingredient.recipe = recipe
                    ingredient.save()

            return redirect('profile')
    else:
        recipe_form = RecipeForm()
        ingredient_formset = RecipeIngredientFormSet()

    return render(request, 'create_recipe.html', {'form': recipe_form, 'ingredient_formset': ingredient_formset})


@login_required
def add_ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = IngredientForm()

    return render(request, 'add_ingredient.html', {'form': form})


@login_required
def delete_recipe(request, i):
    recipe = Recipe.objects.get(pk=i)

    if request.user.username == recipe.author:
        recipe.delete()
        return redirect('profile')
    else:
        raise Http404(
            "Вы не можете удалить этот рецепт, так как вы не являетесь его автором.")


@login_required
def update_recipe(request, i):
    recipe = get_object_or_404(Recipe, pk=i)

    if request.user.username != recipe.author:
        raise Http404(
            "Вы не можете изменить этот рецепт, так как вы не являетесь его автором.")

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, instance=recipe)
        ingredient_formset = RecipeIngredientFormSet(
            request.POST, instance=recipe)

        if recipe_form.is_valid() and ingredient_formset.is_valid():
            recipe = recipe_form.save()
            ingredient_formset.save()

            return redirect('profile')
    else:
        recipe_form = RecipeForm(instance=recipe)
        ingredient_formset = RecipeIngredientFormSet(instance=recipe)

    return render(request, 'update_recipe.html', {'form': recipe_form, 'ingredient_formset': ingredient_formset})
