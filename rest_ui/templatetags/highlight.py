from django import template
import re
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def modulo(num, val):
    return num % val

@register.filter()
def highlight_yellow(text, value):
    if text is not None:
        # text = str(text)
        # src_str = re.compile(value, re.IGNORECASE)
        # str_replaced = src_str.sub(f"<span class=\"highlight\">{value}</span>", text)
        str_replaced = text.replace("<b>", "<b><span class=\"highlight\">").replace("</b>", "</b></span>")
    else:
        str_replaced = ''

    return mark_safe(str_replaced)