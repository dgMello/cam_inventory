from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db import IntegrityError

from .models import Server, Switch, Camera


def index(request):
    server_list = Server.objects.all()
    switch_list = Switch.objects.all()
    camera_list = Camera.objects.all()
    context = {
        'server_list': server_list,
        'switch_list': switch_list,
        'camera_list': camera_list
    }
    return render(request, 'inventory/index.html', context)


def cameras(request):
    camera_list = Camera.objects.all()
    context = {
        'camera_list': camera_list
    }
    return render(request, 'inventory/cameras.html', context)


def camera_detail(request, camera_id):
    camera = get_object_or_404(Camera, pk=camera_id)
    return render(request, 'inventory/camera_detail.html', {'camera': camera})


def camera_new(request):
    switch_list = Switch.objects.all()
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
        selected_switch = Switch.objects.get(path=request.POST['switch'])

        if request.POST['server'] is None:
            selected_server = None
        else:
            selected_server = Server.objects.get(ip_address=request.POST['server'])

        try:
            new_camera = Camera.objects.create(switch=selected_switch, server=selected_server, make=selected_make,
                                               model=selected_model, firmware=selected_firmware, ip_address=selected_ip)
        except IntegrityError:
            context['error_message'] = "You didn't select a choice."
            return render(request, 'inventory/camera_new.html', context)
        else:
            new_camera.save()
            return HttpResponseRedirect(reverse('cameras'))


def servers(request):
    server_list = Server.objects.all()
    context = {
        'server_list': server_list
    }
    return render(request, 'inventory/servers.html', context)


def server_detail(request, server_id):
    server = get_object_or_404(Server, pk=server_id)
    return render(request, 'inventory/server_detail.html', {'server': server})


def switches(request):
    switch_list = Switch.objects.all()
    context = {
        'switch_list': switch_list
    }
    return render(request, 'inventory/switches.html', context)


def switch_detail(request, switch_id):
    switch = get_object_or_404(Switch, pk=switch_id)
    return render(request, 'inventory/switch_detail.html', {'switch': switch})


def new_device(request, device=None):
    return render(request, 'inventory/new_device.html')
