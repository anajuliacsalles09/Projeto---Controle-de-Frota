
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Sum

from .models import Abastecimento
from .forms import AbastecimentoForm


@login_required
@permission_required('abastecimento.view_abastecimento', raise_exception=True)
def abastecimento_list(request):
    objetos = Abastecimento.objects.all()

    quantidade_abastecimentos = objetos.count()

    total_litros = Abastecimento.objects.aggregate(
        total=Sum('litros')
    )['total'] or 0

    valor_total = Abastecimento.objects.aggregate(
        total=Sum('valor')
    )['total'] or 0

    return render(request, 'abastecimento/abastecimento_list.html', {
        'objetos': objetos,
        'quantidade_abastecimentos': quantidade_abastecimentos,
        'total_litros': total_litros,
        'valor_total': valor_total
    })


@login_required
@permission_required('abastecimento.add_abastecimento', raise_exception=True)
def abastecimento_create(request):
    if request.method == 'POST':
        form = AbastecimentoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Abastecimento cadastrado com sucesso!')
            return redirect('abastecimento_list')
        else:
            messages.error(request, 'Não foi possível cadastrar. Verifique os campos.')
    else:
        form = AbastecimentoForm()

    return render(request, 'abastecimento/abastecimento_form.html', {
        'form': form
    })


@login_required
@permission_required('abastecimento.view_abastecimento', raise_exception=True)
def abastecimento_detail(request, pk):
    objeto = get_object_or_404(Abastecimento, pk=pk)

    return render(request, 'abastecimento/abastecimento_detail.html', {
        'objeto': objeto
    })


@login_required
@permission_required('abastecimento.change_abastecimento', raise_exception=True)
def abastecimento_update(request, pk):
    objeto = get_object_or_404(Abastecimento, pk=pk)

    if request.method == 'POST':
        form = AbastecimentoForm(request.POST, instance=objeto)

        if form.is_valid():
            form.save()
            messages.success(request, 'Abastecimento atualizado com sucesso!')
            return redirect('abastecimento_detail', pk=objeto.pk)
        else:
            messages.error(request, 'Não foi possível atualizar. Verifique os campos.')
    else:
        form = AbastecimentoForm(instance=objeto)

    return render(request, 'abastecimento/abastecimento_update.html', {
        'form': form,
        'objeto': objeto
    })


@login_required
@permission_required('abastecimento.delete_abastecimento', raise_exception=True)
def abastecimento_delete(request, pk):
    objeto = get_object_or_404(Abastecimento, pk=pk)

    if request.method == 'POST':
        objeto.delete()
        messages.success(request, 'Abastecimento excluído com sucesso!')
        return redirect('abastecimento_list')

    return render(request, 'abastecimento/abastecimento_delete.html', {
        'objeto': objeto
    })
