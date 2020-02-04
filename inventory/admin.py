from django.contrib import admin

from .models import CameraManufacturer, Server, Switch, IpAddress, Camera

admin.site.register(CameraManufacturer)
admin.site.register(Server)
admin.site.register(Switch)
admin.site.register(IpAddress)
admin.site.register(Camera)