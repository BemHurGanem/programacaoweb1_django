from django.shortcuts import render, redirect

# Create your views here.
from django.template import Library

from .forms import ProdutoForm, ClienteForm, VendaForm, ProdutoVendaForm
from .models import Produto, Cliente, Venda, ProdutosVenda


def home(request):

    return render(request, 'home/home.html')


# PRODUTOS
def cadastrar_produto(request):
    form = ProdutoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('listar_produtos')
    else:
        form = ProdutoForm()

    return render(request, 'produto/produto_form.html', {'form_produto': form})


def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/index.html', {'produtos': produtos})


def editar_produto(request, id):
    produto = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
    return render(request, 'produto/produto_form.html', {'form_produto': form})


def remover_produto(request, id):
    produto = Produto.objects.get(id=id)
    if request.method == "POST":
        produto.delete()
        return redirect('listar_produtos')
    return render(request, 'produto/confirma_exclusao.html', {'produto': produto})


# CLIENTE
def cadastrar_cliente(request):
    form = ClienteForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('listar_cliente')
    else:
        form = ClienteForm()

    return render(request, 'cliente/cliente_form.html', {'form_cliente': form})


def listar_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/index.html', {'clientes': clientes})


def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
    return render(request, 'cliente/cliente_form.html', {'form_cliente': form})


def remover_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == "POST":
        cliente.delete()
        return redirect('listar_cliente')
    return render(request, 'cliente/confirma_exclusao.html', {'cliente': cliente})



# VENDA
def cadastrar_venda(request):
    form = VendaForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('listar_venda')
    else:
        form = VendaForm()

    produtos = Produto.objects.all()

    produtosform = []
    produtosform.append(ProdutoVendaForm())

    return render(request, 'venda/venda_form.html', {'venda_form': form,  "produtos":produtos, "forms":produtosform})


def listar_venda(request):
    vendas = Venda.objects.all()
    return render(request, 'venda/index.html', {'vendas': vendas})


def editar_venda(request, id):
    venda = Venda.objects.get(id=id)
    form = VendaForm(request.POST or None, instance=venda)
    if form.is_valid():
        form.save()
    return render(request, 'venda/venda_form.html', {'venda_form': form})


def remover_venda(request, id):
    venda = Venda.objects.get(id=id)
    if request.method == "POST":
        venda.delete()
        return redirect('listar_venda')
    return render(request, 'venda/confirma_exclusao.html', {'venda': venda})