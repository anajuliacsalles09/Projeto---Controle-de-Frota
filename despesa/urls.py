from django.urls import path
from . import views


urlpatterns = [
    path('', views.despesa_list, name='despesa_list'),
    path('cadastrar/', views.despesa_create, name='despesa_create'),
]