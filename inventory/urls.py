from django.urls import path

from . import views

urlpatterns = [
    # ex: /inventory/
    path('', views.index, name='index'),
    # ex: /inventory/cameras/
    path('cameras/', views.cameras, name='cameras'),
    # ex: /inventory/cameras/5
    path('cameras/<int:camera_id>/', views.camera_detail, name='camera_detail'),
    # ex: /inventory/servers/
    path('servers/', views.servers, name='servers'),
    # ex: /inventory/servers/5
    path('servers/<int:server_id>/', views.server_detail, name='server_detail'),
    # ex: /inventory/switches/
    path('switches/', views.switches, name='switches'),
    # ex: /inventory/switches/5
    path('switches/<int:switch_id>/', views.switch_detail, name='switch_detail'),
    # ex: /inventory/create/
    path('create/', views.new_device, name='new_device'),
]