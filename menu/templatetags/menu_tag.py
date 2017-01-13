import pdb

from django import template
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.db.models import Q
from ..mixins import _check_groups
from ..models import MenuItem, Resource

register = template.Library()

@register.filter
def has_permission(resource, user):
    #pdb.set_trace()

    if not Resource.objects.filter(name=resource).exists():
        return False

    resource = Resource.objects.get(name=resource)

    if (resource.is_superuser & user.is_superuser) | \
        (resource.is_staff & user.is_staff) | \
        (resource.is_authenticated & user.is_authenticated()) | \
        (resource.is_anonymous | \
        _check_groups(resource, user)):

        return True

    return False

@register.inclusion_tag('tag-menu.html')
def menu_tag(user):

    #pdb.set_trace()
    #request = context['request']
    #user = request.user
    if user == '':
        user = AnonymousUser()

    menu_items = []

    menu_parents = MenuItem.objects.filter(menu_parent__isnull=True)

    for menu_parent in menu_parents:
        is_to_show = False
        if (menu_parent.is_superuser & user.is_superuser) | \
            (menu_parent.is_staff & user.is_staff) | \
            (menu_parent.is_authenticated & user.is_authenticated()) | \
            (menu_parent.is_anonymous | \
            _check_groups(menu_parent, user)):

            item = {}
            item['name'] = menu_parent.name
            item['url'] = menu_parent.url
            item['css_class'] = menu_parent.css_class
            item['menu_children'] = _menu_child(menu_parent, user)
            menu_items.append(item)

    #pdb.set_trace()
    return {'menu_items':menu_items}

def _menu_child(parent, user):

    menu_items = []

    menu_parents = MenuItem.objects.filter(menu_parent__id=parent.id)

    for menu_parent in menu_parents:
        if (menu_parent.is_superuser & user.is_superuser) | \
            (menu_parent.is_staff & user.is_staff) | \
            (menu_parent.is_authenticated & user.is_authenticated()) | \
            (menu_parent.is_anonymous | \
            _check_groups(menu_parent, user)):

            item = {}
            item['name'] = menu_parent.name
            item['url'] = menu_parent.url
            item['css_class'] = menu_parent.css_class
            item['menu_children'] = _menu_child(menu_parent, user)
            menu_items.append(item)

    return menu_items
