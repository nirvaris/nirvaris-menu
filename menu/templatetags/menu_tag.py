import pdb

from django import template
from django.conf import settings

from ..models import MenuItem

register = template.Library()

@register.inclusion_tag('tag-menu.html')
def menu_tag():
    menu_items = MenuItem.objects.exclude(menu_parent__isnull=False)

    pdb.set_trace()
    return {'menu_items':menu_items}
