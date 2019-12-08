from django.shortcuts import render, redirect

# Create your views here.
from .forms import ProdutoForm, ClienteForm, VendaForm, ProdutoVendaForm
from .models import Produto, Cliente, Venda


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
    produtoForm = ProdutoVendaForm(request.POST)
    if form.is_valid() and produtoForm.is_valid():
        form.save()
        return redirect('listar_venda')
    else:
        form = VendaForm()
        produtoForm = ProdutoVendaForm()

    return render(request, 'venda/venda_form.html', {'venda_form': form, 'produtovenda_form': produtoForm})


def listar_venda(request):
    vendas = Venda.objects.all()
    return render(request, 'venda/index.html', {'vendas': vendas})

