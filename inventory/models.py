from django.db import models


class Manufacturer(models.Model):
    manu_name = models.CharField('manufacturer name', max_length=20, primary_key=True)

    def __str__(self):
        return self.manu_name


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


class HostId(models.Model):
    switch_subnet = models.ForeignKey(Switch, on_delete=models.CASCADE)
    host_id = models.IntegerField()

    def __str__(self):
        return self.host_id

    @property
    def full_ip_address(self):
        """Returns the fill IP address."""
        return '%s .%s' % (self.switch_subnet, str(self.host_id))


class IpAddress(models.Model):
    ip_address = models.GenericIPAddressField(protocol='IPv4')

    def __str__(self):
        return self.ip_address


class Camera(models.Model):
    switch = models.ForeignKey(Switch, on_delete=models.SET(None))
    server = models.ForeignKey(Server, on_delete=models.SET_NULL, null=True, blank=True)
    make = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    model = models.CharField(max_length=200)
    firmware = models.CharField(max_length=200)
    ip_address = models.GenericIPAddressField(protocol='IPv4', unique=True)
    mac_address = models.CharField(max_length=200)
    PLUGIN_CHOICES = [
        ('arecont', 'Arecont'),
        ('axis', 'Axis'),
        ('dahua', 'Dahua'),
        ('hikvision', 'Hikvision'),
        ('onvif', 'Onvif'),
        ('panasonic', 'Panasonic'),
        ('samsung', 'Samsung'),
        ('sony', 'Sony'),
        ('truvision', 'TruVision')
    ]
    default_plugin = models.CharField(choices=PLUGIN_CHOICES, default='Onvif', max_length=200)
    h265_enabled = models.BooleanField()
    PTZ_CHOICES = [
        ('none', 'None'),
        ('m_ptz', 'Mechanical PTZ'),
        ('d_ptz', 'Digital PTZ')
    ]
    ptz_caps = models.CharField(choices=PTZ_CHOICES, default='None', max_length=200)

    def __str__(self):
        return self.ip_address
