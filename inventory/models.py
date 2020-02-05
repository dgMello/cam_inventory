from django.db import models


class CameraManufacturer(models.Model):
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


class IpAddress(models.Model):
    switch_subnet = models.ForeignKey(Switch, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(protocol='IPv4')

    def __str__(self):
        return self.ip_address


class Camera(models.Model):
    make = models.ForeignKey(CameraManufacturer, on_delete=models.SET_NULL, null=True)
    model = models.CharField(max_length=200)
    firmware = models.CharField(max_length=200)
    ip_address = models.OneToOneField(IpAddress, on_delete=models.SET_NULL, null=True)
    mac_address = models.CharField(max_length=200)
    PLUGIN_CHOICES = [
        ('native', 'Native'),
        ('onvif', 'Onvif'),
    ]
    default_plugin = models.CharField(choices=PLUGIN_CHOICES, default='Onvif', max_length=200)
    h265_enabled = models.BooleanField()
    PTZ_CHOICES = [
        ('none', 'None'),
        ('m_ptz', 'Mechanical PTZ'),
        ('d_ptz', 'Digital PTZ')
    ]
    ptz_caps = models.CharField('ptz capabilities', choices=PTZ_CHOICES, default='None', max_length=200)
    qualified = models.BooleanField(default=False)
    server = models.ForeignKey(Server, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.ip_address.ip_address
