from django.shortcuts import render, redirect, get_object_or_404

from .models import Carga
from .forms import CargaForm


def carga_list(request):
    objetos = Carga.objects.all()

    return render(request, 'carga/carga_list.html', {
        'objetos': objetos
    })


def carga_create(request):
    if request.method == 'POST':
        form = CargaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('carga_list')

    else:
        form = CargaForm()

    return render(request, 'carga/carga_create.html', {
        'form': form
    })


def carga_detail(request, pk):
    objeto = get_object_or_404(Carga, pk=pk)

    return render(request, 'carga/carga_detail.html', {
        'objeto': objeto
    })


def carga_update(request, pk):
    objeto = get_object_or_404(Carga, pk=pk)

    if request.method == 'POST':
        form = CargaForm(request.POST, instance=objeto)

        if form.is_valid():
            form.save()
            return redirect('carga_detail', pk=objeto.pk)

    else:
        form = CargaForm(instance=objeto)

    return render(request, 'carga/carga_update.html', {
        'form': form,
        'objeto': objeto
    })


def carga_delete(request, pk):
    objeto = get_object_or_404(Carga, pk=pk)

    if request.method == 'POST':
        objeto.delete()
        return redirect('carga_list')

    return render(request, 'carga/carga_delete.html', {
        'objeto': objeto
    })