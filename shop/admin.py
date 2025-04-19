from django.contrib import admin
from django.utils.html import format_html
from django.http import HttpRequest
# Register your models here.
from.models import Category, Product, Planting_method, Contact, Order, OrderItem
from .define import*
from .helpers import*


class CategoryAdmin (admin.ModelAdmin):
    list_display = ('name', 'status', 'is_homepage', 'ordering' )
    list_filter = ["is_homepage", "status"]
    search_fields = ["name"]
   # prepopulated_fields = { 'slug': ('name',)}
class ProductAdmin (admin.ModelAdmin):
    list_display = ('image_tag','name', 'status', 'ordering','category','special', 'price_formatted', 'price_sale_formatted','get_planting_method', 'total_sold' )
    list_filter = [ "status",'special' ]
    search_fields = ["name"]

    class Media:
       js = ADMIN_SRC_JS
    #    css = ADMIN_SRC_CSS
    @admin.display(description='Planting Method')
    def get_planting_method(self, obj):
        return "\n".join([p.name for p in obj.planting_method.all()])
    

    @admin.display(description='Price')
    def price_formatted(self,obj):
       return format_currency_vietnam(obj.price)
    @admin.display(description='Price_sale')
    def price_sale_formatted(self,obj):
        return format_currency_vietnam(obj.price_sale) if obj.price_sale else None
    @admin.display(description='Image')
    def image_tag(self, obj):
        return format_html('<img src="{}" width="50" height="50" />',obj.image.url)
   

class PlantingmethodAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'ordering' )
    list_filter = ["status"]
    search_fields = ["name"]

    class Media:
       js = ADMIN_SRC_JS
    #    css = ADMIN_SRC_CSS

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('name', 'email', 'phone','message', 'created' )
    fields = ('name', 'email', 'phone','message','contacted','message_admin', 'created' )
    list_display = ('name', 'email', 'phone','message','contacted','message_admin', 'created' )
    list_filter = ["contacted"]
    search_fields = ["name"]

    class Media:
       js = ADMIN_SRC_JS
    #    css = ADMIN_SRC_CSS  
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False  
    

class OrderItemINLINES(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('order','product','quantity','price','total','price_formatted', 'total_formatted')
    fields = ('order','product','quantity', 'price_formatted', 'total_formatted')

    can_delete = False
    
    def has_add_permission(self, request, obj=None):
        return False
    
    @admin.display(description='Total')
    def price_formatted(self,obj):
       return format_currency_vietnam(obj.price)
    
    @admin.display(description='Total') 
    def total_formatted(self,obj):
       return format_currency_vietnam(obj.total)    

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('code','name', 'email', 'phone','created','quantity', 'total_formatted', 'address', 'total' )
    fields = ('status','code','name', 'email', 'phone','created','quantity', 'total_formatted', 'address' )
    list_display = ('code','name', 'email', 'phone','created','quantity', 'total_formatted', 'status')
    list_filter = ["status"]
    search_fields = ["name"]
    list_editable = ['status']

    inlines = [OrderItemINLINES]
 
    class Media:
       js = ADMIN_SRC_JS
    #     css = ADMIN_SRC_CSS  
    def has_add_permission(self, request):
        return False
    @admin.display(description='Total')
    def total_formatted(self,obj):
       return format_currency_vietnam(obj.total)
    

    def save_model(self, request, obj, form, change):
         super().save_model(request, obj, form, change)
    
    
         if obj.status == 'finish':
                obj.update_total_sold()
            



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Planting_method, PlantingmethodAdmin) 
admin.site.register(Contact, ContactAdmin)
admin.site.register(Order, OrderAdmin)


admin.site.site_header = ADMIN_HEADER_NAME