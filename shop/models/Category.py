from django.db import models
from django.urls import reverse


from shop.custom_field import*
from shop.define import*

class Category(models.Model):
   
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    is_homepage = CustomBooleanField()
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES,  default= APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = TABLE_CATEGORY_SHOW 

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("shop:category", kwargs={"category_slug": self.slug})