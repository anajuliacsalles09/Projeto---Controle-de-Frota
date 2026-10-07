from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

from .models import Carga
from .forms import CargaForm


@login_required
@permission_required('carga.view_carga', raise_exception=True)
def carga_list(request):
    objetos = Carga.objects.all()

    return render(request, 'carga/carga_list.html', {
        'objetos': objetos
    })


@login_required
@permission_required('carga.add_carga', raise_exception=True)
def carga_create(request):
    if request.method == 'POST':
        form = CargaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('carga_list')
    else:
        form = CargaForm()

    return render(request, 'carga/carga_form.html', {
        'form': form
    })


@login_required
@permission_required('carga.view_carga', raise_exception=True)
def carga_detail(request, pk):
    objeto = get_object_or_404(Carga, pk=pk)

    return render(request, 'carga/carga_detail.html', {
        'objeto': objeto
    })


@login_required
@permission_required('carga.change_carga', raise_exception=True)
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


@login_required
@permission_required('carga.delete_carga', raise_exception=True)
def carga_delete(request, pk):
    objeto = get_object_or_404(Carga, pk=pk)

    if request.method == 'POST':
        objeto.delete()
        return redirect('carga_list')

    return render(request, 'carga/carga_delete.html', {
        'objeto': objeto
    })