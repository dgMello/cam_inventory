from django.db import models


class Server(models.Model):
    model = models.CharField(max_length=200)
    ip_address = models.CharField(max_length=200)


class Switch(models.Model):
    path = models.CharField(max_length=200)


class Camera(models.Model):
    switch = models.ForeignKey(Switch, on_delete=models.SET('None'))
    server = models.ForeignKey(Server, on_delete=models.SET('None'))
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    firmware = models.CharField(max_length=200)
    ip_address = models.CharField('IP address', max_length=200)