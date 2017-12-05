import pdb

from django import template
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.db.models import Q
from ..models import MenuItem, Resource
from ..permissions import check_permission

register = template.Library()

@register.filter
def has_permission(resource, user):
    if not Resource.objects.filter(name=resource).exists():
        return True

    resource = Resource.objects.get(name=resource)
    return check_permission(resource, user)


@register.inclusion_tag('tag-menu.html')
def menu_tag(user='', clicked_menu=None):
    if user == '':
        user = AnonymousUser()

    menu_items = []

    menu_parents = MenuItem.objects.filter(menu_parent__isnull=True)

    for menu_parent in menu_parents:
        is_to_show = False

        if check_permission(menu_parent, user):

            item = {}
            item['name'] = menu_parent.name
            item['url'] = menu_parent.url
            item['css_class'] = menu_parent.css_class

            if menu_parent.menu_children.filter(name=clicked_menu).exists():
                    item['is_open'] = True

            item['is_hidden'] = menu_parent.is_hidden
            item['menu_children'] = _menu_child(menu_parent, user, clicked_menu)
            menu_items.append(item)

    return {'menu_items':menu_items}

def _menu_child(parent, user, clicked_menu=None):
    menu_items = []
    
    menu_parents = MenuItem.objects.filter(menu_parent__id=parent.id)

    for menu_parent in menu_parents:
        if check_permission(menu_parent, user):

            item = {}
            item['name'] = menu_parent.name
            item['url'] = menu_parent.url
            item['css_class'] = menu_parent.css_class

            if menu_parent.name==clicked_menu:
                    item['is_open'] = True

            item['is_hidden'] = menu_parent.is_hidden
            item['menu_children'] = _menu_child(menu_parent, user)
            menu_items.append(item)

    return menu_items

@register.filter('is_external_url')
def is_external_url(text):
    if 'http' in text:
        return True
    return False