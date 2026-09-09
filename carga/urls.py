from django.urls import path

from . import views


urlpatterns = [
    path('', views.carga_list, name='carga_list'),
    path('criar/', views.carga_create, name='carga_create'),
]