from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from usuario.models import Usuario
from veiculo.models import Veiculo
from viagem.models import Viagem
from carga.models import Carga
from despesa.models import Despesa
from abastecimento.models import Abastecimento
from manutencao.models import Manutencao


class CompleteCrudTests(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username='audit-admin', password='Audit-admin-753!')
        self.driver = Usuario.objects.create(username='audit-driver', nome='Motorista', numero=1, tipo='FUNCIONARIO')
        self.vehicle = Veiculo.objects.create(placa='ABC1234', modelo='Caminhao', marca='Teste', ano=2024, quilometragem=1000, status='Ativo', capacidade_carga=1000)
        self.trip = Viagem.objects.create(usuario=self.driver, veiculo=self.vehicle, origem='Salvador', destino='Feira', data_saida='2026-11-17', data_retorno='2026-11-18', distancia=100, valor_frete=1000, status='Concluida')
        self.cases = [
            ('usuario', Usuario, {'username': 'audit-new-user', 'nome': 'Novo usuario', 'email': 'audit@example.com', 'cpf': '12345678901', 'telefone': '71999999999', 'rua': 'Rua A', 'bairro': 'Centro', 'cep': '40000000', 'numero': 10, 'logradouro': 'Rua', 'tipo': 'FUNCIONARIO', 'password1': 'K7!vQ2#rL9@xZ4', 'password2': 'K7!vQ2#rL9@xZ4'}, 'nome', 'Usuario editado'),
            ('veiculo', Veiculo, {'placa': 'DEF5678', 'modelo': 'Novo veiculo', 'marca': 'Teste', 'ano': 2024, 'quilometragem': 1000, 'status': 'Ativo', 'capacidade_carga': 1000}, 'modelo', 'Veiculo editado'),
            ('viagem', Viagem, {'usuario': self.driver.pk, 'veiculo': self.vehicle.pk, 'origem': 'Origem teste', 'destino': 'Destino teste', 'data_saida': '2026-11-17', 'data_retorno': '2026-11-18', 'km_saida': 1000, 'km_chegada': 1200, 'valor_frete': 1000, 'status': 'Concluida'}, 'origem', 'Origem editada'),
            ('carga', Carga, {'viagem': self.trip.pk, 'descricao': 'Nova carga', 'peso': 100, 'valor': 500, 'observacao': 'Teste'}, 'descricao', 'Carga editada'),
            ('despesa', Despesa, {'viagem': self.trip.pk, 'tipo': 'Pedagio', 'descricao': 'Nova despesa', 'valor': 50, 'data': '2026-11-17'}, 'descricao', 'Despesa editada'),
            ('abastecimento', Abastecimento, {'veiculo': self.vehicle.pk, 'litros': 100, 'valor': 600, 'data': '2026-11-17', 'tipo_combustivel': 'Diesel'}, 'tipo_combustivel', 'Diesel S10'),
            ('manutencao', Manutencao, {'veiculo': self.vehicle.pk, 'tipo': 'Revisao', 'descricao': 'Nova manutencao', 'data': '2026-11-17', 'valor': 200}, 'descricao', 'Manutencao editada'),
        ]

    def test_seven_complete_cruds_and_invalid_submissions(self):
        self.client.force_login(self.admin)
        for name, model, payload, changed_field, changed_value in self.cases:
            with self.subTest(module=name):
                create_url = reverse(name + '_create')
                response = self.client.get(create_url)
                self.assertEqual(response.status_code, 200)
                before = set(model.objects.values_list('pk', flat=True))
                invalid = self.client.post(create_url, {})
                self.assertEqual(invalid.status_code, 200)
                self.assertTrue(invalid.context['form'].errors)
                self.assertEqual(set(model.objects.values_list('pk', flat=True)), before)
                response = self.client.post(create_url, payload)
                self.assertEqual(response.status_code, 302, response.context['form'].errors if response.status_code == 200 else '')
                item = model.objects.exclude(pk__in=before).get()
                self.assertEqual(getattr(item, changed_field), payload[changed_field])
                self.assertEqual(self.client.get(reverse(name + '_list')).status_code, 200)
                detail = self.client.get(reverse(name + '_detail', args=[item.pk]))
                self.assertEqual(detail.status_code, 200)
                self.assertContains(detail, str(payload[changed_field]))
                edit_url = reverse(name + '_update', args=[item.pk])
                self.assertEqual(self.client.get(edit_url).status_code, 200)
                response = self.client.post(edit_url, {**payload, changed_field: changed_value})
                self.assertEqual(response.status_code, 302)
                item.refresh_from_db()
                self.assertEqual(getattr(item, changed_field), changed_value)
                delete_url = reverse(name + '_delete', args=[item.pk])
                self.assertEqual(self.client.get(delete_url).status_code, 200)
                self.assertTrue(model.objects.filter(pk=item.pk).exists())
                response = self.client.post(delete_url)
                self.assertEqual(response.status_code, 302)
                self.assertFalse(model.objects.filter(pk=item.pk).exists())
                self.assertEqual(self.client.get(reverse(name + '_detail', args=[item.pk])).status_code, 404)

    def test_anonymous_and_unprivileged_accounts_cannot_access_cruds(self):
        restricted = User.objects.create_user(username='audit-restricted')
        for authenticated in (False, True):
            if authenticated:
                self.client.force_login(restricted)
            for name, model, payload, changed_field, changed_value in self.cases:
                for action in ('list', 'create', 'detail', 'update', 'delete'):
                    with self.subTest(authenticated=authenticated, module=name, action=action):
                        args = [999999] if action in ('detail', 'update', 'delete') else []
                        url = reverse(name + '_' + action, args=args)
                        self.assertEqual(self.client.get(url).status_code, 403 if authenticated else 302)
                        if action in ('create', 'update', 'delete'):
                            self.assertEqual(self.client.post(url, payload).status_code, 403 if authenticated else 302)

    def test_login_logout_and_employee_restrictions(self):
        self.admin.set_password('Audit-admin-753!')
        self.admin.save()
        response = self.client.post(reverse('login'), {'username': self.admin.username, 'password': 'Audit-admin-753!'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.get(reverse('dashboard')).status_code, 200)
        self.assertEqual(self.client.post(reverse('logout')).status_code, 302)
        self.assertNotIn('_auth_user_id', self.client.session)
        self.client.force_login(self.driver)
        for name in ('veiculo', 'viagem', 'carga', 'despesa', 'abastecimento', 'manutencao'):
            self.assertEqual(self.client.get(reverse(name + '_list')).status_code, 200)
        self.assertEqual(self.client.get(reverse('usuario_list')).status_code, 403)
        self.assertEqual(self.client.get(reverse('veiculo_create')).status_code, 403)
        self.assertEqual(self.client.get(reverse('usuario_create')).status_code, 403)
        self.assertEqual(self.client.post(reverse('viagem_delete', args=[self.trip.pk])).status_code, 403)
