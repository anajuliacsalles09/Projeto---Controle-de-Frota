from django.shortcuts import render, redirect, get_object_or_404

from .models import Despesa
from .forms import DespesaForm


def despesa_list(request):
    objetos = Despesa.objects.all()

    return render(request, 'despesa/despesa_list.html', {
        'objetos': objetos
    })


def despesa_create(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('despesa_list')

    else:
        form = DespesaForm()

    return render(request, 'despesa/despesa_form.html', {
        'form': form
    })


def despesa_detail(request, pk):
    objeto = get_object_or_404(Despesa, pk=pk)

    return render(request, 'despesa/despesa_detail.html', {
        'objeto': objeto
    })


def despesa_update(request, pk):
    objeto = get_object_or_404(Despesa, pk=pk)

    if request.method == 'POST':
        form = DespesaForm(request.POST, instance=objeto)

        if form.is_valid():
            form.save()
            return redirect('despesa_detail', pk=objeto.pk)

    else:
        form = DespesaForm(instance=objeto)

    return render(request, 'despesa/despesa_update.html', {
        'form': form,
        'objeto': objeto
    })


def despesa_delete(request, pk):
    objeto = get_object_or_404(Despesa, pk=pk)

    if request.method == 'POST':
        objeto.delete()
        return redirect('despesa_list')

    return render(request, 'despesa/despesa_delete.html', {
        'objeto': objeto
    })