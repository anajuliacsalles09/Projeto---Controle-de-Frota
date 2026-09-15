from django.shortcuts import render, redirect, get_object_or_404

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
            return redirect('manutencao_list')

    else:
        form = ManutencaoForm()

    return render(
        request,
        'manutencao/manutencao_form.html',
        {'form': form}
    )


def manutencao_detail(request, pk):
    objeto = get_object_or_404(Manutencao, pk=pk)

    return render(
        request,
        'manutencao/manutencao_detail.html',
        {'objeto': objeto}
    )


def manutencao_update(request, pk):
    objeto = get_object_or_404(Manutencao, pk=pk)

    if request.method == 'POST':
        form = ManutencaoForm(request.POST, instance=objeto)

        if form.is_valid():
            form.save()
            return redirect('manutencao_detail', pk=objeto.pk)

    else:
        form = ManutencaoForm(instance=objeto)

    return render(
        request,
        'manutencao/manutencao_update.html',
        {
            'form': form,
            'objeto': objeto
        }
    )


def manutencao_delete(request, pk):
    objeto = get_object_or_404(Manutencao, pk=pk)

    if request.method == 'POST':
        objeto.delete()
        return redirect('manutencao_list')

    return render(
        request,
        'manutencao/manutencao_delete.html',
        {'objeto': objeto}
    )