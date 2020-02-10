from django.urls import path

from . import views

app_name = 'inventory'
urlpatterns = [
    # ex: /inventory/
    path('', views.index, name='index'),
    # ex: /inventory/cameras/
    path('cameras/', views.CamerasView.as_view(), name='cameras'),
    # ex: /inventory/cameras/5
    path('cameras/<int:pk>/', views.CameraDetailView.as_view(), name='camera_detail'),
    # ex: /inventory/servers/
    path('servers/', views.ServersView.as_view(), name='servers'),
    # ex: /inventory/servers/5
    path('servers/<int:pk>/', views.ServerDetailView.as_view(), name='server_detail'),
    # ex: /inventory/switches/
    path('switches/', views.SwitchesView.as_view(), name='switches'),
    # ex: /inventory/switches/5
    path('switches/<int:pk>/', views.SwitchDetailView.as_view(), name='switch_detail'),
    # ex: /inventory/create/
    path('create/', views.new_device, name='new_device'),
    # ex: /inventory/cameras/new
    path('cameras/new', views.CameraCreate.as_view(), name='camera-create'),
]
