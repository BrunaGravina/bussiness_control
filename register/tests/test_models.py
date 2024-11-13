from django.test import TestCase
from register.models import Empresa, Funcionario
from datetime import date

from django.test import TestCase
from register.models import Empresa


class EmpresaModelTest(TestCase):
    def setUp(self):
        self.empresa = Empresa.objects.create(
            cnpj='12.345.678/0001-90',
            logradouro='Rua das Flores, 123',
            cidade='São Paulo',
            pais='Brasil',
            ativo=True
        )

    def test_empresa_criada(self):
        self.assertEqual(self.empresa.cnpj, '12.345.678/0001-90')
        self.assertEqual(self.empresa.logradouro, 'Rua das Flores, 123')
        self.assertEqual(self.empresa.cidade, 'São Paulo')
        self.assertEqual(self.empresa.pais, 'Brasil')
        self.assertTrue(self.empresa.ativo)

    def test_campo_cnpj_unico(self):
        with self.assertRaises(Exception):
            Empresa.objects.create(
                cnpj='12.345.678/0001-90',
                logradouro='Rua Nova, 456',
                cidade='Rio de Janeiro',
                pais='Brasil',
                ativo=True
            )

    def test_str_method(self):
        self.assertEqual(str(self.empresa), '12.345.678/0001-90')


def test_empresa_inativacao(self):
    # Testa se a empresa pode ser inativada
    self.empresa.ativo = False
    self.empresa.save()
    self.assertFalse(self.empresa.ativo)


class FuncionarioModelTest(TestCase):
    def setUp(self):
        # Configuração inicial de uma instância de Empresa e Funcionario para testes
        self.empresa = Empresa.objects.create(
            cnpj="12345678000199",
            logradouro="Rua das Flores, 123",
            cidade="São Paulo",
            pais="Brasil",
            ativo=True
        )
        self.funcionario = Funcionario.objects.create(
            nome_completo="João Silva",
            email="joao.silva@example.com",
            telefone="11999999999",
            data_nascimento=date(1990, 1, 1),
            data_ingresso=date(2020, 5, 1),
            ativo=True,
            cidade="São Paulo",
            empresa=self.empresa
        )

    def test_funcionario_creation(self):
        # Testa se o funcionário foi criado corretamente
        self.assertEqual(self.funcionario.nome_completo, "João Silva")
        self.assertEqual(self.funcionario.empresa, self.empresa)
        self.assertTrue(self.funcionario.ativo)

    def test_funcionario_inativacao(self):
        # Testa se o funcionário pode ser inativado
        self.funcionario.ativo = False
        self.funcionario.save()
        self.assertFalse(self.funcionario.ativo)
