from django.shortcuts import render, redirect, get_object_or_404

from .models import Abastecimento
from .forms import AbastecimentoForm


def abastecimento_list(request):
    objetos = Abastecimento.objects.all()

    return render(request, 'abastecimento/abastecimento_list.html', {
        'objetos': objetos
    })


def abastecimento_create(request):
    if request.method == 'POST':
        form = AbastecimentoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('abastecimento_list')

    else:
        form = AbastecimentoForm()

    return render(request, 'abastecimento/abastecimento_form.html', {
        'form': form
    })


def abastecimento_detail(request, pk):
    objeto = get_object_or_404(Abastecimento, pk=pk)

    return render(request, 'abastecimento/abastecimento_detail.html', {
        'objeto': objeto
    })


def abastecimento_update(request, pk):
    objeto = get_object_or_404(Abastecimento, pk=pk)

    if request.method == 'POST':
        form = AbastecimentoForm(request.POST, instance=objeto)

        if form.is_valid():
            form.save()
            return redirect('abastecimento_detail', pk=objeto.pk)

    else:
        form = AbastecimentoForm(instance=objeto)

    return render(request, 'abastecimento/abastecimento_update.html', {
        'form': form,
        'objeto': objeto
    })


def abastecimento_delete(request, pk):
    objeto = get_object_or_404(Abastecimento, pk=pk)

    if request.method == 'POST':
        objeto.delete()
        return redirect('abastecimento_list')

    return render(request, 'abastecimento/abastecimento_delete.html', {
        'objeto': objeto
    })