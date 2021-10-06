from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # http://127.0.0.1:8000/admin/
    # python3 manage.py createsuperuser
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/auth/ 
    path("auth/", include('usuarios.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)