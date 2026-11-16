
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from .models import Manutencao
from .forms import ManutencaoForm


@login_required
@permission_required('manutencao.view_manutencao', raise_exception=True)
def manutencao_list(request):
    objetos = Manutencao.objects.all()

    quantidade_manutencoes = objetos.count()
    valor_total = sum(manutencao.valor for manutencao in objetos)

    return render(
        request,
        'manutencao/manutencao_list.html',
        {
            'objetos': objetos,
            'quantidade_manutencoes': quantidade_manutencoes,
            'valor_total': valor_total
        }
    )


@login_required
@permission_required('manutencao.add_manutencao', raise_exception=True)
def manutencao_create(request):
    if request.method == 'POST':
        form = ManutencaoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Manutenção cadastrada com sucesso!')
            return redirect('manutencao_list')
        else:
            messages.error(request, 'Não foi possível cadastrar. Verifique os campos.')
    else:
        form = ManutencaoForm()

    return render(
        request,
        'manutencao/manutencao_form.html',
        {'form': form}
    )


@login_required
@permission_required('manutencao.view_manutencao', raise_exception=True)
def manutencao_detail(request, pk):
    objeto = get_object_or_404(Manutencao, pk=pk)

    return render(
        request,
        'manutencao/manutencao_detail.html',
        {'objeto': objeto}
    )


@login_required
@permission_required('manutencao.change_manutencao', raise_exception=True)
def manutencao_update(request, pk):
    objeto = get_object_or_404(Manutencao, pk=pk)

    if request.method == 'POST':
        form = ManutencaoForm(request.POST, instance=objeto)

        if form.is_valid():
            form.save()
            messages.success(request, 'Manutenção atualizada com sucesso!')
            return redirect('manutencao_detail', pk=objeto.pk)
        else:
            messages.error(request, 'Não foi possível atualizar. Verifique os campos.')
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


@login_required
@permission_required('manutencao.delete_manutencao', raise_exception=True)
def manutencao_delete(request, pk):
    objeto = get_object_or_404(Manutencao, pk=pk)

    if request.method == 'POST':
        objeto.delete()
        messages.success(request, 'Manutenção excluída com sucesso!')
        return redirect('manutencao_list')

    return render(
        request,
        'manutencao/manutencao_delete.html',
        {'objeto': objeto}
    )
