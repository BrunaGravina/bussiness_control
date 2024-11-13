from register.serializers import EmpresaSerializer
from django.test import TestCase
from register.models import Empresa
from register.serializers import FuncionarioSerializer
from datetime import date
from datetime import date

from django.test import TestCase

from register.models import Empresa
from register.serializers import EmpresaSerializer
from register.serializers import FuncionarioSerializer


class EmpresaSerializerTest(TestCase):
    def setUp(self):
        self.empresa_data = {
            "cnpj": "12.345.678/0001-90",
            "logradouro": "Rua das Lágrimas, 122",
            "cidade": "São Caetano",
            "pais": "Brasil",
            "ativo": True
        }

    def test_empresa_serializer_valid_data(self):
        serializer = EmpresaSerializer(data=self.empresa_data)
        self.assertTrue(serializer.is_valid())


    def test_empresa_serializer_invalid_data(self):
        invalid_data = self.empresa_data.copy()
        invalid_data["cnpj"] = ""
        serializer = EmpresaSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("cnpj", serializer.errors)



class FuncionarioSerializerTest(TestCase):
    def setUp(self):
        self.empresa = Empresa.objects.create(
            cnpj="12.345.678/0001-90",
            logradouro="Rua das Flores, 123",
            cidade="São Paulo",
            pais="Brasil",
            ativo=True
        )

        self.funcionario_data = {
            "nome_completo": "João Silva",
            "email": "joao.silva@example.com",
            "telefone": "11999999999",
            "data_nascimento": date(1990, 1, 1),
            "data_ingresso": date(2020, 5, 1),
            "ativo": True,
            "cidade": "São Paulo",
            "empresa": self.empresa.id  # Associando ao ID da empresa
        }

    def test_funcionario_serializer_valid(self):
        serializer = FuncionarioSerializer(data=self.funcionario_data)
        self.assertTrue(serializer.is_valid())

    def test_funcionario_serializer_invalid_email(self):
        invalid_data = self.funcionario_data.copy()
        invalid_data["email"] = "invalid-email"
        serializer = FuncionarioSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
