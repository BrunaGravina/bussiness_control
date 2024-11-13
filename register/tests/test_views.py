from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from register.models import Empresa, Funcionario
from datetime import date
from dotenv import load_dotenv
import base64
import os

load_dotenv()


class EmpresaViewSetTest(APITestCase):

    def get_basic_auth(self):
        import base64
        credentials = f'{self.username}:{self.password}'
        return base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

    def setUp(self):
        self.username = os.getenv('USER_USERNAME')
        self.password = os.getenv('USER_PASSWORD')

        self.user = User.objects.create_user(username=self.username, password=self.password)

        self.empresa = Empresa.objects.create(
            cnpj="12.345.678/0001-99",
            logradouro="Rua Testando, 178",
            cidade="Cidade Teste",
            pais="Brasil",
            ativo=True
        )

        self.client.credentials(HTTP_AUTHORIZATION=f'Basic {self.get_basic_auth()}')

    def test_inativar_empresa(self):
        response = self.client.post(f'/api/empresas/{self.empresa.id}/inativar/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.empresa.refresh_from_db()
        self.assertFalse(self.empresa.ativo)

        self.assertEqual(response.data['status'], 'Empresa inativa')


class FuncionarioViewSetTest(APITestCase):

    def get_basic_auth(self):
        credentials = f'{self.username}:{self.password}'
        return base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

    def setUp(self):
        self.username = os.getenv('USER_USERNAME')
        self.password = os.getenv('USER_PASSWORD')

        if not self.username or not self.password:
            raise ValueError("Usuário ou senha errados, checar o .env")


        self.empresa = Empresa.objects.create(
            cnpj="12.332.678/0001-90",
            logradouro="Rua Testezinho",
            cidade="São Paulo",
            pais="Brasil",
            ativo=True
        )

        self.user = User.objects.create_user(username=self.username, password=self.password)

        self.funcionario = Funcionario.objects.create(
            nome_completo="Cleber Carlos",
            email="cleber.c@empresa.com",
            telefone="1234567890",
            data_nascimento=date(2001, 12, 30),
            data_ingresso=date(2020, 4, 3),
            ativo=True,
            cidade="Rio de Janeiro",
            empresa=self.empresa
        )


        self.client.credentials(HTTP_AUTHORIZATION=f'Basic {self.get_basic_auth()}')


    def test_inativar_funcionario(self):
        url = f'/api/funcionarios/{self.funcionario.id}/inativar/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'Funcionario inativo')

        self.funcionario.refresh_from_db()

        self.assertFalse(self.funcionario.ativo)
