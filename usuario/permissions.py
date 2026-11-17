"""Grupo padrão e permissões operacionais dos funcionários."""

from django.contrib.auth.models import Group, Permission
from django.db.models import Q


EMPLOYEE_GROUP = 'Funcionario'
EMPLOYEE_PERMISSIONS = (
    ('abastecimento', 'add_abastecimento'),
    ('abastecimento', 'view_abastecimento'),
    ('carga', 'view_carga'),
    ('despesa', 'add_despesa'),
    ('despesa', 'view_despesa'),
    ('manutencao', 'add_manutencao'),
    ('manutencao', 'view_manutencao'),
    ('veiculo', 'view_veiculo'),
    ('viagem', 'add_viagem'),
    ('viagem', 'view_viagem'),
)


def employee_group(using='default'):
    group, created = Group.objects.using(using).get_or_create(name=EMPLOYEE_GROUP)
    if created:
        query = Q()
        for app_label, codename in EMPLOYEE_PERMISSIONS:
            query |= Q(content_type__app_label=app_label, codename=codename)
        group.permissions.set(Permission.objects.using(using).filter(query))
    return group


def sync_employee_group(user, using='default'):
    if user.tipo == 'FUNCIONARIO':
        user.groups.add(employee_group(using))
    else:
        user.groups.remove(*user.groups.filter(name=EMPLOYEE_GROUP))
