from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField()
    
    class Meta:
        indexes = [
            models.Index(fields=['price']),
        ]
