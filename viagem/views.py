
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Sum

from .models import Viagem
from .forms import ViagemForm


@login_required
@permission_required('viagem.view_viagem', raise_exception=True)
def viagem_list(request):
    objetos = Viagem.objects.all()

    quantidade_viagens = objetos.count()

    viagens_em_andamento = objetos.filter(
        status__iexact='Em andamento'
    ).count()

    total_fretes = Viagem.objects.aggregate(
        total=Sum('valor_frete')
    )['total'] or 0

    total_resultado = Viagem.objects.aggregate(
        total=Sum('valor_resultado')
    )['total'] or 0

    return render(request, 'viagem/viagem_list.html', {
        'objetos': objetos,
        'quantidade_viagens': quantidade_viagens,
        'viagens_em_andamento': viagens_em_andamento,
        'total_fretes': total_fretes,
        'total_resultado': total_resultado
    })


@login_required
@permission_required('viagem.add_viagem', raise_exception=True)
def viagem_create(request):
    if request.method == 'POST':
        form = ViagemForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Viagem cadastrada com sucesso!')
            return redirect('viagem_list')
        else:
            messages.error(request, 'Não foi possível cadastrar. Verifique os campos.')
    else:
        form = ViagemForm()

    return render(request, 'viagem/viagem_form.html', {'form': form})


@login_required
@permission_required('viagem.view_viagem', raise_exception=True)
def viagem_detail(request, pk):
    objeto = get_object_or_404(Viagem, pk=pk)
    return render(request, 'viagem/viagem_detail.html', {'objeto': objeto})


@login_required
@permission_required('viagem.change_viagem', raise_exception=True)
def viagem_update(request, pk):
    objeto = get_object_or_404(Viagem, pk=pk)

    if request.method == 'POST':
        form = ViagemForm(request.POST, instance=objeto)

        if form.is_valid():
            form.save()
            messages.success(request, 'Viagem atualizada com sucesso!')
            return redirect('viagem_detail', pk=objeto.pk)
        else:
            messages.error(request, 'Não foi possível atualizar. Verifique os campos.')
    else:
        form = ViagemForm(instance=objeto)

    return render(request, 'viagem/viagem_form.html', {
        'form': form,
        'objeto': objeto
    })


@login_required
@permission_required('viagem.delete_viagem', raise_exception=True)
def viagem_delete(request, pk):
    objeto = get_object_or_404(Viagem, pk=pk)

    if request.method == 'POST':
        objeto.delete()
        messages.success(request, 'Viagem excluída com sucesso!')
        return redirect('viagem_list')

    return render(request, 'viagem/viagem_confirm_delete.html', {
        'objeto': objeto
    })
