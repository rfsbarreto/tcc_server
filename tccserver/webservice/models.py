from django.db import models

# Create your models here.
class Ponto(models.Model):
	latitude = models.CharField(max_length=20)
	longitude = models.CharField(max_length=20)
	id_smtt= models.IntegerField()
	cod_opcao = models.IntegerField()
