from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import Usuario
from .forms import UsuarioForm


def usuario_list(request):
    objetos = Usuario.objects.all()

    return render(
        request,
        'usuario/usuario_list.html',
        {'objetos': objetos}
    )


def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['cpf'],
                password='123456'
            )

            usuario = form.save(commit=False)
            usuario.user_ptr = user
            usuario.save()

            return redirect('usuario_list')

    else:
        form = UsuarioForm()

    return render(
        request,
        'usuario/usuario_form.html',
        {'form': form}
    )


def usuario_detail(request, pk):
    objeto = Usuario.objects.get(pk=pk)

    return render(
        request,
        'usuario/usuario_detail.html',
        {'objeto': objeto}
    )


def usuario_update(request, pk):
    objeto = Usuario.objects.get(pk=pk)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=objeto)

        if form.is_valid():
            usuario = form.save()

            usuario.user_ptr.username = form.cleaned_data['cpf']
            usuario.user_ptr.save()

            return redirect('usuario_detail', pk=objeto.pk)

    else:
        form = UsuarioForm(instance=objeto)

    return render(
        request,
        'usuario/usuario_form.html',
        {
            'form': form,
            'objeto': objeto
        }
    )


def usuario_delete(request, pk):
    objeto = Usuario.objects.get(pk=pk)

    if request.method == 'POST':
        user = objeto.user_ptr

        objeto.delete()
        user.delete()

        return redirect('usuario_list')

    return render(
        request,
        'usuario/usuario_confirm_delete.html',
        {'objeto': objeto}
    )