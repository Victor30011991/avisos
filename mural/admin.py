# Register your models here.
from django.contrib import admin
from .models import Categoria, Aviso

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(Aviso)
class AvisoAdmin(admin.ModelAdmin):
    # Exibição das colunas na listagem
    list_display = ('titulo', 'caegoria', 'data_criacao')
    
    # Filtros laterais para facilitar a navegação
    list_filter = ('caegoria', 'data_criacao')
    
    # Barra de pesquisa para títulos
    search_fields = ('titulo', 'conteudo')
    
    # Ordenação padrão (mais recentes primeiro)
    ordering = ('-data_criacao',)