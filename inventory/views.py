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


def camera_new(request):
    switch_list = Subnet.objects.all()
    server_list = Server.objects.all()
    context = {
        'switch_list': switch_list,
        'server_list': server_list
    }
    if request.method == 'GET':
        return render(request, 'inventory/camera_new.html', context)
    elif request.method == 'POST':
        selected_ip = request.POST['ip_address']
        selected_make = request.POST['make']
        selected_model = request.POST['model']
        selected_firmware = request.POST['firmware']
        selected_switch = Subnet.objects.get(subnet=request.POST['switch'])

        if request.POST['server'] == 'none':
            selected_server = None
        else:
            selected_server = Server.objects.get(ip_address=request.POST['server'])

        try:
            new_camera = Camera.objects.create(switch=selected_switch, server=selected_server, make=selected_make,
                                               model=selected_model, firmware=selected_firmware, ip_address=selected_ip)
        except IntegrityError:
            context['error_message'] = "Duplicate IP address. Select a different IP address."
            return render(request, 'inventory/camera_new.html', context)
        except DataError as e:
            context['error_message'] = "Invalid input."
            return render(request, 'inventory/camera_new.html', context)
        else:
            new_camera.save()
            return HttpResponseRedirect(reverse('cameras'))


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
