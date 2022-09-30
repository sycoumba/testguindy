from django.db import models

# Create your models here.
from django.db import models                              
class Categories(models.Model):
        categories = models.CharField(max_length=120)
        sous_categories = models.CharField(max_length=120)
        sous_sous_categories = models.CharField(max_length=120)
        produits = models.CharField(max_length=120)
        def __str__(self):
            return self.categories   
