from django.contrib import admin

# Register your models here.
from.models import Category, Article, Feed
from .define import*


class CategoryAdmin (admin.ModelAdmin):
    list_display = ('name', 'status', 'is_homepage', 'layout', 'ordering' )
    list_filter = ["is_homepage", "status","layout"]
    search_fields = ["name"]
   # prepopulated_fields = { 'slug': ('name',)}
class Media:
     js = ADMIN_SRC_JS
    # css = ADMIN_SRC_CSS
  
class ArticleAdmin (admin.ModelAdmin):
    list_display = ('name','category', 'status', 'ordering','special' )
    list_filter = [ "status", "special", "category"]
    search_fields = ["name"]
    # prepopulated_fields = { 'slug': ('name',)}
class Media:
     js = ADMIN_SRC_JS
    # css = ADMIN_SRC_CSS

class FeedAdmin (admin.ModelAdmin):
    list_display = ('name', 'status', 'ordering' )
    list_filter = [ "status"]
    search_fields = ["name"]
    prepopulated_fields = { 'slug': ('name',)}
class Media:
    js = ADMIN_SRC_JS
    # css = ADMIN_SRC_CSS

 

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Feed,FeedAdmin)
admin.site.site_header = ADMIN_HEADER_NAME