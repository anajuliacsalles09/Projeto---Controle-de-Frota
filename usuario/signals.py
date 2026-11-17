from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Usuario
from .permissions import sync_employee_group


@receiver(post_save, sender=Usuario, dispatch_uid='usuario.employee_permissions')
def assign_employee_permissions(sender, instance, raw=False, using='default', **kwargs):
    if raw:
        return
    sync_employee_group(instance, using)
