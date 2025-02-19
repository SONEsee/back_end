from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('lcicHome.urls', 'lcicHome'), namespace='lcic')),
    path('news/', include(('lcicNews.urls', 'lcicNews'), namespace='news')),
    path('api/', include('lcicHome.urls')),
<<<<<<< HEAD
    # path('sql/', include('sqlserver_models.urls')),
=======
    # path('sql/', include('ned_sql.urls')),
>>>>>>> 74493af0add209ff2657fc83bfc6762a869dd790
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
