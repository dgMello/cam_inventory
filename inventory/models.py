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


class Subnet(models.Model):
    subnet = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.subnet


class IpAddress(models.Model):
    ip_address = models.GenericIPAddressField(protocol='IPv4')

    def __str__(self):
        return self.ip_address


class PatchPanel(models.Model):
    name = models.CharField(max_length=10, primary_key=True)

    def __str__(self):
        return self.patch_panel


class PatchPanelConnection(models.Model):
    connection = models.CharField(max_length=10)
    patch_panel = models.ForeignKey(PatchPanel, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.patch_panel.name + "-" + self.connection


class Camera(models.Model):
    make = models.ForeignKey(CameraManufacturer, on_delete=models.SET_NULL, null=True)
    model = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    ip_address = models.OneToOneField(IpAddress, on_delete=models.SET_NULL, null=True)
    subnet = models.ForeignKey(Subnet, on_delete=models.SET_NULL, null=True)
    un_pw = models.CharField('username/password', max_length=20)
    firmware = models.CharField(max_length=20)
    mac_address = models.CharField(max_length=20)
    # Assigned user placeholder
    location = models.CharField(max_length=20)
    patch_panel_connection = models.ForeignKey(PatchPanelConnection, on_delete=models.SET_NULL, null=True)
    PLUGIN_CHOICES = [
        ('native', 'Native'),
        ('onvif', 'Onvif'),
    ]
    default_plugin = models.CharField(choices=PLUGIN_CHOICES, default='Onvif')
    h265_enabled = models.BooleanField()
    four_k_resolution = models.BooleanField('4k resolution')
    PTZ_CHOICES = [
        ('none', 'None'),
        ('m_ptz', 'Mechanical PTZ'),
        ('d_ptz', 'Digital PTZ')
    ]
    ptz_caps = models.CharField('ptz capabilities', choices=PTZ_CHOICES, default='None')
    qualified = models.BooleanField(default=False)
    server = models.ForeignKey(Server, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.CharField(max_length=200, blank=True)

    def __str__(self):
        make = self.make
        camera = make.manu_name + ' ' + self.model
        return camera
