from django import forms 
from django.forms import ModelForm, RadioSelect
from api.models import *


# Описание форма создания и редактирования сотрудника
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        # Описание полей формы
        widgets = {
            'fullName': forms.TextInput(attrs={'class': 'form-control'}),
            'isMan': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'birthDay': forms.DateInput(attrs={'class': 'form-control', 'type':'date'}),
            'position': forms.Select(attrs={'class': 'form-select form-select-lg mb-3'}),
            'category': forms.Select(attrs={'class': 'form-select form-select-lg mb-3'}),
        }
        # Описание лейблов около полей
        labels = {
            "fullName": "ФИО",
            "isMan" : "Мужчина",
            "birthDay" : "День рождения",
            "position" : "Должность",
            "category" : "Категория"
        }

# Описание форма создания и редактирования сотрудника
class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ['name', 'isActive']
        # Описание полей формы
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        # Описание лейблов около полей
        labels = {
            "name": "Название должности",
            "isActive": "Должность актина",
        }