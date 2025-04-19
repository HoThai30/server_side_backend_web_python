from django.shortcuts import render, get_object_or_404, redirect

import re

from .define import *
from .models import *
from .helpers import *
from .forms import CheckoutForm, ContactForm  # Import the Checkout and ContactForm if they exist in forms.py
from django.core.paginator import Paginator
from django.urls import reverse
# Create your views here.
def index(request):
#     items_article_special = Article.objects.filter(special=True, status = APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date')[:SETTING_ARTICLE_TOTAL_ITEMS_SPECIAL]
    items_category = Category.objects.filter(status = APP_VALUE_STATUS_ACTIVE ,is_homepage=True).order_by('ordering')
    
    for category in items_category:
        category.Product_filter =  category.product_set.filter (status = APP_VALUE_STATUS_ACTIVE, special=True).order_by('ordering')[:SETTING_PRODUCT_TOTAL_ITEMS_SPECIAL_INDEX]

    items_product_latest = Product.objects.filter(status = APP_VALUE_STATUS_ACTIVE).order_by('-id')[:SETTING_PRODUCT_TOTAL_ITEMS_LATEST_INDEX]
    items_product_latest= chunked(items_product_latest, SETTING_PRODUCT_TOTAL_ITEMS_PER_SLIDE)

    items_product_hot = Product.objects.filter(status = APP_VALUE_STATUS_ACTIVE).order_by('total_sold')[:SETTING_PRODUCT_TOTAL_ITEMS_HOT_INDEX]
    items_product_hot= chunked(items_product_hot, SETTING_PRODUCT_TOTAL_ITEMS_PER_SLIDE)

    items_product_ramdom = Product.objects.filter(status = APP_VALUE_STATUS_ACTIVE).order_by('?')[:SETTING_PRODUCT_TOTAL_ITEMS_RAMDOM_INDEX]
    items_product_ramdom= chunked(items_product_ramdom, SETTING_PRODUCT_TOTAL_ITEMS_PER_SLIDE)
   
    return render(request, APP_PATH_PAGES +'index.html',{
      "title_page": "trang chủ",
      "items_product_latest":items_product_latest,
      "items_product_hot":items_product_hot,
      "items_product_ramdom":items_product_ramdom,
      "items_category":items_category
    })
def product(request, Product_slug, Product_id):
    item_product = get_object_or_404(Product,id=Product_id, slug=Product_slug, status = APP_VALUE_STATUS_ACTIVE)

    items_product_related = Product.objects.filter(category=item_product.category, status = APP_VALUE_STATUS_ACTIVE).order_by('-id').exclude(id=Product_id)[:SETTING_PRODUCT_TOTAL_ITEMS_RELATED]
    
    
    return render(request, APP_PATH_PAGES +'detail.html',{
      "title_page": item_product.name,
      "item_product":item_product,
      "items_product_related":items_product_related,
    }) 

def category(request, category_slug='shop'):
    item_category = None
    if category_slug !='shop':
        item_category = get_object_or_404(Category, slug=category_slug, status = APP_VALUE_STATUS_ACTIVE)
   
    params = {
        'order': request.GET.get('order') if request.GET.get('order') == 'price' else '-price',
        'minPrice': request.GET.get('minPrice',''),
        'maxPrice': request.GET.get('maxPrice',''),
        'planting': request.GET.get('planting',''),
        'keyword': request.GET.get('keyword',''),

    }
   
    items_product = Product.objects.filter(status = APP_VALUE_STATUS_ACTIVE).order_by(params['order'] + '_real')
    
    if item_category:
        items_product = items_product.filter(category = item_category)
    if params['minPrice']:
        items_product = items_product.filter(price_real__gte = params['minPrice'])
    if params['maxPrice']:
        items_product = items_product.filter(price_real__lte = params['maxPrice'])
    if params['planting']:
        items_product = items_product.filter(planting_method__id = params['planting'])
    if params['keyword']:
        items_product = items_product.filter(name__iregex=re.escape(params['keyword']))

    item_product = items_product.count()
     # phân trang
    paginator = Paginator(items_product, SETTING_PRODUCT_TOTAL_ITEMS_PER_PAGE)
    page = request.GET.get('page')
    items_product = paginator.get_page(page)    


    items_category = Category.objects.filter(status = APP_VALUE_STATUS_ACTIVE ).order_by('ordering')[:SETTING_CATEGORY_TOTAL_ITEMS_SIDEBAR]
    
    items_planting_methods = Planting_method.objects.filter(status = APP_VALUE_STATUS_ACTIVE ).order_by('ordering')[:SETTING_PLANTING_METHOD_TOTAL_ITEMS_SIDEBAR]

    items_product_latest = Product.objects.filter(status = APP_VALUE_STATUS_ACTIVE).order_by('-id')[:SETTING_PRODUCT_TOTAL_ITEMS_LATEST_SIDEBAR]
    items_product_latest= chunked(items_product_latest, SETTING_PRODUCT_TOTAL_ITEMS_PER_SLIDE)

    return render(request, APP_PATH_PAGES +'category.html',{
      "title_page": item_category.name if item_category else "Cửa hàng",
      "item_category":item_category,
      "items_product":items_product,
      'params'       :params,
      "items_category":items_category,
      "items_planting_methods":items_planting_methods,
      "paginator": paginator,
      "items_product_latest":items_product_latest,
      "item_product":item_product,
    })
def cart(request): 
    items_product_cart      = []
    total_price             = 0

    if 'cart' in request.session:
        cart = request.session['cart']

        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)
            
            item_price = product.price_real * quantity
            total_price += item_price

            cart_item = {
                'id': product_id,
                'product': product,
                'quantity': quantity,
                'item_price': item_price,
            }
            items_product_cart.append(cart_item)
       
        

    return render(request, APP_PATH_PAGES +'cart.html',{
        "title_page": "Giỏ hàng",
        "items_product_cart":items_product_cart,
        'total_price': total_price, 
    })


def checkout(request):
    cart = request.session.get('cart', {})
    form = CheckoutForm ()
    if not cart:
        absolute_url = request.build_absolute_uri(reverse('shop:cart')) 
        return redirect(absolute_url)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)#validate

        if form.is_valid():
               return checkout_post(request, form, cart)   
            
    items_product_checkout      = []
    total_price                 = 0

    for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)
            name = product.name
            
            total = product.price_real * quantity
            total_price += total
    
            cart_item = {
                'name': name,
                'total': total,
                'quantity': quantity,
            }
            items_product_checkout.append(cart_item)

    return render(request, APP_PATH_PAGES +'checkout.html',{
        "title_page": "Thanh Toán",
        "items_product_checkout":items_product_checkout,
        'total_price': total_price,
        'form': form,
    })


def checkout_post(request, form, cart):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        address = form.cleaned_data['address']

        code = get_order_code()
        # Tạo đơn hàng
        order = Order.objects.create( code = code, name = name, email = email, phone = phone, address = address,)
    
        total_order = 0

        quantity_order = 0
    # # Lưu lại giỏ hàng vào đơn hàng
        for product_id, quantity in cart.items():

            product = Product.objects.get(id=product_id)

            price = product.price_real 

            total = price * quantity

            OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price, total=total)# # Tạo OrderItem cho từng sản phẩm trong giỏ hàng
                
            total_order += total
            quantity_order += quantity
        order.total = total_order
        order.quantity = quantity_order
        order.save()    
            
        # Xóa giỏ hàng sau khi đặt hàng thành công
        del request.session['cart']
        absolute_url = request.build_absolute_uri(reverse('shop:success')) + '?t=order'
        return redirect(absolute_url)    


def success(request):
    notify = NOTIFY_ORDER_SUCCESS
    if request.GET.get('t') == 'contact':
        notify = NOTIFY_CONTAC_SUCCESS

    return render(request, APP_PATH_PAGES +'success.html',{
        "title_page": "Đặt hàng thành công",
        'notify': notify,
    })



def add_to_cart(request): 

    if request.method == 'POST':
        product_id = request.POST.get('id')
        quantity = request.POST.get('quantity')

        if 'cart' not in request.session:
            request.session['cart'] = {}
            
        cart = request.session['cart']
        if product_id in cart:
            cart[product_id] += int(quantity)
        else:
            cart[product_id] = int(quantity)
        if 'null' in cart:
            del cart['null']
        # # Lưu lại giỏ hàng vào session
        request.session.modified = True  
        
    absolute_url = request.build_absolute_uri(reverse('shop:cart'))
    return redirect(absolute_url)

def update_cart(request): 
    action = request.GET.get('action')
    product_id = request.GET.get('productId')

    product_id = str(product_id)

    cart = request.session.get('cart', {})

    if product_id in cart:
      if action == 'decrease':
          if cart[product_id] > 1:
              cart[product_id] -= 1
          else:
              del cart[product_id]
      elif action == 'increase':
          cart[product_id] += 1    
      elif action == 'delete':
            del cart[product_id]
    # Lưu lại giỏ hàng vào session
    request.session['cart'] = cart


    absolute_url = request.build_absolute_uri(reverse('shop:cart'))
    return redirect(absolute_url)


def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return contact_post(request, form)
             
    return render(request, APP_PATH_PAGES +'contact.html', {
        "title_page": "Liên hệ",
        'form': form,
    })
def contact_post(request, form):
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    phone = form.cleaned_data['phone']
    message = form.cleaned_data['message']
    contacted = False
    Contact.objects.create(name=name, email=email, phone=phone, message=message, contacted=contacted)

    absolute_url = request.build_absolute_uri(reverse('shop:success')) + '?t=contact'
    return redirect(absolute_url)


def check_order(request):
    if request.method == 'POST':
       return check_order_post(request)
    return render(request, APP_PATH_PAGES +'check-order.html', {
        "title_page": "Kiểm tra đơn hàng",
    })


def check_order_post(request):
    code_order = request.POST.get('code', "")
    error_message = None
    item_order = None
    
    code_order = code_order.strip()
    if code_order == "":
        error_message = NOTIFY_ORDER_CHECK_NOT_EXIST
    else:
        try:
            item_order = Order.objects.get(code=code_order)
        except Order.DoesNotExist:
            error_message = NOTIFY_ORDER_CHECK_NOT_NULL

    return render(request, APP_PATH_PAGES +'check-order.html', {
        "title_page": "Kiểm tra đơn hàng",
        'item_order': item_order,
        'error_message': error_message,
        'code_order': code_order,
    })
    
   