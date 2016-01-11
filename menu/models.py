from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=70)
    url = models.CharField(max_length=255)
    menu_parent = models.ForeignKey(MenuItem, null=True, blank=True, related_name='menu_children')
    is_hidden = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
