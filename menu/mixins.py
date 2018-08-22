
import pdb


from django.core.exceptions import PermissionDenied
from django.urls import reverse, resolve
from django.utils.translation import get_language_from_path

from .permissions import check_permission

from .models import MenuItem, Resource

class MenuPermissionsMixin(object):

    def dispatch(self, request, *args, **kwargs):
        #pdb.set_trace()
        path_info = request.path_info

        url_name = resolve(request.path_info).url_name
        user = request.user

        if MenuItem.objects.filter(url=url_name).exists():

            menu_item = MenuItem.objects.filter(url=url_name)[0]
            request.session['menu_item'] = menu_item.name

        if user.is_superuser:
            return super(MenuPermissionsMixin, self).dispatch(request, *args, **kwargs)

        if Resource.objects.filter(name=url_name).exists():
            resource = Resource.objects.get(name=url_name)
            if not check_permission(url_name, user):
                raise PermissionDenied

        if MenuItem.objects.filter(url=url_name).exists():

            menu_item = MenuItem.objects.filter(url=url_name)[0]
            request.session['menu_item'] = menu_item.name

            if not check_permission(menu_item,user):
                raise PermissionDenied

        return super(MenuPermissionsMixin, self).dispatch(request, *args, **kwargs)
