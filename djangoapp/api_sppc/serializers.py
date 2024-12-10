from rest_framework import serializers
from api_sppc.models import Produto, PrincipioAtivo, Consumidor, Tratamento


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ["id", "nome", "marca", "funcao", "peso_liquido", "unidade_medida", "principios_ativos"]
        # fields = ["__all__"]
        # exclude = ["id"]


class PrincipioAtivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrincipioAtivo
        fields = ["id", "nome"]
        # exclude = ["id"]


class ConsumidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumidor
        fields = "__all__"
        # exclude = ["id"]
        

class TratamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamento
        fields = "__all__"
        # exclude = ["id"]


class RecomendacoesSerializer(serializers.Serializer):
    produtos_recomendados = ProdutoSerializer(many=True, read_only=True)