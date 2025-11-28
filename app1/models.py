from django.db import models

# Create your models here.
class Produtos(models.Model):
    Codigo = models.IntegerField()
    NomeDoProduto = models.CharField(max_length=40)
    PrecoaVista = models.FloatField()
    PrecoaPrazo = models.FloatField()
    
    def __str__(self):
        return self.NomeDoProduto