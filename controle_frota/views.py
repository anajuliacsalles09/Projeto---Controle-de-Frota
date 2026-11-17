

from django.shortcuts import render
from django.urls import reverse

from veiculo.models import Veiculo
from viagem.models import Viagem
from abastecimento.models import Abastecimento
from manutencao.models import Manutencao
from usuario.models import Usuario
from carga.models import Carga
from despesa.models import Despesa


def dashboard(request):
    public_dashboard = not request.user.is_authenticated
    indicadores = []
    resumo = []
    atalhos = []
    modulos = (
        (Veiculo, 'Veículos cadastrados', 'Ver veículos', 'truck'),
        (Viagem, 'Viagens registradas', 'Ver viagens', 'road'),
        (Abastecimento, 'Abastecimentos', 'Ver abastecimentos', 'tint'),
        (Manutencao, 'Manutenções', 'Ver manutenções', 'wrench'),
        (Carga, 'Cargas registradas', 'Ver cargas', 'cubes'),
        (Despesa, 'Despesas registradas', 'Ver despesas', 'money'),
        (Usuario, 'Usuários cadastrados', 'Ver usuários', 'users'),
    )
    nomes_cadastro = {
        'veiculo': 'Cadastrar veículo',
        'viagem': 'Registrar viagem',
        'abastecimento': 'Registrar abastecimento',
        'manutencao': 'Registrar manutenção',
        'carga': 'Cadastrar carga',
        'despesa': 'Registrar despesa',
        'usuario': 'Cadastrar usuário',
    }
    for model, label, link_label, icon in modulos:
        app = model._meta.app_label
        name = model._meta.model_name
        if public_dashboard or request.user.has_perm(f'{app}.view_{name}'):
            item = {
                'label': label, 'total': model.objects.count(),
                'url': reverse(f'{name}_list'), 'link_label': link_label,
                'icon': icon,
            }
            if model in (Veiculo, Viagem, Abastecimento, Manutencao):
                indicadores.append(item)
            else:
                resumo.append(item)
        if request.user.has_perm(f'{app}.add_{name}'):
            atalhos.append({
                'label': nomes_cadastro[name], 'url': reverse(f'{name}_create'),
                'icon': icon,
            })

    context = {
        'indicadores': indicadores, 'resumo': resumo, 'atalhos': atalhos,
        'public_dashboard': public_dashboard,
    }
    if public_dashboard or request.user.has_perm('viagem.view_viagem'):
        context['viagens_recentes'] = Viagem.objects.select_related(
            'veiculo'
        ).order_by('-data_saida', '-pk')[:5]
    if public_dashboard or request.user.has_perm('despesa.view_despesa'):
        context['despesas_recentes'] = Despesa.objects.select_related(
            'viagem'
        ).order_by('-data', '-pk')[:4]

    return render(request, 'dashboard.html', context)
