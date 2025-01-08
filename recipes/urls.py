from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('add/', views.recipe_add, name='recipe_add'),
    path('<int:pk>/edit/', views.recipe_edit, name='recipe_edit'),
    path('<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),
]
