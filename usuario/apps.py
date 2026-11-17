from django.apps import AppConfig


class UsuarioConfig(AppConfig):
    name = 'usuario'

    def ready(self):
        from . import signals  # noqa: F401
