from django.db import models

# Create your models here.

class items(models.Model):
  name = models.TextField()
  price = models.DecimalField(default = 0.0, decimal_places=1, max_digits=5)
  enchanted = models.BooleanField(default=False)