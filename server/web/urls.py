from django.conf.urls import url, include
from django.views.generic import RedirectView


from django.conf.urls.static import static
from django.conf import settings

from .views import *

urlpatterns = [
    url(r'^Employee/$', EmployeePage, name='employee'),
    url(r'^Position/$', PositionPage, name='position'),
    url(r'^AddEmployee/$', AddEmployeePage, name='addEmployee'),
    url(r'^AddPosition/$', AddPositionPage, name='addPosition'),
    url(r'^editemployee/(?P<id>)', EditEmployeePage),
    url(r'^editposition/(?P<id>)', EditPositionPage),
]