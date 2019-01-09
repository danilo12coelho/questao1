from django.contrib import admin

from core.models import Despesa

admin.site.site_header = 'Painel de Controle'
admin.site.index_title = 'Despesas'
admin.site.index_title = 'Controle de Gastos'


class DepesaAdmin(admin.ModelAdmin):
    list_display = ('data_criacao', 'tipoDespesa', 'descricao', 'formaPagamento', 'vencimento', 'quitado',)

    date_hierarchy = 'vencimento'
    list_filter = ('quitado',)


admin.site.register(Despesa, DepesaAdmin)
