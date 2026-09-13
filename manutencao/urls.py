from django.urls import path
from . import views


urlpatterns = [
    path('', views.manutencao_list, name='manutencao_list'),
    path('cadastrar/', views.manutencao_create, name='manutencao_create'),
]