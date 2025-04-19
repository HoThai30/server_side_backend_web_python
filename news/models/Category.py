from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse


from news.helpers import*
from news.custom_field import*
from news.define import*

class Category(models.Model):
   
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    is_homepage = CustomBooleanField()
    layout = models.CharField(max_length=10, choices=APP_VALUE_LAYOUT_CHOICE , default= APP_VALUE_LAYOUT_DEFAULT)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES,  default= APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = TABLE_CATEGORY_SHOW 

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("category", kwargs={"category_slug": self.slug})