from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns=[
    path("customer_home/", views.customer_home, name="customer_home"),
    path("maintenance/", views.maintenance, name="maintenance"),
    path("maintenanceForm/", views.maintenance_form, name="maintenanceForm"),

    path("network/", views.network, name="network"),
    path("network_form/", views.network_form, name="network_form"),

    path("software/", views.software, name="software"),
    path("network_form/", views.network_form, name="network_form"),



]