from django.contrib import admin

from .models import Server, Switch, IpAddress, Camera

admin.site.register(Server)
admin.site.register(Switch)
admin.site.register(IpAddress)
admin.site.register(Camera)