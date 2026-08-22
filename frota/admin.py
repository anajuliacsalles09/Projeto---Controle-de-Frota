from django.contrib import admin
from .models import Usuario, Viagem, Veiculo, Abastecimento, Manutencao, Carga, Despesa


admin.site.register(Usuario)
admin.site.register(Viagem)
admin.site.register(Veiculo)
admin.site.register(Abastecimento)
admin.site.register(Manutencao)
admin.site.register(Carga)
admin.site.register(Despesa)