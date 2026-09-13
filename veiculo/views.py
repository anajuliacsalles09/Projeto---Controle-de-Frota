from django.shortcuts import render, redirect, get_object_or_404

from .models import Veiculo
from .forms import VeiculoForm


def veiculo_list(request):
    objetos = Veiculo.objects.all()

    return render(request, 'veiculo/veiculo_list.html', {
        'objetos': objetos
    })


def veiculo_create(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('veiculo_list')

    else:
        form = VeiculoForm()

    return render(request, 'veiculo/veiculo_create.html', {
        'form': form
    })


def veiculo_detail(request, pk):
    objeto = get_object_or_404(Veiculo, pk=pk)

    return render(request, 'veiculo/veiculo_detail.html', {
        'objeto': objeto
    })


def veiculo_update(request, pk):
    objeto = get_object_or_404(Veiculo, pk=pk)

    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=objeto)

        if form.is_valid():
            form.save()
            return redirect('veiculo_detail', pk=objeto.pk)

    else:
        form = VeiculoForm(instance=objeto)

    return render(request, 'veiculo/veiculo_update.html', {
        'form': form,
        'objeto': objeto
    })


def veiculo_delete(request, pk):
    objeto = get_object_or_404(Veiculo, pk=pk)

    if request.method == 'POST':
        objeto.delete()
        return redirect('veiculo_list')

    return render(request, 'veiculo/veiculo_delete.html', {
        'objeto': objeto
    })
