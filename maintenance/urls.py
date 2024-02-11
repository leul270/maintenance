
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('base.urls')),
    path('technician/', include('technician.urls')),
    path("customer/",include('customer.urls'))
]
