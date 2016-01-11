from django import template
from django.conf import settings

from ..models import MenuItem

register = template.Library()

@register.inclusion_tag('tag-menu.html')
def search_form_tag():
    menu_items = MenuItem.objects.all()
    return {'search_form':form, 'dictionary_url': NV_DICTIONARY_URL}
