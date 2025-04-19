
from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse


from shop.helpers import*
from shop.custom_field import*
from shop.define import*
from .Category import Category
from .planting_method import Planting_method


class Product(models.Model):
   
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)
    special = CustomBooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    price_sale = models.DecimalField(max_digits=10, decimal_places=2, default=0,null=True, blank=True)
    price_real = models.DecimalField(max_digits=10, decimal_places=2, default=0,editable=False)
    total_sold = models.IntegerField(default=0,editable=False)
    sumary = models.TextField(null=True, blank=True)
    content = HTMLField(null=True, blank=True)
    image = models.ImageField(upload_to=get_file_path)  # Thêm null=True, blank=True để tránh lỗi
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)  # Thêm null=True, blank=True để tránh lỗi migration
    planting_method = models.ManyToManyField(Planting_method)
    class Meta:
        verbose_name_plural = TABLE_PRODUCT_SHOW  

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("shop:Product", kwargs={"Product_slug": self.slug, "Product_id": self.id})
    
    def save(self, *args, **kwargs):
       
        if  self.price_sale:
            self.price_real = self.price_sale
        else: self.price_real = self.price  

        super().save(*args, **kwargs)