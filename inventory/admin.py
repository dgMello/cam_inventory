from django.contrib import admin

from .models import CameraManufacturer, Server, Subnet, IpAddress, Camera

admin.site.register(CameraManufacturer)
admin.site.register(Server)
admin.site.register(Subnet)
admin.site.register(IpAddress)
admin.site.register(Camera)