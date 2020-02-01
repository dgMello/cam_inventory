from django.db import models


class Server(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    ip_address = models.CharField(max_length=50, unique=True)
    sw_version = models.CharField('software version', max_length=200)

    def __str__(self):
        return self.name


class Switch(models.Model):
    subnet = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.subnet


class Camera(models.Model):
    switch = models.ForeignKey(Switch, on_delete=models.SET(None))
    server = models.ForeignKey(Server, on_delete=models.SET_NULL, null=True, blank=True)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    firmware = models.CharField(max_length=200)
    ip_address = models.GenericIPAddressField(protocol='IPv4', unique=True)

    def __str__(self):
        return self.ip_address
