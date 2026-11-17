
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.db.models import F, Q
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.urls import reverse
from django.utils.http import urlencode, url_has_allowed_host_and_scheme
from django.views.decorators.http import require_GET

from .models import Usuario
from .permissions import is_administrator
from .forms import (
    UsuarioForm,
    UsuarioUpdateForm
)


def _proximo_destino(request):
    destino = request.GET.get('next', '') or request.POST.get('next', '')
    if url_has_allowed_host_and_scheme(
        destino, allowed_hosts={request.get_host()}, require_https=request.is_secure()
    ):
        return destino
    return ''


def _url_acesso(nome, destino, **kwargs):
    url = reverse(nome, kwargs=kwargs or None)
    return f'{url}?{urlencode({"next": destino})}' if destino else url


class ContaLoginView(LoginView):
    template_name = 'usuario/login.html'
    redirect_authenticated_user = True


@require_GET
def escolher_acesso(request, perfil=None):
    # Mantem links antigos funcionando com o formulario unico.
    return redirect(_url_acesso('login', _proximo_destino(request)))


@login_required
@permission_required('usuario.add_usuario', raise_exception=True)
def usuario_register(request):
    if not is_administrator(request.user):
        raise PermissionDenied
    # Compatibilidade com o endereço antigo, agora sem cadastro público.
    return redirect('usuario_create')


@login_required
@permission_required('usuario.view_usuario', raise_exception=True)
def usuario_list(request):

    objetos = User.objects.annotate(
        nome=F('usuario__nome'),
        cpf=F('usuario__cpf'),
        tipo=F('usuario__tipo'),
        perfil_id=F('usuario__pk'),
    ).order_by('nome', 'username')
    administradores = Q(is_superuser=True) | Q(usuario__tipo='ADMIN')
    quantidade_usuarios = objetos.count()
    quantidade_administradores = objetos.filter(administradores).count()
    quantidade_funcionarios = objetos.exclude(administradores).count()

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
    if not is_administrator(request.user):
        raise PermissionDenied

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
