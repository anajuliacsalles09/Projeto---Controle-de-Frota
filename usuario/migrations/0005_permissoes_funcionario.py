from django.db import migrations


def configure_employee_permissions(apps, schema_editor):
    alias = schema_editor.connection.alias if schema_editor else 'default'
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    Usuario = apps.get_model('usuario', 'Usuario')
    group, _ = Group.objects.using(alias).get_or_create(name='Funcionario')
    permissions = []
    for app_label, actions in (
        ('abastecimento', ('add', 'view')),
        ('carga', ('view',)),
        ('despesa', ('add', 'view')),
        ('manutencao', ('add', 'view')),
        ('veiculo', ('view',)),
        ('viagem', ('add', 'view')),
    ):
        content_type, _ = ContentType.objects.using(alias).get_or_create(
            app_label=app_label, model=app_label,
        )
        # Em um banco novo, post_migrate ainda não criou as permissões.
        for action in actions:
            permission, _ = Permission.objects.using(alias).get_or_create(
                content_type=content_type, codename=f'{action}_{app_label}',
                defaults={'name': f'Can {action} {app_label}'},
            )
            permissions.append(permission)
    group.permissions.set(permissions)
    membership = Usuario.groups.through
    for user_id in Usuario.objects.using(alias).filter(
        tipo='FUNCIONARIO'
    ).values_list('pk', flat=True).iterator():
        membership.objects.using(alias).get_or_create(user_id=user_id, group_id=group.pk)


class Migration(migrations.Migration):
    dependencies = [
        ('usuario', '0004_usuario_tipo'),
        ('abastecimento', '0001_initial'),
        ('carga', '0002_initial'),
        ('despesa', '0002_initial'),
        ('manutencao', '0001_initial'),
        ('viagem', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(configure_employee_permissions, migrations.RunPython.noop),
    ]
