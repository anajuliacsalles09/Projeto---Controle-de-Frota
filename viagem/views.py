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
