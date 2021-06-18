from django.shortcuts import render, reverse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'potato': {
        'картошка, г': 200,
        'соль, г': 5,
        'масло, г': 15,
    }
    # добавил картошку
}


def home_view(request):
    template_name = 'calculator/home.html'
    return render(request, template_name)  # наверное для одной надписи главная страница не надо рендера.


# def home_view(request):
#     """второй способ: сделать переход по ссылкам"""
#     template_name = 'calculator/home.html'
#     pages = {
#         'Главная страница': reverse('home'),
#         'Страница с рецептами': reverse('recipes')
#     }
#     context = {'pages': pages}
#     return render(request, template_name, context)


# def recipe_list_view(request):
# для второго способа - страница с выбором блюд. пока не добавлять переменную recipe в recipe_view - это работает,
# создаёт в цикле эти ссылки перехода, а имена берутся из urls в цикле ниже там
#     template_name = 'calculator/home.html'
#     pages = {}
#
#     for recipe in DATA:
#         pages[recipe] = reverse(recipe)
#
#     context = {'pages': pages}
#     return render(request, template_name, context)


def recipe_view(request, recipe):
    template_name = 'calculator/index.html'
    data = DATA[recipe]
    servings = request.GET.get('servings')

    if servings:
        data = {key: value * int(servings) for key, value in data.items()}  # какая красота...))))

    context = {'recipe': data}

    return render(request, template_name, context)


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
