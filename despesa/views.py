from django.shortcuts import render
from .models import Despesa
from .forms import DespesaForm


def despesa_list(request):
    objetos = Despesa.objects.all()
    return render(request, 'despesa/despesa_list.html', {'objetos': objetos})


def despesa_create(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)

        if form.is_valid():
            form.save()

            return render(
                request,
                'despesa/despesa_list.html',
                {'objetos': Despesa.objects.all()}
            )
    else:
        form = DespesaForm()

    return render(request, 'despesa/despesa_form.html', {'form': form})