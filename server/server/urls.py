from django.conf.urls import url, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('api/', include('api.urls')),
    url('admin/', include('api.urls')),
] 

urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += url('', include('web.urls')).url_patterns