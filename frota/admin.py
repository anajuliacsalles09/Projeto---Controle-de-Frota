from django.contrib import admin
from .models import Usuario, Viagem, Veiculo, Abastecimento, Manutencao


admin.site.register(Usuario)
admin.site.register(Viagem)
admin.site.register(Veiculo)
admin.site.register(Abastecimento)
admin.site.register(Manutencao)