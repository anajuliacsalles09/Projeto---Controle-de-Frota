from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('painel/', RedirectView.as_view(pattern_name='dashboard', permanent=False)),

    path('admin/', admin.site.urls),

    path('veiculos/', include('veiculo.urls')),
    path('usuarios/', include('usuario.urls')),
    path('despesas/', include('despesa.urls')),
    path('abastecimentos/', include('abastecimento.urls')),
    path('manutencoes/', include('manutencao.urls')),
    path('viagens/', include('viagem.urls')),
    path('cargas/', include('carga.urls')),
]
