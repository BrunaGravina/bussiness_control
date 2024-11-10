from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'empresas', views.EmpresaViewSet)
router.register(r'funcionarios', views.FuncionarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
