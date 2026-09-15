from django.urls import path
from . import views


urlpatterns = [
    path('', views.manutencao_list, name='manutencao_list'),
    path('cadastrar/', views.manutencao_create, name='manutencao_create'),
    path('<int:pk>/', views.manutencao_detail, name='manutencao_detail'),
    path('<int:pk>/editar/', views.manutencao_update, name='manutencao_update'),
    path('<int:pk>/excluir/', views.manutencao_delete, name='manutencao_delete'),
]