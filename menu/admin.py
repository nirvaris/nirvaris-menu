from django.contrib import admin

from .models import MenuItem, Resource, IsAdmin

def make_is_staff(modeladmin, request, queryset):
    queryset.update(is_published=True)

class MenuItemAdmin(admin.ModelAdmin):

    list_filter = ('name', 'url', 'menu_parent', 'css_class',  'display_order', 'is_hidden','is_superuser','is_staff','is_authenticated', 'is_anonymous')
    list_display = ('name', 'url', 'menu_parent', 'css_class',  'display_order', 'is_hidden','is_superuser','is_staff','is_authenticated', 'is_anonymous')
    list_editable = ('is_superuser','is_staff','is_authenticated', 'is_anonymous')
    #actions = [make_published]

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Resource)
admin.site.register(IsAdmin)
