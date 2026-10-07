from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required

from .models import Usuario
from .forms import UsuarioForm


@login_required
@permission_required('usuario.view_usuario', raise_exception=True)
def usuario_list(request):
    objetos = Usuario.objects.all()

    return render(
        request,
        'usuario/usuario_list.html',
        {'objetos': objetos}
    )


@login_required
@permission_required('usuario.add_usuario', raise_exception=True)
def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

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
    objeto = Usuario.objects.get(pk=pk)

    return render(
        request,
        'usuario/usuario_detail.html',
        {'objeto': objeto}
    )


@login_required
@permission_required('usuario.change_usuario', raise_exception=True)
def usuario_update(request, pk):
    objeto = Usuario.objects.get(pk=pk)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=objeto)

        if form.is_valid():
            form.save()
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


@login_required
@permission_required('usuario.delete_usuario', raise_exception=True)
def usuario_delete(request, pk):
    objeto = Usuario.objects.get(pk=pk)

    if request.method == 'POST':
        objeto.delete()
        return redirect('usuario_list')

    return render(
        request,
        'usuario/usuario_confirm_delete.html',
        {'objeto': objeto}
    )