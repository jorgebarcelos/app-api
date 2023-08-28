from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField('name', max_length=150)
    cnpj = models.IntegerField('cnpj')
    description = models.TextField()

    def __str__(self) -> str:
        return self.name