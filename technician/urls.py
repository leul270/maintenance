from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path("", views.home, name="tech_home"),
      path("detail/<str:pk>", views.detail, name="detail"),
           path("updateProfile/<str:pk>", views.updateProfile, name="updateProfile"),
            path("all-tasks", views.allTasks, name="allTasks"),
            path("<str:pk>", views.isFixed, name="isFixed"),
    
]