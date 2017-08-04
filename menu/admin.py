from django.contrib import admin

from .models import MenuItem, Resource, IsAdmin

admin.site.register(MenuItem)
admin.site.register(Resource)
admin.site.register(IsAdmin)
