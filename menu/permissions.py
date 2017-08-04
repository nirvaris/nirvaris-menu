
from .models import Resource

from .mixins import _check_groups

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

def is_admin(user):

    for group in user.groups.all():

        if hasattr(group, 'is_admin'):
            if group.is_admin.it_is:
                return True

    return False
