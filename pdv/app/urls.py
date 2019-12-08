from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name=''),

    path('listar_produtos', listar_produtos, name='listar_produtos'),
    path('cadastrar_produto', cadastrar_produto, name="cadastrar_produto"),
    path('editar_produto/<int:id>', editar_produto, name='editar_produto'),
    path('remover_produto/<int:id>', remover_produto, name='remover_produto'),

    path('listar_cliente', listar_cliente, name='listar_cliente'),
    path('cadastrar_cliente', cadastrar_cliente, name="cadastrar_cliente"),
    path('editar_cliente/<int:id>', editar_cliente, name='editar_cliente'),
    path('remover_cliente/<int:id>', remover_cliente, name='remover_cliente'),

    path('listar_venda', listar_venda, name='listar_venda'),
    path('cadastrar_venda', cadastrar_venda, name="cadastrar_venda"),
    path('editar_venda/<int:id>', editar_venda, name='editar_venda'),
    path('remover_venda/<int:id>', remover_venda, name='remover_venda'),
]
