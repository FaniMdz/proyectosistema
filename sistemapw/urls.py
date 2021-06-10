from django.contrib import admin
from django.urls import path, include

from django.config import settings
from django.config.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('viewparking/', include ('estacionamiento.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
