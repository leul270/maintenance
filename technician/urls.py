from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path("", views.home, name="tech_home"),
      path("detail/<str:pk>/<str:parameter>/", views.detail, name="detail"),
           path("updateProfile/<str:pk>", views.updateProfile, name="updateProfile"),
            path("all-softwares", views.softwareTaks, name="softwareTasks"),
            path("all-networks", views.networkTaks, name='networkTaks'),
            path("all-maintenances", views.maintenanceTasks, name='maintenanceTasks'),
            path("<str:pk>", views.isFixed, name="isFixed"),
    
]