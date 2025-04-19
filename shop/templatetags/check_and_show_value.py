from django import template


register = template.Library()

@register.simple_tag
def check_and_show_value(value):
    if value:
        return value
    else:
        return ''
    
   