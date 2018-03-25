from django.urls import path

from . import views

app_name="weekplanner"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:recipe_id>/edit', views.edit, name='edit'),
    path('<int:recipe_id>/', views.detail, name='detail'),
    path('addrecipe/', views.addRecipe, name='addrecipe')
]
