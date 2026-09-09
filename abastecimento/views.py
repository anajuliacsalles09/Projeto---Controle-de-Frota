from django.shortcuts import render
from .models import Abastecimento
from .forms import AbastecimentoForm


def abastecimento_list(request):
    objetos = Abastecimento.objects.all()
    return render(
        request,
        'abastecimento/abastecimento_list.html',
        {'objetos': objetos}
    )


def abastecimento_create(request):
    if request.method == 'POST':
        form = AbastecimentoForm(request.POST)

        if form.is_valid():
            form.save()

            return render(
                request,
                'abastecimento/abastecimento_list.html',
                {'objetos': Abastecimento.objects.all()}
            )
    else:
        form = AbastecimentoForm()

    return render(
        request,
        'abastecimento/abastecimento_form.html',
        {'form': form}
    )