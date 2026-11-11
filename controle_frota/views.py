
from django.shortcuts import render

from veiculo.models import Veiculo
from viagem.models import Viagem
from abastecimento.models import Abastecimento
from manutencao.models import Manutencao
from usuario.models import Usuario
from carga.models import Carga
from despesa.models import Despesa


def dashboard(request):
    context = {
        'total_veiculos': Veiculo.objects.count(),
        'total_viagens': Viagem.objects.count(),
        'total_abastecimentos': Abastecimento.objects.count(),
        'total_manutencoes': Manutencao.objects.count(),
        'total_usuarios': Usuario.objects.count(),
        'total_cargas': Carga.objects.count(),
        'total_despesas': Despesa.objects.count(),
    }

    return render(request, 'dashboard.html', context)
