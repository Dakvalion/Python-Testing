from django.shortcuts import render

recipe_list = [
    {'title': "Pizza", 'recipe_id': 0},
    {'title': "Pahlava", 'recipe_id': 1},
    {'title': "Birthday Cake", 'recipe_id': 2}
]

# Create your views here.


def about_page(request):
    return render(request, 'main_page.html')


def catalog_page(request):
    context = {
        'recipe_list': recipe_list
    }
    print(context)

    return render(request, 'catalog.html', context)


def recipe_detail(request, i):
    context = {
        'title': recipe_list[i]['title'],
        'recipe_id': i + 1
    }

    return render(request, 'recipe_detail.html', context)
