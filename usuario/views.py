from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Usuario
from .forms import UsuarioForm


def usuario_list(request):
    objetos = Usuario.objects.all()
    return render(request, 'usuario/usuario_list.html', {'objetos': objetos})


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

            return render(
                request,
                'usuario/usuario_list.html',
                {'objetos': Usuario.objects.all()}
            )
    else:
        form = UsuarioForm()

    return render(request, 'usuario/usuario_form.html', {'form': form})