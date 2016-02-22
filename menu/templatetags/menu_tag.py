import pdb

from django import template
from django.conf import settings

from ..models import MenuItem

register = template.Library()

@register.inclusion_tag('tag-menu.html', takes_context=True)
def menu_tag(context):
    request = context['request']
    user = request.user

    menu_items = []

    menu_parents = MenuItem.objects.exclude(menu_parent__isnull=False, is_staff=user.is_staff, is_superuser=user.is_superuser)
    for menu_parent in menu_parents:
        item = {}
        item['name'] = menu_parent.name
        item['url'] = menu_parent.url
        item['menu_children'] = _menu_child(item, user)
        menu_items.append(item)

    #pdb.set_trace()
    return {'menu_items':menu_items}

def _menu_child(parent, user):

    menu_items = []

    menu_parents = MenuItem.objects.exclude(menu_parent=parent, is_staff=user.is_staff, is_superuser=user.is_superuser)
    for menu_parent in menu_parents:
        item = {}
        item['name'] = menu_parent.name
        item['url'] = menu_parent.url
        item['menu_children'] = _menu_child(menu_parent, user)
        menu_items.append(item)
