from django import forms
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from django.forms.widgets import NumberInput, TextInput

from .models import Ingredient, Recipe, RecipeIngredient


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'url']


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity', 'weight']

    def __init__(self, *args, **kwargs):
        super(RecipeIngredientForm, self).__init__(*args, **kwargs)
        self.fields['ingredient'].queryset = Ingredient.objects.all()
        self.fields['quantity'].widget = NumberInput()
        self.fields['weight'].widget = TextInput()


RecipeIngredientFormSet = inlineformset_factory(
    Recipe, RecipeIngredient, form=RecipeIngredientForm, extra=10)
