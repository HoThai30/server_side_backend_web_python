from django.db import models
from django.urls import reverse


from shop.custom_field import*
from shop.define import*

from .order import Order
from .Product import Product

class OrderItem(models.Model):
   order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
   product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
   quantity = models.IntegerField()
   price = models.DecimalField(max_digits=10, decimal_places=0)
   total = models.DecimalField(max_digits=10, decimal_places=0)


   def __str__(self):
        return "" 