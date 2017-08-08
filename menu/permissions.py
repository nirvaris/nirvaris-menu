
from .models import Resource, MenuItem

def check_permission(resource, user):
    #pdb.set_trace()

    if user.is_superuser:
        return True

    if not resource:
        return False

    if isinstance(resource, str):
        if Resource.object.filter(name=resource).exists():
            resource = Resource.object.get(name=resource)

        if MenuItem.object.filter(name=resource).exists():
            resource = MenuItem.object.get(name=resource)

    if not (isinstance(resource, Resource) or isinstance(resource, MenuItem)):
        return False

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
