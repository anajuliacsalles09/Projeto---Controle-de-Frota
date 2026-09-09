from django.shortcuts import render
from .models import Manutencao
from .forms import ManutencaoForm


def manutencao_list(request):
    objetos = Manutencao.objects.all()
    return render(
        request,
        'manutencao/manutencao_list.html',
        {'objetos': objetos}
    )


def manutencao_create(request):
    if request.method == 'POST':
        form = ManutencaoForm(request.POST)

        if form.is_valid():
            form.save()

            return render(
                request,
                'manutencao/manutencao_list.html',
                {'objetos': Manutencao.objects.all()}
            )
    else:
        form = ManutencaoForm()

    return render(
        request,
        'manutencao/manutencao_form.html',
        {'form': form}
    )