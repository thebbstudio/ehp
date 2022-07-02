from django import forms 
from django.forms import ModelForm, RadioSelect

from api.models import *

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            'fullName': forms.TextInput(attrs={'class': 'form-control'}),
            'isMan': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'birthDay': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'position': forms.Select(attrs={'class': 'form-select form-select-lg mb-3'}),
            'category': forms.Select(attrs={'class': 'form-select form-select-lg mb-3'}),
        }
        labels = {
            "fullName": "ФИО",
            "isMan" : "Мужчина",
            "birthDay" : "День рождения",
            "position" : "Должность",
            "category" : "Категория"
        }

class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ['name', 'isActive']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            "name": "Название должности",
            "isActive": "Должность актина",
        }