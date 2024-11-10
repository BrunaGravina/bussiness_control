from django.db import models

class Empresa(models.Model):
    cnpj = models.CharField(max_length=18, unique=True)
    logradouro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.cnpj

class Funcionario(models.Model):
    nome_completo = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    data_ingresso = models.DateField()
    data_desligamento = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=True)
    cidade = models.CharField(max_length=100)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='funcionarios')

    def __str__(self):
        return self.nome_completo





