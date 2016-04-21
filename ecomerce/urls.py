from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('principal.urls')),
    url(r'^', include('login.urls', namespace ='login')),
    url(r'^', include('productos.urls', namespace = 'productos')),
    url(r'^', include('cliente.urls')),
    url(r'^', include('dashboard.urls', namespace='userprofiles'),),
    url(r'^noticias', include('blog.urls')),    
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
