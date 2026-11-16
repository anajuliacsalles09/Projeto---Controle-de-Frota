
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

from .models import Usuario
from .forms import (
    UsuarioForm,
    UsuarioRegistroForm,
    UsuarioUpdateForm
)


def usuario_register(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UsuarioRegistroForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Conta criada com sucesso! Faça login para acessar.'
            )

            return redirect('login')
        else:
            messages.error(
                request,
                'Não foi possível criar a conta. Verifique os campos.'
            )

    else:
        form = UsuarioRegistroForm()

    return render(
        request,
        'usuario/usuario_register.html',
        {'form': form}
    )


@login_required
@permission_required('usuario.view_usuario', raise_exception=True)
def usuario_list(request):

    objetos = Usuario.objects.all().order_by('nome')

    quantidade_usuarios = objetos.count()

    quantidade_administradores = objetos.filter(
        tipo='ADMIN'
    ).count()

    quantidade_funcionarios = objetos.filter(
        tipo='FUNCIONARIO'
    ).count()

    return render(
        request,
        'usuario/usuario_list.html',
        {
            'objetos': objetos,
            'quantidade_usuarios': quantidade_usuarios,
            'quantidade_administradores': quantidade_administradores,
            'quantidade_funcionarios': quantidade_funcionarios
        }
    )


@login_required
@permission_required('usuario.add_usuario', raise_exception=True)
def usuario_create(request):

    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Usuário cadastrado com sucesso!'
            )

            return redirect('usuario_list')
        else:
            messages.error(
                request,
                'Não foi possível cadastrar. Verifique os campos.'
            )

    else:
        form = UsuarioForm()

    return render(
        request,
        'usuario/usuario_form.html',
        {'form': form}
    )


@login_required
@permission_required('usuario.view_usuario', raise_exception=True)
def usuario_detail(request, pk):

    objeto = get_object_or_404(Usuario, pk=pk)

    return render(
        request,
        'usuario/usuario_detail.html',
        {'objeto': objeto}
    )


@login_required
@permission_required('usuario.change_usuario', raise_exception=True)
def usuario_update(request, pk):

    objeto = get_object_or_404(Usuario, pk=pk)

    if request.method == 'POST':
        form = UsuarioUpdateForm(request.POST, instance=objeto)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Usuário atualizado com sucesso!'
            )

            return redirect('usuario_detail', pk=objeto.pk)
        else:
            messages.error(
                request,
                'Não foi possível atualizar. Verifique os campos.'
            )

    else:
        form = UsuarioUpdateForm(instance=objeto)

    return render(
        request,
        'usuario/usuario_form.html',
        {
            'form': form,
            'objeto': objeto
        }
    )


@login_required
@permission_required('usuario.delete_usuario', raise_exception=True)
def usuario_delete(request, pk):

    objeto = get_object_or_404(Usuario, pk=pk)

    if request.method == 'POST':
        objeto.delete()

        messages.success(
            request,
            'Usuário excluído com sucesso!'
        )

        return redirect('usuario_list')

    return render(
        request,
        'usuario/usuario_confirm_delete.html',
        {'objeto': objeto}
    )
