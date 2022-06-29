from django import forms 
from django.forms import ModelForm

from api.models import *


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"