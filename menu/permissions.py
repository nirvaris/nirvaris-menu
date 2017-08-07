
from .models import Resource

def check_permission(resource, user):
    #pdb.set_trace()

    if user.is_superuser:
        return True

    if (resource.is_staff & user.is_staff) | \
        (resource.is_authenticated & user.is_authenticated()) | \
        (resource.is_anonymous | \
        check_groups(resource, user)):

        return True

    return False

def is_admin(user):

    for group in user.groups.all():

        if hasattr(group, 'is_admin'):
            if group.is_admin.it_is:
                return True
    return False

def check_groups(resource, user):
    for group in resource.groups.all():
        if user.groups.filter(name=group.name).exists():
            return True
    return False
