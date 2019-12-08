from django import forms
from .models import Produto, Cliente, Venda, ProdutosVenda

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        # exclude = ('produtos',)
        fields ='__all__'

class ProdutoVendaForm(forms.ModelForm):
    class Meta:
        model = ProdutosVenda
        exclude = ('venda',)

