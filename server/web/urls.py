from django.conf.urls import url, include
from django.views.generic import RedirectView


from django.conf.urls.static import static
from django.conf import settings

from .views import *

urlpatterns = [
    url(r'^employee/$', EmployeePage, name='employee'),
    url(r'^position/$', PositionPage, name='position'),
    url(r'^addEmployee/$', AddEmployeePage, name='addEmployee'),
    url(r'^addPosition/$', AddPositionPage, name='addPosition'),
    url(r'^editEmployee/(?P<id>\d+)', EditEmployeePage),
    url(r'^editPosition/(?P<id>\d+)', EditPositionPage),
    url(r'^.*$', RedirectView.as_view(url='/employee/', permanent=False), name='index')
]