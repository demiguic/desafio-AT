from django.db import models

# Create your models here.


class Asset(models.Model):
    name = models.CharField(max_length=10)
    interval = models.PositiveIntegerField()
    superior_limit = models.DecimalField(max_digits=5, decimal_places=2)
    inferior_limit = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    email_sent_status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - R$ {self.value}. Updated at {self.updated_at}'
