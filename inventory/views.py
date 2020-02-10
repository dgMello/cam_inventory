from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db import IntegrityError, DataError
from django.views import generic

from .models import Server, Subnet, Camera


def index(request):
    server_list = Server.objects.all()
    subnet_list = Subnet.objects.all()
    camera_list = Camera.objects.all()
    context = {
        'server_list': server_list,
        'switch_list': subnet_list,
        'camera_list': camera_list
    }
    return render(request, 'inventory/index.html', context)


class CamerasView(generic.ListView):
    model = Camera
    template_name = 'inventory/cameras.html'


class CameraDetailView(generic.DetailView):
    model = Camera
    template_name = 'inventory/camera_detail.html'


class CameraCreate(generic.edit.CreateView):
    model = Camera
    fields = ['make', 'model', 'firmware', 'subnet', 'ip_address', 'mac_address', 'default_plugin', 'h265_enabled',
              'four_k_resolution', 'ptz_caps', 'qualified', 'server']


class ServersView(generic.ListView):
    model = Server
    template_name = 'inventory/servers.html'


class ServerDetailView(generic.DetailView):
    model = Server
    template_name = 'inventory/server_detail.html'


class SwitchesView(generic.ListView):
    model = Server
    template_name = 'inventory/servers.html'


class SwitchDetailView(generic.DetailView):
    model = Subnet
    template_name = 'inventory/switch_detail.html'


def new_device(request, device=None):
    return render(request, 'inventory/new_device.html')
