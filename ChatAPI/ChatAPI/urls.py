from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from . import settings

schema_view = get_swagger_view(title='Django Chat API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace='users')),
    path('docs/', schema_view)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
