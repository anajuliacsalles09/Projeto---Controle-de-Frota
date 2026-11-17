from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class UnifiedLoginTests(TestCase):
    def test_entry_shows_login_without_profile_choice(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'name="username"')
        self.assertNotContains(response, 'Como deseja entrar?')
        self.assertNotContains(response, 'Trocar perfil')

    def test_accounts_login_without_selecting_profile(self):
        for admin in (False, True):
            with self.subTest(admin=admin):
                user = User.objects.create_user(username=f'account{admin}', password='Test-login-842!', is_superuser=admin)
                response = self.client.post(reverse('login'), {'username': user.username, 'password': 'Test-login-842!'})
                self.assertRedirects(response, '/', fetch_redirect_response=False)
                user.refresh_from_db()
                self.assertEqual(user.is_superuser, admin)
                self.client.logout()

    def test_invalid_password_is_rejected(self):
        User.objects.create_user(username='test', password='Test-login-842!')
        response = self.client.post(reverse('login'), {'username': 'test', 'password': 'wrong'})
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_external_next_is_rejected(self):
        User.objects.create_user(username='test', password='Test-login-842!')
        response = self.client.post(reverse('login'), {'username': 'test', 'password': 'Test-login-842!', 'next': 'https://example.com/'})
        self.assertRedirects(response, '/', fetch_redirect_response=False)

    def test_old_profile_links_redirect_to_unified_login(self):
        for profile in ('admin', 'funcionario'):
            response = self.client.get(reverse('login_perfil', kwargs={'perfil': profile}), {'next': '/veiculos/'})
            self.assertRedirects(response, reverse('login') + '?next=%2Fveiculos%2F', fetch_redirect_response=False)

    def test_inactive_account_cannot_login(self):
        User.objects.create_user(username='inactive', password='Test-login-842!', is_active=False)
        response = self.client.post(reverse('login'), {'username': 'inactive', 'password': 'Test-login-842!'})
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('_auth_user_id', self.client.session)


class UserListCountsTests(TestCase):
    def test_counts_include_superusers_without_profile(self):
        from usuario.models import Usuario
        admin = User.objects.create_superuser(username='rootadmin', password='Test-login-842!')
        Usuario.objects.create(username='employee', nome='Employee', numero=1, tipo='FUNCIONARIO')
        Usuario.objects.create(username='profileadmin', nome='Admin', numero=1, tipo='ADMIN')
        Usuario.objects.create(username='superprofile', nome='Super', numero=1, tipo='FUNCIONARIO', is_superuser=True)
        self.client.force_login(admin)
        response = self.client.get(reverse('usuario_list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['quantidade_usuarios'], 4)
        self.assertEqual(response.context['quantidade_administradores'], 3)
        self.assertEqual(response.context['quantidade_funcionarios'], 1)
        self.assertContains(response, 'rootadmin')
