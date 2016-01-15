from django import template
from django.conf import settings

from ..models import MenuItem

register = template.Library()

@register.inclusion_tag('tag-menu.html')
def search_form_tag():
    menu_items = MenuItem.objects.exclude(menu_parent__isnull=True).exclude(menu_parent__exact='')
    return {'menu_items':menu_items}
