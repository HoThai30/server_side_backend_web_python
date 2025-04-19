from django import template
import locale
from django.utils.safestring import mark_safe

register = template.Library()
@register.simple_tag
def check_and_show_error(errors):
    xhtml = ''
    if errors:
         xhtml += "<div class='error-message'>{}</div>".format(errors)
    return mark_safe(xhtml)