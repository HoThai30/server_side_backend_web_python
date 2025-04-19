
from django import template
import locale

register = template.Library()

def format_currency_vietnam(number):
     locale.setlocale(locale.LC_ALL, 'vi_VN')
     formatted = locale.format_string("%d",number, grouping=True) +" đ"
     return formatted

register.filter('format_currency_vietnam', format_currency_vietnam)
   
