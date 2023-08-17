from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('minalba/', include('minalba.urls')),
    path('vibra/', include('vibra.urls')),
    path('api/', include('api.urls'))
]
