from django.contrib import admin
from .models import Usuario
from .permissions import is_administrator, sync_employee_group


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return is_administrator(request.user) and super().has_add_permission(request)

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        # O admin salva os grupos depois de post_save: mantenha o grupo padrão.
        sync_employee_group(form.instance, using=form.instance._state.db)
