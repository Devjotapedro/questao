from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .models import Produtos

# Create your views here.

def home(request):
    valor1 = 'Primeiro valor'
    valor2 = 'Segundo Valor'
    valor3 = 'terceiro Valor'
    
    contexto = {
        "valor1": valor1,
        "valor2": valor2,
        "valor3": valor3
    }
    
    return render(request, "home.html", contexto)

class ProdutoCreateView(CreateView):
    model = Produtos
    fields = ['Codigo', 'NomeDoProduto', 'PrecoaVista', 'PrecoaPrazo']
    template_name = "produto_form.html"
    success_url = "/produtos/"


class ProdutoListView(ListView):
    model = Produtos
    template_name = "produto_list.html"
    context_object_name = "produtos"


class ProdutoUpdateView(UpdateView):
    model = Produtos
    fields = ['Codigo', 'NomeDoProduto', 'PrecoaVista', 'PrecoaPrazo']
    template_name = "produto_form.html"
    success_url = "/produtos/"


class ProdutoDeleteView(DeleteView):
    model = Produtos
    template_name = "produto_confirm_delete.html"
    success_url = "/produtos/"