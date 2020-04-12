from django.db import models

class Categoria(models.Model):
    nome      = models.CharField(max_length=100)
    dtCriacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.nome

class Transacao(models.Model):
    data        = models.DateTimeField()
    descricao   = models.CharField(max_length=200)
    valor       = models.DecimalField(max_digits=7, decimal_places=2)
    categoria   = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    observacoes = models.TextField(null=True, blank=True)

    # Definir o nome plural da minha classe
    class Meta:
        verbose_name_plural = 'Transacoes'

    # Definir o campo que será exibido na lista de cadastro
    def __str__(self):
       return self.descricao