from django.urls import path
from . import views


urlpatterns = [
    path('', views.abastecimento_list, name='abastecimento_list'),
    path('cadastrar/', views.abastecimento_create, name='abastecimento_create'),
]