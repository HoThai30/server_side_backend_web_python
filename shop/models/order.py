from django.db import models
from django.urls import reverse
from django.utils.timezone import now


from shop.custom_field import*
from shop.define import*

class Order(models.Model):

    code = models.CharField(unique=True, max_length=10)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    quantity = models.IntegerField(default=0)
    total = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_ORDER_CHOICES, default=APP_VALUE_STATUS_ORDER_DEFAULT)
    created = models.DateTimeField(default=now)
    
    class Meta:
        verbose_name_plural = TABLE_ORDER_SHOW 

    def __str__(self):
        return self.name
    
    def update_total_sold(self):
        if self.status == "finish":
            for item in self.order_items.all():
                product = item.product
                product.total_sold += item.quantity
                product.save()
    
