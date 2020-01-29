from django.contrib import admin

from .models import Server, Switch, Camera

admin.site.register(Server)
admin.site.register(Switch)
admin.site.register(Camera)