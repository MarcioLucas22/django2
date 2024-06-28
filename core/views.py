from django.shortcuts import render
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