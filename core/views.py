from django.shortcuts import render, get_object_or_404
from .forms import ContatoForm, ProdutoModelForm
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib import messages
from .models import Produto
from django.urls import reverse

def index(request: HttpRequest):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request: HttpRequest):
    form = ContatoForm(request.POST or None) # Formulário pode enviar um POST quando preenchemos os campos ou None quando for apenas para apresentar o formulário em branco

    if str(request.method) == 'POST':
        if form.is_valid():
            form.envio_email()

            messages.success(request, 'Email enviado com sucesso')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar email')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request: HttpRequest):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request, 'Produto salvo com sucesso.')
            form = ProdutoModelForm()
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request, 'Erro ao salvar produto.')
    else:
        form = ProdutoModelForm()

    context = {
        'form': form
    }
    return render(request, 'produto.html', context)

def exclui_produto(request: HttpRequest, id_produto):
    produto = get_object_or_404(Produto, pk=id_produto)

    if request.method == 'POST':
        produto.delete()
        return HttpResponseRedirect(reverse('index'))

    context = {
        'produto': produto
    }

    return render(request, 'index.html', context)

def edita_produto(request: HttpRequest, id_produto):
    produto = get_object_or_404(Produto, pk=id_produto)
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():            
            form.save()

            messages.success(request, 'Produto editado com sucesso.')
            form = ProdutoModelForm()
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.error(request, 'Erro ao editar produto.')
    else:
        form = ProdutoModelForm(instance=produto)

    context = {
        'form': form,
        'produto': produto,
    }
    return render(request, 'edita_produto.html', context)