from django.urls import path

from . import views


urlpatterns = [
    path('', views.viagem_list, name='viagem_list'),
    path('criar/', views.viagem_create, name='viagem_create'),
    path('<int:pk>/', views.viagem_detail, name='viagem_detail'),
    path('<int:pk>/editar/', views.viagem_update, name='viagem_update'),
    path('<int:pk>/excluir/', views.viagem_delete, name='viagem_delete'),
]

