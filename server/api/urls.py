from django.conf.urls import url

from django.conf.urls.static import static
from django.conf import settings
from .views import DeleteEmployee


urlpatterns = [
    url('', DeleteEmployee),
] 



