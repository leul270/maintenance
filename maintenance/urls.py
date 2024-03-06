
from django.contrib import admin
from django.urls import path,include
from .views import home

admin.site.site_header = "Hawassa University ICT Coordinator Office"
admin.site.index_title = "Adminnistrator"


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path('accounts/', include('base.urls')),
    path('technician/', include('technician.urls')),
    path("customer/",include('customer.urls')),
    path("administrations/",include('administrator.urls'))
]
