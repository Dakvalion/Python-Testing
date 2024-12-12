"""
URL configuration for recipe_genuis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from recipe_genius import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile', views.profile, name='profile'),
    path("admin/", admin.site.urls),
    path('', views.catalog_page, name='catalog_page'),
    path('about', views.about_page, name='about_page'),
    path('recipe/<int:i>', views.recipe_detail, name='recipe_detail'),
    path('create_recipe', views.create_recipe, name='create_recipe'),
    path('add_ingredient', views.add_ingredient, name='add_ingredient'),
    path('update_recipe/<int:i>/', views.update_recipe, name='update_recipe'),
    path('delete_recipe/<int:i>/', views.delete_recipe, name='delete_recipe'),
]
