from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    ip_address = models.CharField(max_length=50, unique=True)
    sw_version = models.CharField('Software version', max_length=200)


class Switch(models.Model):
    path = models.CharField(max_length=50, unique=True)


class Camera(models.Model):
    switch = models.ForeignKey(Switch, on_delete=models.SET('None'))
    server = models.ForeignKey(Server, on_delete=models.SET('None'), blank=True)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    firmware = models.CharField(max_length=200)
    ip_address = models.CharField('IP address', max_length=200, unique=True)