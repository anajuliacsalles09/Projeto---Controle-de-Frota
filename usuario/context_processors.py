from .permissions import is_administrator


def account_permissions(request):
    return {
        'can_register_users': is_administrator(request.user)
        and request.user.has_perm('usuario.add_usuario'),
    }
