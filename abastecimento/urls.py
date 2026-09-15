from django.urls import path

from . import views


urlpatterns = [
    path('', views.abastecimento_list, name='abastecimento_list'),
    path('cadastrar/', views.abastecimento_create, name='abastecimento_create'),
    path('<int:pk>/', views.abastecimento_detail, name='abastecimento_detail'),
    path('<int:pk>/editar/', views.abastecimento_update, name='abastecimento_update'),
    path('<int:pk>/excluir/', views.abastecimento_delete, name='abastecimento_delete'),
]