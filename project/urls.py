from django.contrib import admin
from django.urls import path, include





urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/', include('mathobsession.urls')),
    path('api/', include('jwt_auth.urls')),
    path('', include('frontend.urls'))
]
