from .models import Category, Article, Feed

from .define import *
from django.db.models import Count
from django.utils import timezone

import requests

def items_category_sidebar_menu (request):
    items_category_sidebar_menu = Category.objects.filter(status = APP_VALUE_STATUS_ACTIVE ).order_by('ordering').annotate(num_article = Count('article'))[:SETTING_CATEGORY_TOTAL_ITEMS_SIDEBAR ]

    return{
        "items_category_sidebar_menu":items_category_sidebar_menu
    }

def items_feed_sidebar_menu (request):
    items_feed_sidebar_menu = Feed.objects.filter(status = APP_VALUE_STATUS_ACTIVE ).order_by('ordering')[:SETTING_FEED_TOTAL_ITEMS_SIDEBAR]

    return{
        "items_feed_sidebar_menu":items_feed_sidebar_menu
    }
def items_article_sidebar_recent (request):
    skip_slug = request.get_full_path().replace("/article/","")
    items_article_sidebar_recent=Article.objects.filter( status = APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).exclude(slug=skip_slug).order_by('-publish_date')[:SETTING_ARTICLE_TOTAL_ITEMS_RECENT]

    return{
        'items_article_sidebar_recent':items_article_sidebar_recent
     }
def items_article_sidebar_ramdom (request):
    skip_slug = request.get_full_path().replace("/article/","")
    items_article_sidebar_ramdom=Article.objects.filter( status = APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).exclude(slug=skip_slug).order_by('?')[:SETTING_ARTICLE_TOTAL_ITEMS_RAMDOM]

    return{
        'items_article_sidebar_ramdom':items_article_sidebar_ramdom
     }
def items_article_header_trending (request):
    skip_slug = request.get_full_path().replace("/article/","")
    items_article_header_trending=Article.objects.filter( status = APP_VALUE_STATUS_ACTIVE, publish_date__lte = timezone.now()).exclude(slug=skip_slug).order_by('?')[:1]

    return{
        'items_article_header_trending':items_article_header_trending
     }
def items_price_sidebar_coin (request):
    url = SETTING_API_LINK_PRICE_COIN
    items_price_sidebar_coin = []
    response = requests.get(url)
    if response.status_code == 200:
        items_price_sidebar_coin = response.json()[:SETTING_PRICE_COIN_TOTAL_ITEMS]
    

    return{
        'items_price_sidebar_coin':items_price_sidebar_coin
    }
def items_price_sidebar_gold (request):
    url = SETTING_API_LINK_PRICE_GOLD
    items_price_sidebar_gold = []
    response = requests.get(url)
    if response.status_code == 200:
        items_price_sidebar_gold = response.json()[:SETTING_PRICE_GOLD_TOTAL_ITEMS]
    

    return{
        'items_price_sidebar_gold':items_price_sidebar_gold
    }
     
