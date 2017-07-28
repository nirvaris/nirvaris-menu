
import pdb


from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse
from django.utils.translation import get_language_from_path
from .models import MenuItem

def _check_groups(menu, user):
    for group in menu.groups.all():
        if user.groups.filter(name=group.name).exists():
            return True
    return False

class MenuPermissionsMixin(object):

    def dispatch(self, request, *args, **kwargs):
        #pdb.set_trace()
        user = self.request.user

        path_info = self.request.path_info
        lg = get_language_from_path(path_info)

        #view_url = path_info.replace('/'+lg,'')
        view_url = path_info.split('/')[-1]
        if view_url:
            if not MenuItem.objects.filter(url=view_url).exists():
                raise PermissionDenied

            menu_item = MenuItem.objects.filter(url=view_url)[0]
            request.session['menu_item'] = menu_item.name

            if (menu_item.is_superuser & user.is_superuser) | \
                (menu_item.is_staff & user.is_staff) | \
                (menu_item.is_authenticated & user.is_authenticated()) | \
                (menu_item.is_anonymous | \
                _check_groups(menu_item, user)):

                return super(MenuPermissionsMixin, self).dispatch(request, *args, **kwargs)

        raise PermissionDenied
