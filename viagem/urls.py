from django.urls import path

from . import views


urlpatterns = [
    path('', views.viagem_list, name='viagem_list'),
    path('criar/', views.viagem_create, name='viagem_create'),
]