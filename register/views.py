from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Empresa, Funcionario
from .serializers import EmpresaSerializer, FuncionarioSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

    @action(detail=True, methods=['post'])
    def inativar(self, request, pk=None):
        empresa = self.get_object()
        empresa.ativo = False
        empresa.save()
        return Response({'status': 'Empresa inativa'})

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

    @action(detail=True, methods=['post'])
    def inativar(self, request, pk=None):
        funcionario = self.get_object()
        funcionario.ativo = False
        funcionario.save()
        return Response({'status': 'Funcionario inativo'})


