from django.contrib import admin

from .models import CameraManufacturer, Server, Subnet, IpAddress, PatchPanel, PatchPanelConnection, Camera

admin.site.register(CameraManufacturer)
admin.site.register(Server)
admin.site.register(Subnet)
admin.site.register(IpAddress)
admin.site.register(PatchPanel)
admin.site.register(PatchPanelConnection)
admin.site.register(Camera)