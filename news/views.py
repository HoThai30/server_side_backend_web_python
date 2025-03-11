from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone
from .models import Category,Article,Feed
import re
import feedparser
import json
from bs4 import BeautifulSoup

from .define import *

def index(request):
    items_article_special = Article.objects.filter(special=True, status = APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date')[:SETTING_ARTICLE_TOTAL_ITEMS_SPECIAL]
    items_category = Category.objects.filter(status = APP_VALUE_STATUS_ACTIVE ,is_homepage=True).order_by('ordering')
    
    for category in items_category:
        category.article_filter =  category.article_set.filter (status = APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date')

    return render(request, APP_PATH_PAGES +'index.html',{
      "title_page": "trang chủ",
      "items_article_special":items_article_special,
      "items_category":items_category
    })

def category(request, category_slug):

    item_category =  get_object_or_404(Category, slug=category_slug, status=APP_VALUE_STATUS_ACTIVE)
    items_article = Article.objects.filter(category=item_category, status = APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date')
    
    # phân trang
    paginator = Paginator(items_article, SETTING_ARTICLE_TOTAL_ITEMS_PER_PAGE)
    page = request.GET.get('page')
    items_article = paginator.get_page(page)
   
   
    return render(request, APP_PATH_PAGES +'category.html',{
        "title_page": item_category.name,
        "item_category":item_category,
        "items_article":items_article,
        'paginator'    :paginator
        })

def article(request, article_slug):
    item_article =  get_object_or_404(Article, slug=article_slug, status=APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now())
    items_article_related = Article.objects.filter(category=item_article.category, status = APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date').exclude(slug=article_slug)[:SETTING_ARTICLE_TOTAL_ITEMS_RELATED]
    # items_article_Recently = Article.objects.filter(category=item_article.category, status = APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date')


    return render(request, APP_PATH_PAGES +'article.html',{
        "title_page": item_article.name,
         "item_article":item_article,
         "items_article_related":items_article_related,
        #  "items_article_Recently":items_article_Recently,
    })

def feed(request,feed_slug):
    item_feed =  get_object_or_404(Feed, slug=feed_slug, status=APP_VALUE_STATUS_ACTIVE)
    feed = feedparser.parse(item_feed.link)

    items_feed = []

    for entry in feed.entries:
        soup = BeautifulSoup(entry.summary, 'html.parser')
        img_tag = soup.find('img')
        src_img = APP_VALUE_IMAGES_DEFAULT

        if img_tag:
            src_img = img_tag['src']
        item = {
            'title': entry.title,
            'link': entry.link,
            'pub_date':entry.published,
            'img': src_img,
        }
    items_feed.append(item)
    return render(request,APP_PATH_PAGES + 'feed.html',{
        "title_page": item_feed.name,
        'items_feed':items_feed,
        'item_feed': item_feed,
    })



def search(request):
    keyword = request.GET.get('keyword')
    items_article = Article.objects.filter(name__iregex=re.escape(keyword), status = APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).order_by('-publish_date')
    paginator = Paginator(items_article, SETTING_ARTICLE_TOTAL_ITEMS_PER_PAGE)
    page = request.GET.get('page')
    items_article = paginator.get_page(page)

    return render(request, APP_PATH_PAGES +'search.html',{
        "title_page": "tìm kiếm từ khóa " +keyword,
        "items_article":items_article,
        "keyword":keyword,
        'paginator'    :paginator

    })

def about(request):
    

    return render(request,APP_PATH_PAGES + 'about.html',{
        "title_page": "Giới thiệu ",

    })
def contact(request):
    
    return render(request, APP_PATH_PAGES +'contact.html',{
        "title_page": "liên hệ ",

    })