from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required

from .models import Veiculo
from .forms import VeiculoForm


@login_required
@permission_required('veiculo.view_veiculo', raise_exception=True)
def veiculo_list(request):
    objetos = Veiculo.objects.all()

    return render(
        request,
        'veiculo/veiculo_list.html',
        {'objetos': objetos}
    )


@login_required
@permission_required('veiculo.add_veiculo', raise_exception=True)
def veiculo_create(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('veiculo_list')

    else:
        form = VeiculoForm()

    return render(
        request,
        'veiculo/veiculo_form.html',
        {'form': form}
    )


@login_required
@permission_required('veiculo.view_veiculo', raise_exception=True)
def veiculo_detail(request, pk):
    objeto = get_object_or_404(Veiculo, pk=pk)

    return render(
        request,
        'veiculo/veiculo_detail.html',
        {'objeto': objeto}
    )


@login_required
@permission_required('veiculo.change_veiculo', raise_exception=True)
def veiculo_update(request, pk):
    objeto = get_object_or_404(Veiculo, pk=pk)

    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=objeto)

        if form.is_valid():
            form.save()
            return redirect('veiculo_detail', pk=objeto.pk)

    else:
        form = VeiculoForm(instance=objeto)

    return render(
        request,
        'veiculo/veiculo_update.html',
        {
            'form': form,
            'objeto': objeto
        }
    )


@login_required
@permission_required('veiculo.delete_veiculo', raise_exception=True)
def veiculo_delete(request, pk):
    objeto = get_object_or_404(Veiculo, pk=pk)

    if request.method == 'POST':
        objeto.delete()
        return redirect('veiculo_list')

    return render(
        request,
        'veiculo/veiculo_delete.html',
        {'objeto': objeto}
    )