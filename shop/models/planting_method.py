from django.db import models
from django.urls import reverse


from shop.custom_field import*
from shop.define import*

class Planting_method(models.Model):
   
    name = models.CharField(unique=True, max_length=100)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES,  default= APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = TABLE_PLANTING_METHOD_SHOW
        
    def __str__(self):
        return self.name