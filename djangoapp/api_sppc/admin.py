from django.contrib import admin
from api_sppc.models import (
    Produto,
    PrincipioAtivo,
    Consumidor,
    Tratamento
)

# Register your models here.
admin.site.register([
    Produto,
    PrincipioAtivo,
    Consumidor,
    Tratamento
])
