from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the inventory index.")


def cameras(request):
    return HttpResponse("You're looking at the list of cameras.")


def camera_detail(request, camera_id):
    return HttpResponse("You're looking at camera %s." % camera_id)


def servers(request):
    return HttpResponse("You're looking at the list of servers.")


def server_detail(request, server_id):
    return HttpResponse("You're looking at server %s." % server_id)


def switches(request):
    return HttpResponse("You're looking at the list of switches.")


def switch_detail(request, switch_id):
    return HttpResponse("You're looking at switch %s." % switch_id)
