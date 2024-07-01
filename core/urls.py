from django.urls import path
from .views import index, produto, contato, exclui_produto, edita_produto


urlpatterns = [
    path('', index, name='index'),
    path('produto/', produto, name='produto'),
    path('contato/', contato, name='contato'),
    path('produto/deletar/<id_produto>/', exclui_produto, name='deleta_produto'),
    path('produto/editar/<id_produto>/', edita_produto, name='edita_produto'),
]