from django.urls import path
from . import views


urlpatterns = [
    path('', views.veiculo_list, name='veiculo_list'),
    path('cadastrar/', views.veiculo_create, name='veiculo_create'),
    path('<int:id>/', views.veiculo_detail, name='veiculo_detail'),
    path('<int:id>/editar/', views.veiculo_update, name='veiculo_update'),
    path('<int:id>/excluir/', views.veiculo_delete, name='veiculo_delete'),
]