from django.urls import path
from .views import home_view, recipe_view
# from .views import recipe_list_view  # нужно для второго способа, который я пытался сделать
# from .views import DATA


urlpatterns = [
    # path('recipes/', recipe_list_view, name='recipes'),  # строчка с списком рецептов для второго способа
    path('<recipe>/', recipe_view, name='recipe'),
]

# здесь я пытался для каждого блюда создать в цикле свой юрл с именем рецепта, чтобы потом reverse сделать,
# но так не сработало, потому что recipe параметр...
# for r in DATA:
#     urlpatterns.append(path('recipes/<recipe>/', recipe_view, name=r))
