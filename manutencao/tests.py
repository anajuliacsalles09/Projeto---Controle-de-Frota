from django.test import TestCase
from manutencao.models import Manutencao
from veiculo.models import Veiculo


class MaintenanceHistoryTests(TestCase):
    def test_history_filters_vehicle_and_orders_newest_first(self):
        def vehicle(plate):
            return Veiculo.objects.create(placa=plate, modelo='Teste', marca='Teste', ano=2024, quilometragem=0, status='Ativo', capacidade_carga=1000)
        first = vehicle('AAA1234')
        second = vehicle('BBB1234')
        old = Manutencao.objects.create(veiculo=first, tipo='Revisao', descricao='Teste', valor=100, data='2026-10-01')
        new = Manutencao.objects.create(veiculo=first, tipo='Revisao', descricao='Teste', valor=200, data='2026-11-01')
        Manutencao.objects.create(veiculo=second, tipo='Revisao', descricao='Teste', valor=300, data='2026-11-02')
        self.assertEqual(list(Manutencao.consultar_historico(first)), [new, old])
        self.assertEqual(Manutencao.consultar_historico().count(), 3)

        from django.contrib.auth.models import User
        from django.urls import reverse
        admin = User.objects.create_superuser(username='history-admin', password='Test-admin-941!')
        self.client.force_login(admin)
        response = self.client.get(reverse('manutencao_list'), {'veiculo': first.pk})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['objetos']), [new, old])
        self.assertEqual(response.context['quantidade_manutencoes'], 2)
        self.assertEqual(response.context['valor_total'], 300)
