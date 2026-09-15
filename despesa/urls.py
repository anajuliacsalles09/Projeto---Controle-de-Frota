from django.urls import path

from . import views


urlpatterns = [
    path('', views.despesa_list, name='despesa_list'),
    path('cadastrar/', views.despesa_create, name='despesa_create'),
    path('<int:pk>/', views.despesa_detail, name='despesa_detail'),
    path('<int:pk>/editar/', views.despesa_update, name='despesa_update'),
    path('<int:pk>/excluir/', views.despesa_delete, name='despesa_delete'),
]