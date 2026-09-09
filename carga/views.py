from django.shortcuts import render, redirect

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

    return render(request, 'carga/carga_form.html', {
        'form': form
    })
