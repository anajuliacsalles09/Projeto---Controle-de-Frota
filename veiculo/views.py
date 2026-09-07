from django.shortcuts import render

from .models import Veiculo


def veiculo_list(request):
    objetos = Veiculo.objects.all()

    return render(request, 'veiculo/veiculo_list.html', {
        'objetos': objetos
    })


def veiculo_detail(request, id):
    veiculo = Veiculo.objects.get(id=id)

    return render(request, 'veiculo/veiculo_detail.html', {
        'veiculo': veiculo
    })


def veiculo_update(request, id):
    veiculo = Veiculo.objects.get(id=id)

    if request.method == 'POST':
        veiculo.placa = request.POST['placa']
        veiculo.modelo = request.POST['modelo']
        veiculo.marca = request.POST['marca']
        veiculo.ano = request.POST['ano']
        veiculo.quilometragem = request.POST['quilometragem']
        veiculo.status = request.POST['status']
        veiculo.capacidade_carga = request.POST['capacidade_carga']

        veiculo.save()

        return render(request, 'veiculo/veiculo_detail.html', {
            'veiculo': veiculo
        })

    return render(request, 'veiculo/veiculo_update.html', {
        'veiculo': veiculo
    })


def veiculo_delete(request, id):
    veiculo = Veiculo.objects.get(id=id)

    if request.method == 'POST':
        veiculo.delete()

        return render(request, 'veiculo/veiculo_list.html', {
            'objetos': Veiculo.objects.all()
        })

    return render(request, 'veiculo/veiculo_delete.html', {
        'veiculo': veiculo
    })