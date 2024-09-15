import os

import django
from django.db import models

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
