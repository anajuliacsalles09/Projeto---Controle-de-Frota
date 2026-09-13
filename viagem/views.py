from django.shortcuts import render, redirect

from django.shortcuts import render, redirect

from .models import Viagem
from .forms import ViagemForm


def viagem_list(request):
    objetos = Viagem.objects.all()

    return render(request, 'viagem/viagem_list.html', {
        'objetos': objetos
    })


def viagem_create(request):
    if request.method == 'POST':
        form = ViagemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('viagem_list')

    else:
        form = ViagemForm()

    return render(request, 'viagem/viagem_form.html', {
        'form': form
    })

def viagem_detail(request, pk):
    objeto = Viagem.objects.get(pk=pk)

    return render(request, 'viagem/viagem_detail.html', {
        'objeto': objeto
    })

def viagem_update(request, pk):
    objeto = Viagem.objects.get(pk=pk)

    if request.method == 'POST':
        form = ViagemForm(request.POST, instance=objeto)

        if form.is_valid():
            form.save()
            return redirect('viagem_detail', pk=objeto.pk)

    else:
        form = ViagemForm(instance=objeto)

    return render(request, 'viagem/viagem_form.html', {
        'form': form
    })

def viagem_delete(request, pk):
    objeto = Viagem.objects.get(pk=pk)

    if request.method == 'POST':
        objeto.delete()
        return redirect('viagem_list')

    return render(request, 'viagem/viagem_confirm_delete.html', {
        'objeto': objeto
    })