from django.db import models

from django.conf.locale.pt_BR import formats as pt_BR_formats

pt_BR_formats.DATE_FORMAT = "d M Y"
pt_BR_formats.DATETIME_FORMAT = "d M Y H:i"


class Despesa(models.Model):
    TipoDespesa_choices = {
        ('', (
            ('RÉMEDIO', 'Rémedio'),
            ('ROUPAS', 'Roupas'),
            ('ALIMENTAÇÃO', 'Alimentação'),
            ('Educação', 'Educação'),
            ('TRANSPORTE', 'Transporte'),
            ('OUTROS', 'Outros'),
        ),
         )
    }
    FormaPagamento_choices = (
        (' ', (
            ('DINHEIRO', 'Dinheiro'),
            ('CARTÃO DE CRÉDITO', 'Cartão de Crédito'),
            ('CARTÃO DE DÉBITO', 'Cartão de Débito'),
            ('CARTÃO CREDIÁRIO', 'Cartão Crediário'),
            ('CHEQUE', 'Cheque'),
        ),
         ),
    )

    data_criacao = models.CharField('Data de Criação', max_length=10)
    tipoDespesa = models.CharField('Tipo de despesa', max_length=100, choices=TipoDespesa_choices, default=' ', )
    descricao = models.TextField('Descrição')
    formaPagamento = models.CharField('Forma de Pagamento', max_length=50, choices=FormaPagamento_choices,default=' ', )
    vencimento = models.DateField('Vencimento')
    quitado = models.BooleanField('Quitado')

    class Meta:
        verbose_name_plural = 'Despesas'
        verbose_name = 'Despesa'
        ordering = ('vencimento', 'formaPagamento')
