# Documentação de Testes da API de Cadastro

Este documento tem como objetivo detalhar o raciocínio e a mecânica por trás dos testes implementados na aplicação de cadastro, que envolve as operações de CRUD (Create, Read, Update, Delete) para as entidades **Empresa** e **Funcionario**. Os testes abrangem as validações de **modelos**, **serializers** e **views** utilizadas na aplicação.

## Estrutura de Testes

Os testes estão organizados da seguinte forma:

- **Testes de Modelos**: Validam o comportamento dos modelos `Empresa` e `Funcionario`, garantindo que os dados sejam armazenados corretamente e que os relacionamentos entre as entidades estejam funcionando como esperado.
  
- **Testes de Serializers**: Avaliam se os serializers estão corretamente serializando e desserializando os dados para as entidades `Empresa` e `Funcionario`, e também verificar a validação de campos obrigatórios e formatos de dados.

- **Testes de Views**: Testam a interação com as views e endpoints da API, validando as respostas, códigos de status e mensagens retornadas pela API.

## Tipos de testes

### 1. Testes de Modelos

Os testes de modelo garantem que os dados de empresas e funcionários sejam armazenados corretamente e que os relacionamentos entre as tabelas funcionem como esperado.

**Cenários Testados:**
- Criação de empresas com atributos válidos (CNPJ, endereço, cidade, etc.).
- Criação de funcionários associados corretamente a uma empresa.
- Verificação para para que não seja possível criar empresas com o mesmo CNPJ.
- Exclusão de registros e a verificação do campo `ativo` para marcação de inatividade.

**Exemplo de Teste de Modelo:**

```python
class EmpresaModelTest(TestCase):
    def setUp(self):
        self.empresa = Empresa.objects.create(
            cnpj='12.345.678/0001-90',
            logradouro='Rua das Loucuras, 156',
            cidade='São Paulo',
            pais='Brasil',
            ativo=True
        )

    def test_empresa_criada(self):
        self.assertEqual(self.empresa.cnpj, '12.345.678/0001-90')
        self.assertEqual(self.empresa.logradouro, 'Rua das Loucuras, 156')
        self.assertEqual(self.empresa.cidade, 'São Paulo')
        self.assertEqual(self.empresa.pais, 'Brasil')
        self.assertTrue(self.empresa.ativo)

```
### 2. Testes de Serializers 

Os testes de serializers garantem que os dados sejam corretamente validados e convertidos entre formato JSON e os modelos do banco de dados.

**Cenários Testados:**
- Validação de campos obrigatórios (como cnpj e nome_completo).
- Teste de dados inválidos e se a resposta de erro é retornada corretamente.

**Exemplo**

```python

class EmpresaSerializerTest(TestCase):
    def setUp(self):
        self.empresa_data = {
            "cnpj": "12.345.678/0001-90",
            "logradouro": "Rua das Flores, 123",
            "cidade": "São Paulo",
            "pais": "Brasil",
            "ativo": True
        }

    def test_empresa_serializer_valid_data(self):
        serializer = EmpresaSerializer(data=self.empresa_data)
        self.assertTrue(serializer.is_valid())

```

## 3. Testes de Views

Os testes de views verificam se as respostas da API estão corretas em termos de código de status HTTP, dados retornados, e se as operações de CRUD funcionam conforme o esperado.

**Cenários Testados:**
- Verificação de inativar empresas e funcionários.
- Verificação de basic auth configurado no .env.

```python

class EmpresaViewSetTest(APITestCase):

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

```


