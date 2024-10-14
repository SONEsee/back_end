from django import urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(('lcicHome.urls','lcicHome'), namespace ='lcic')),
    path('news/',include(('lcicNews.urls','lcicNews'), namespace ='news')),
    path('api/', include('lcicHome.urls')),
    
    # path('pdfapp/', include('pdfapp.urls')),
    ] 
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
