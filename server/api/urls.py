from django.conf.urls import url

from django.conf.urls.static import static
from django.conf import settings
from .views import DeleteEmployee, DeletePosition


urlpatterns = [
    url(r'^deleteEmployee/(?P<id>\d+)', DeleteEmployee),
    url(r'^deletePosition/(?P<id>\d+)', DeletePosition),
] 



