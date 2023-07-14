from django.db import models

# Create your models here.
class User(models.Model):
    nome = models.CharField(max_length=50)

class Stock(models.Model):
    name = models.CharField(max_length=10)
    interval = models.CharField(max_length=10)

    def __str__(self):
        return self.name