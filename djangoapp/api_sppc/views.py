# from django.shortcuts import render

from django.http import JsonResponse
from api_sppc.models import Produto, PrincipioAtivo, Consumidor, Tratamento
from api_sppc.serializers import (
    ProdutoSerializer,
    PrincipioAtivoSerializer,
    ConsumidorSerializer,
    TratamentoSerializer,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import pickle
import pandas as pd
import psycopg2 as ps
import os
import numpy as np

# Create your views here.


def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "Hi, hello, world!"})


class Recomendacao:
    """Recomenda produtos com base nos consumidores que tiveram tratamentos cadastrados no sistema
    Args:
    Returns:
    """    
    def __init__(self):
        super().__init__()
        self.model = self._load_model()
        self.df_model_pivot = self._prepare_dataframe()

    def _load_model(self):
        """Carrega o modelo KNN que ecomenda produtos com base nos consumidores 
        que tiveram tratamentos cadastrados no sistema

        Returns:
            pickle: modelo KNN
        """
        with open("./auxiliar/nearest_neighbors_model.pkl", "rb") as f:
            return pickle.load(f)

    def _prepare_dataframe(self):
        conn = ps.connect(
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            host=os.getenv("POSTGRES_HOST"),
            password=os.getenv("POSTGRES_PASSWORD"),
            port=os.getenv("POSTGRES_PORT"),
        )

        cs = conn.cursor()

        try:
            cs.execute(
                query="select * from sppc_db.public.api_sppc_tratamento_produtos;"
            )
            result = cs.fetchall()
            df_tratamentos_produtos = pd.DataFrame(
                data=result, columns=[desc[0] for desc in cs.description]
            )
            df_tratamentos_produtos = df_tratamentos_produtos.replace({None: np.nan})
            print("Consulta realizada com sucesso.")
        except Exception as e:
            print("Alguma coisa ruim aconteceu enquanto consultava a tabela: ", e)

        df_tratamentos = pd.DataFrame(Tratamento.objects.all().values())

        df_model = pd.merge(
            left=df_tratamentos,
            right=df_tratamentos_produtos,
            left_on=["id"],
            right_on=["tratamento_id"],
            how="left",
            suffixes=["_tratamento", "_produto"],
        )

        df_model = df_model[
            ["consumidores_id", "produto_id", "id_tratamento", "eficaz"]
            and df_model["eficaz"] == 1
        ]

        df_model = df_model.astype(dtype={"eficaz": np.int8})

        df_model_pivot = df_model.pivot_table(
            columns=["produto_id"], index=["consumidores_id"], values=["eficaz"]
        )
        df_model_pivot.fillna(value=0, inplace=True)

        return (df_model_pivot, df_tratamentos, df_tratamentos_produtos)

    def get_recomedacoes(self, pk):
        # consumidor = Consumidor.objects.get(pk=pk)
        df_model_pivot, df_tratamentos, df_tratamentos_produtos = (
            self._prepare_dataframe()
        )
        distances, sugestions = self.model.kneighbors(
            df_model_pivot.filter(items=[int(pk)], axis=0).values.reshape(1, -1)
        )
        # Obter os IDs dos tratamentos dos vizinhos
        ids_tratametnos = (
            df_tratamentos[df_tratamentos["consumidores_id"].isin(sugestions[0])]
            .drop_duplicates(["consumidores_id"])["id"]
            .values
        )
        # Obter os IDs dos produtos dos tratamentos
        produtos_recomendados = (
            df_tratamentos_produtos[
                df_tratamentos_produtos["tratamento_id"].isin(ids_tratametnos)
            ]["produto_id"]
            .drop_duplicates()
            .sample(n=3)
            .values
        )
        return produtos_recomendados


class ProdutoAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer_class = ProdutoSerializer(data=data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        else:
            return Response(serializer_class.errors)

    def get(self, request):
        data = request.data
        id = data.get("id", None)

        if id is not None:
            queryset = Produto.objects.get(id=id)
            serializer_class = ProdutoSerializer(queryset)
            return Response(serializer_class.data)

        queryset = Produto.objects.all()
        serializer_class = ProdutoSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def put(self, request):
        data = request.data
        id = data.get("id", None)
        queryset = Produto.objects.get(id=id)
        serializer_class = ProdutoSerializer(queryset, data=data, partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        else:
            return Response(serializer_class.errors)

    def delete(self, request):
        data = request.data
        id = data.get("id", None)
        try:
            queryset = Produto.objects.get(id=id)
        except Produto.DoesNotExist:
            response = {"message": f"Produto '{id}' não encontrado."}
            return Response(response, status=404)

        queryset.delete()
        response = {"message": "Produto excluído com sucesso."}
        return Response(response)


""" class IncluirProdutoAPIView(generics.CreateAPIView):
    summary_

    Args:
        request (_type_): _description_


    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ListarProdutoAPIView(generics.ListAPIView):
    _summary_

    Args:
        request (_type_): _description_


    queryset = Produto.objects.all().order_by("nome")
    serializer_class = ProdutoSerializer


class AtualizarProdutoAPIView(generics.UpdateAPIView):
    _summary_

    Args:
        request (_type_): _description_
    

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    lookup_field = "pk"


class ExcluirProdutoAPIView(generics.DestroyAPIView):
    summary_

    Args:
        request (_type_): _description_


    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    lookup_field = "pk"
 """


class PrincipioAtivoAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer_class = PrincipioAtivoSerializer(data=data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        else:
            return Response(serializer_class.errors)

    def get(self, request):
        data = request.data
        id = data.get("id", None)

        if id is not None:
            queryset = PrincipioAtivo.objects.get(id=id)
            serializer_class = PrincipioAtivoSerializer(queryset)
            return Response(serializer_class.data)

        queryset = PrincipioAtivo.objects.all()
        serializer_class = PrincipioAtivoSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def put(self, request):
        data = request.data
        id = data.get("id", None)
        queryset = PrincipioAtivo.objects.get(id=id)
        serializer_class = PrincipioAtivoSerializer(queryset, data=data, partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        else:
            return Response(serializer_class.errors)

    def delete(self, request):
        data = request.data
        id = data.get("id", None)
        try:
            queryset = PrincipioAtivo.objects.get(id=id)
        except PrincipioAtivo.DoesNotExist:
            response = {"message": f"Principio ativo '{id}' não encontrado."}
            return Response(response, status=404)

        queryset.delete()
        response = {"message": "Principio ativo excluído com sucesso."}
        return Response(response)


class ConsumidorAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer_class = ConsumidorSerializer(data=data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        else:
            return Response(serializer_class.errors)

    def get(self, request):
        data = request.data
        id = data.get("id", None)

        if id is not None:
            queryset = Consumidor.objects.get(id=id)
            serializer_class = ConsumidorSerializer(queryset)
            return Response(serializer_class.data)

        queryset = Consumidor.objects.all()
        serializer_class = ConsumidorSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def put(self, request):
        data = request.data
        id = data.get("id", None)
        queryset = Consumidor.objects.get(id=id)
        serializer_class = ConsumidorSerializer(queryset, data=data, partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        else:
            return Response(serializer_class.errors)

    def delete(self, request):
        data = request.data
        id = data.get("id", None)
        try:
            queryset = Consumidor.objects.get(id=id)
        except Consumidor.DoesNotExist:
            response = {"message": f"Consumidor '{id}' não encontrado."}
            return Response(response, status=404)

        queryset.delete()
        response = {"message": "Consumidor excluído com sucesso."}
        return Response(response)


class TratamentoAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer_class = TratamentoSerializer(data=data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        else:
            return Response(serializer_class.errors)

    def get(self, request):
        data = request.data
        id = data.get("id", None)

        if id is not None:
            queryset = Tratamento.objects.get(id=id)
            serializer_class = TratamentoSerializer(queryset)
            return Response(serializer_class.data)

        queryset = Tratamento.objects.all()
        serializer_class = TratamentoSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def put(self, request):
        data = request.data
        id = data.get("id", None)
        queryset = Tratamento.objects.get(id=id)
        serializer_class = TratamentoSerializer(queryset, data=data, partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data)
        else:
            return Response(serializer_class.errors)

    def delete(self, request):
        data = request.data
        id = data.get("id", None)
        try:
            queryset = Tratamento.objects.get(id=id)
        except Tratamento.DoesNotExist:
            response = {"message": f"Tratamento '{id}' não encontrado."}
            return Response(response, status=404)

        queryset.delete()
        response = {"message": "Tratamento excluído com sucesso."}
        return Response(response)


class ProdutoRecomendadoAPIView(APIView):

    """ def __init__(self):
        super().__init__()
        self.model = self._load_model()
        self.df_model_pivot = self._prepare_dataframe() """
    def __init__(self):
        super().__init__()
        self.recomendacoes = Recomendacao()
        
    """ 
    def _load_model(self):
        with open("./auxiliar/nearest_neighbors_model.pkl", "rb") as f:
            return pickle.load(f)

    def _prepare_dataframe(self):
        conn = ps.connect(
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            host=os.getenv("POSTGRES_HOST"),
            password=os.getenv("POSTGRES_PASSWORD"),
            port=os.getenv("POSTGRES_PORT"),
        )

        cs = conn.cursor()

        try:
            cs.execute(
                query="select * from sppc_db.public.api_sppc_tratamento_produtos;"
            )
            result = cs.fetchall()
            df_tratamentos_produtos = pd.DataFrame(
                data=result, columns=[desc[0] for desc in cs.description]
            )
            df_tratamentos_produtos = df_tratamentos_produtos.replace({None: np.nan})
            print("Consulta realizada com sucesso.")
        except Exception as e:
            print("Alguma coisa ruim aconteceu enquanto consultava a tabela: ", e)

        df_tratamentos = pd.DataFrame(Tratamento.objects.all().values())

        df_model = pd.merge(
            left=df_tratamentos,
            right=df_tratamentos_produtos,
            left_on=["id"],
            right_on=["tratamento_id"],
            how="left",
            suffixes=["_tratamento", "_produto"],
        )

        df_model = df_model[
            ["consumidores_id", "produto_id", "id_tratamento", "eficaz"]
            and df_model["eficaz"] == 1
        ]

        df_model = df_model.astype(dtype={"eficaz": np.int8})

        df_model_pivot = df_model.pivot_table(
            columns=["produto_id"], index=["consumidores_id"], values=["eficaz"]
        )
        df_model_pivot.fillna(value=0, inplace=True)

        return (df_model_pivot, df_tratamentos, df_tratamentos_produtos)
    """
 
    def get(self, request, pk=None):
        try:
            """ # consumidor = Consumidor.objects.get(pk=pk)
            df_model_pivot, df_tratamentos, df_tratamentos_produtos = (
                self._prepare_dataframe()
            )
            distances, sugestions = self.model.kneighbors(
                df_model_pivot.filter(items=[int(pk)], axis=0).values.reshape(1, -1)
            )
            # Obter os IDs dos tratamentos dos vizinhos
            ids_tratametnos = (
                df_tratamentos[df_tratamentos["consumidores_id"].isin(sugestions[0])]
                .drop_duplicates(["consumidores_id"])["id"]
                .values
            )
            # Obter os IDs dos produtos dos tratamentos
            produtos_recomendados = (
                df_tratamentos_produtos[
                    df_tratamentos_produtos["tratamento_id"].isin(ids_tratametnos)
                ]["produto_id"]
                .drop_duplicates()
                .sample(n=3)
                .values
            ) """
            produtos_recomendados = self.recomendacoes.get_recomedacoes(pk=pk)
            produtos = Produto.objects.filter(
                id__in=produtos_recomendados
            )
            serializer = ProdutoSerializer(produtos, many=True)
            produtos_recomendados = Produto.objects.filter(id__in=produtos_recomendados)
            serializer = ProdutoSerializer(produtos_recomendados, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ConsumidorProdutoRecomendadoAPIView(APIView):

    def __init__(self):
        super().__init__()
        self.recomendacoes = Recomendacao()
        
        
    def post(self, request):
        data = request.data
        serializer_consumidor_class = ConsumidorSerializer(data=data)

        if serializer_consumidor_class.is_valid():
            consumidor = serializer_consumidor_class.save()
            produtos_recomendados = self.recomendacoes.get_recomedacoes(pk=consumidor.id)
            produtos = Produto.objects.filter(
                id__in=produtos_recomendados
            )
            serializer_produtos_class = ProdutoSerializer(produtos, many=True)
            produtos_recomendados = Produto.objects.filter(id__in=produtos_recomendados)
            serializer_produtos_class = ProdutoSerializer(produtos_recomendados, many=True)
            return Response(serializer_produtos_class.data, status=201)

        else:
            return Response(data=serializer_consumidor_class.errors, status=422)
