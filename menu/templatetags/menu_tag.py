#import pdb

from django import template
from django.conf import settings
from django.db.models import Q

from ..models import MenuItem

register = template.Library()

@register.inclusion_tag('tag-menu.html', takes_context=True)
def menu_tag(context):

    #pdb.set_trace()
    if 'request' in context:
        request = context['request']
        user = request.user
    else:
        user = AnonymousUser()

    menu_items = []

    q_obj = Q()
    q_obj &= Q(is_superuser=user.is_superuser) | Q(is_staff=user.is_staff) | Q(is_authenticated=user.is_authenticated()) | ~Q(is_anonymous=user.is_authenticated())

    menu_parents = MenuItem.objects.filter(menu_parent__isnull=True).filter(q_obj)

    for menu_parent in menu_parents:
        item = {}
        item['name'] = menu_parent.name
        item['url'] = menu_parent.url
        item['menu_children'] = _menu_child(menu_parent, user)
        menu_items.append(item)

    #pdb.set_trace()
    return {'menu_items':menu_items}

def _menu_child(parent, user):

    menu_items = []
    #pdb.set_trace()
    menu_parents = MenuItem.objects.filter(menu_parent__id=parent.id)

    for menu_parent in menu_parents:
        item = {}
        item['name'] = menu_parent.name
        item['url'] = menu_parent.url
        item['menu_children'] = _menu_child(menu_parent, user)
        menu_items.append(item)

    return menu_items
