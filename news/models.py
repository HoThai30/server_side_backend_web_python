from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse


from .helpers import*
from .custom_field import*
from .define import*

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

class Article(models.Model):
   
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.CharField(max_length=10, choices=APP_VALUE_STATUS_CHOICES, default=APP_VALUE_STATUS_DEFAULT)
    ordering = models.IntegerField(default=0)
    special = CustomBooleanField()
    publish_date = models.DateTimeField()
    content = HTMLField(null=True, blank=True)
    image = models.ImageField(upload_to=get_file_path)  # Thêm null=True, blank=True để tránh lỗi
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)  # Thêm null=True, blank=True để tránh lỗi migration

    class Meta:
        verbose_name_plural = TABLE_ARTICLE_SHOW  

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("article", kwargs={"article_slug": self.slug})

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
    
    