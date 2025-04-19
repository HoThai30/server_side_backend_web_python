import re

from django import template
from django.utils.html import mark_safe
register = template.Library()

def highlight_shop(value,keyword):
    if not keyword:
        return value
    else:
        regex = re.compile(re.escape(keyword), re.IGNORECASE)
        return mark_safe( regex.sub(f'<span class = "highlight">{keyword}</span>',value))



register.filter('highlight_shop',highlight_shop)

