from django.urls import path
from .views import index, produto, contato


urlpatterns = [
    path('', index, name='index'),
    path('produto/', produto, name='produto'),
    path('contato/', contato, name='contato'),
]