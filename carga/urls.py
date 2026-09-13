from django.urls import path

from . import views


urlpatterns = [
    path('', views.carga_list, name='carga_list'),
    path('criar/', views.carga_create, name='carga_create'),
    path('<int:pk>/', views.carga_detail, name='carga_detail'),
    path('<int:pk>/editar/', views.carga_update, name='carga_update'),
    path('<int:pk>/excluir/', views.carga_delete, name='carga_delete'),
]