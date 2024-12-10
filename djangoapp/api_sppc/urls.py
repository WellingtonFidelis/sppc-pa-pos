from django.urls import path
from api_sppc.views import (
    #IncluirProdutoAPIView,
    #ListarProdutoAPIView,
    #AtualizarProdutoAPIView,
    #ExcluirProdutoAPIView,
    ProdutoAPIView,
    PrincipioAtivoAPIView,
    ConsumidorAPIView,
    TratamentoAPIView,
    ProdutoRecomendadoAPIView
)


urlpatterns = [
    #path("produto/incluir", IncluirProdutoAPIView.as_view()),
    #path("produto/listar", ListarProdutoAPIView.as_view()),
    #path("produto/<int:pk>/atualizar", AtualizarProdutoAPIView.as_view()),
    #path("produto/<int:pk>/excluir", ExcluirProdutoAPIView.as_view()),
    path(route="produto", view=ProdutoAPIView.as_view(), name="produto"),
    path(route="principio-ativo", view=PrincipioAtivoAPIView.as_view(), name="principio-ativo"),
    path(route="consumidor", view=ConsumidorAPIView.as_view(), name="consumidor"),
    path(route="tratamento", view=TratamentoAPIView.as_view(), name="tratamento"),
    path(route="produtos-recomendados/<int:pk>/", view=ProdutoRecomendadoAPIView.as_view(), name="produtos-recomendados"),
]
