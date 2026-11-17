from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    # Endereço antigo de cadastro: acesso restrito aos administradores.
    path('registrar/', views.usuario_register, name='usuario_register'),

    # Login e logout
    path('login/', views.ContaLoginView.as_view(), name='login'),
    path('login/<str:perfil>/', views.escolher_acesso, name='login_perfil'),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    # CRUD de usuários (área restrita)
    path('', views.usuario_list, name='usuario_list'),
    path('cadastrar/', views.usuario_create, name='usuario_create'),
    path('<int:pk>/', views.usuario_detail, name='usuario_detail'),
    path('<int:pk>/editar/', views.usuario_update, name='usuario_update'),
    path('<int:pk>/excluir/', views.usuario_delete, name='usuario_delete'),
]
