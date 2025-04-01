from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('user/', include('users.urls', namespace='user')),
    path('', include('main.urls', namespace='main')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
