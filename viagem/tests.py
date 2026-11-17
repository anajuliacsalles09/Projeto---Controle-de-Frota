from django.test import TestCase
from viagem.forms import ViagemForm
from viagem.models import Viagem
from usuario.models import Usuario
from veiculo.models import Veiculo


class TripOdometerTests(TestCase):
    def setUp(self):
        self.driver = Usuario.objects.create(username='driver', numero=1)
        self.vehicle = Veiculo.objects.create(placa='ABC1234', modelo='Teste', marca='Teste', ano=2024, quilometragem=0, status='Ativo', capacidade_carga=1000)
        self.data = {'usuario': self.driver.pk, 'veiculo': self.vehicle.pk, 'origem': 'Salvador', 'destino': 'Feira de Santana', 'data_saida': '2026-11-17', 'data_retorno': '2026-11-18', 'valor_frete': 1000, 'valor_resultado': 500, 'status': 'Concluida'}

    def test_saves_difference_ignoring_submitted_distance(self):
        form = ViagemForm(data={**self.data, 'km_saida': '1000.10', 'km_chegada': '1231.25', 'distancia': '1'})
        self.assertTrue(form.is_valid(), form.errors)
        trip = form.save()
        trip.refresh_from_db()
        self.assertEqual(trip.distancia, 231.15)
        self.assertEqual(float(trip.km_saida), 1000.10)
        self.assertEqual(float(trip.km_chegada), 1231.25)

    def test_rejects_arrival_before_departure(self):
        form = ViagemForm(data={**self.data, 'km_saida': '1000', 'km_chegada': '999'})
        self.assertFalse(form.is_valid())
        self.assertIn('km_chegada', form.errors)

    def test_rejects_negative_odometer(self):
        form = ViagemForm(data={**self.data, 'km_saida': '-1', 'km_chegada': '10'})
        self.assertFalse(form.is_valid())
        self.assertIn('km_saida', form.errors)

    def test_new_trip_requires_both_readings(self):
        for values in ({}, {'km_saida': '1000'}, {'km_chegada': '1200'}):
            with self.subTest(values=values):
                form = ViagemForm(data={**self.data, **values})
                self.assertFalse(form.is_valid())

    def test_legacy_distance_is_preserved_and_can_be_recalculated(self):
        trip = Viagem.objects.create(usuario=self.driver, veiculo=self.vehicle, origem='Salvador', destino='Feira de Santana', data_saida='2026-11-17', data_retorno='2026-11-18', distancia=230, valor_frete=1000, valor_resultado=500, status='Concluida')
        edit = ViagemForm(data=self.data, instance=trip)
        self.assertTrue(edit.is_valid(), edit.errors)
        self.assertEqual(edit.save().distancia, 230)
        edit = ViagemForm(data={**self.data, 'km_saida': '1000', 'km_chegada': '1240'}, instance=trip)
        self.assertTrue(edit.is_valid(), edit.errors)
        self.assertEqual(edit.save().distancia, 240)


class TripFinancialTests(TestCase):
    def setUp(self):
        from despesa.models import Despesa
        self.Despesa = Despesa
        driver = Usuario.objects.create(username='finance-driver', numero=1)
        vehicle = Veiculo.objects.create(placa='DEF1234', modelo='Teste', marca='Teste', ano=2024, quilometragem=0, status='Ativo', capacidade_carga=1000)
        self.trip = Viagem.objects.create(usuario=driver, veiculo=vehicle, origem='A', destino='B', data_saida='2026-11-17', data_retorno='2026-11-18', distancia=100, valor_frete=1000, valor_resultado=0, status='Concluida')
        self.other = Viagem.objects.create(usuario=driver, veiculo=vehicle, origem='C', destino='D', data_saida='2026-11-17', data_retorno='2026-11-18', distancia=100, valor_frete=500, valor_resultado=0, status='Concluida')

    def expense(self, value, trip=None):
        return self.Despesa.objects.create(viagem=trip or self.trip, tipo='Pedagio', descricao='Teste', valor=value, data='2026-11-17')

    def test_empty_totals_and_new_trip_result(self):
        self.assertEqual(self.Despesa.calcular_total(), 0)
        self.assertEqual(self.trip.calcular_resultado(), 1000)
        self.trip.refresh_from_db()
        self.assertEqual(self.trip.valor_resultado, 1000)

    def test_expenses_are_scoped_to_trip_and_totaled(self):
        self.expense(100)
        self.expense(50)
        self.expense(20, self.other)
        self.assertEqual(self.Despesa.calcular_total(self.trip), 150)
        self.assertEqual(self.Despesa.calcular_total(), 170)
        self.trip.refresh_from_db()
        self.assertEqual(self.trip.valor_resultado, 850)

    def test_update_move_and_bulk_delete_refresh_results(self):
        expense = self.expense(100)
        expense.valor = 200
        expense.save()
        self.trip.refresh_from_db()
        self.assertEqual(self.trip.valor_resultado, 800)
        expense.viagem = self.other
        expense.save()
        self.trip.refresh_from_db()
        self.other.refresh_from_db()
        self.assertEqual(self.trip.valor_resultado, 1000)
        self.assertEqual(self.other.valor_resultado, 300)
        self.Despesa.objects.filter(pk=expense.pk).delete()
        self.other.refresh_from_db()
        self.assertEqual(self.other.valor_resultado, 500)

    def test_negative_result_and_freight_update(self):
        self.expense(1100)
        self.trip.refresh_from_db()
        self.assertEqual(self.trip.valor_resultado, -100)
        self.trip.valor_frete = 1500
        self.trip.save()
        self.trip.refresh_from_db()
        self.assertEqual(self.trip.valor_resultado, 400)

    def test_trip_pages_show_automatic_financial_values(self):
        from django.contrib.auth.models import User
        from django.urls import reverse
        admin = User.objects.create_superuser(username='finance-admin', password='Test-admin-941!')
        self.client.force_login(admin)
        self.expense(100)
        detail = self.client.get(reverse('viagem_detail', args=[self.trip.pk]))
        self.assertEqual(detail.status_code, 200)
        self.assertEqual(detail.context['objeto'].total_despesas, 100)
        self.assertEqual(detail.context['objeto'].valor_resultado, 900)
        listing = self.client.get(reverse('viagem_list'))
        self.assertEqual(listing.status_code, 200)
        self.assertEqual(listing.context['total_resultado'], 1400)
        form = self.client.get(reverse('viagem_create'))
        self.assertNotContains(form, 'name="valor_resultado"')
