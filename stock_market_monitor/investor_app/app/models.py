from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Stock(models.Model):
    name = models.CharField(max_length=10)
    interval = models.PositiveIntegerField()
    superior_limit = models.DecimalField(max_digits=5, decimal_places=2)
    inferior_limit = models.DecimalField(max_digits=5, decimal_places=2)
    updated_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name