from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

# swagger not support for Django >= 3.0
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Vgg API')

urlpatterns = [
    path('', schema_view),
    path('users/', include('users.api.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
