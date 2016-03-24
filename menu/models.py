from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.db import models

# Create your models here.

class MenuItem(models.Model):

    class Meta:
        ordering = ['display_order']

    name = models.CharField(max_length=70)
    url = models.CharField(max_length=255)
    menu_parent = models.ForeignKey('MenuItem', null=True, blank=True, related_name='menu_children')
    css_class = models.CharField(max_length=255)
    groups = models.ManyToManyField(Group)
    display_order = models.IntegerField()
    is_hidden = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Resource(models.Model):

    name = models.CharField(max_length=70, unique=True)
    groups = models.ManyToManyField(Group)
    is_hidden = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=False)
    is_anonymous = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name