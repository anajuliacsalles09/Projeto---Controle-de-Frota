from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('', views.usuario_list, name='usuario_list'),
    path('cadastrar/', views.usuario_create, name='usuario_create'),
    path('<int:pk>/', views.usuario_detail, name='usuario_detail'),
    path('<int:pk>/editar/', views.usuario_update, name='usuario_update'),
    path('<int:pk>/excluir/', views.usuario_delete, name='usuario_delete'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='usuario/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),
]