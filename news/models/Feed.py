from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse


from news.helpers import*
from news.custom_field import*
from news.define import*


class Feed(models.Model):
   
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)
    link = models.CharField(max_length=250)
     
    class Meta:
        verbose_name_plural = TABLE_FEED_SHOW  

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("feed", kwargs={"feed_slug": self.slug})