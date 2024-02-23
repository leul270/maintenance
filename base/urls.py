from django.urls import path
from django.contrib.auth.views import LoginView
from .forms import UserLoginForm
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "customer_registration",
        views.customer_registration,
        name="customer_registration",
    ),
    path(
        "technician_registration",
        views.technician_registration,
        name="technician_registration",
    ),
    path('logout/', views.log_out, name='logout'),
    path(
        "administrator_registration",
        views.administrator_registration,
        name="administrator_registration",
    ),
    path("login/", views.login_user, name="login"), 
    path("signup_selection/", views.signup_selection, name="signup_selection"),
    path("user_home/<str:id>/", views.user_home, name="user_home"),
    path("technician_home/<str:id>/", views.technician_home, name="technician_home"),
    path(
        "administrator_home/<str:id>/",
        views.administrator_home,
        name="administrator_home",
    ),
    path(
        "login1",
        views.home,
        name="login1",
    ),
]
