from django import forms 
from django.forms import ModelForm, RadioSelect
from api.models import *
from django.db import connection


# Описание форма создания и редактирования сотрудника
class EmployeeForm(ModelForm):
    def CustomInsert(self):
        with connection.cursor() as cursor:
            cursor.execute(f'''INSERT INTO public.api_employee 
                                    ("fullName", "isMan", 
                                    "birthDay", category_id, position_id)
                                VALUES ('{self.instance.fullName}',
                                        {self.instance.isMan},
                                        '{self.instance.birthDay}',
                                        {self.instance.category_id},
                                        {self.instance.position_id});''')
    
    
    def CustomUpdate(self):
        with connection.cursor() as cursor:
            cursor.execute(f'''UPDATE public.api_employee
                                SET "fullName"='{self.instance.fullName}',
                                    "isMan"={self.instance.isMan}, 
                                    "birthDay"='{self.instance.birthDay}', 
                                    category_id={self.instance.category_id}, 
                                    position_id={self.instance.position_id}
                                WHERE id = {self.instance.id}''')
         

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
    def CustomInsert(self):
        with connection.cursor() as cursor:
            cursor.execute(f'''INSERT INTO public.api_position(
                                name, "isActive", "isDeleted")
                                VALUES ('{self.instance.name}', {self.instance.isActive}, False);''')
                                
    
    def CustomUpdate(self):
        with connection.cursor() as cursor:
            cursor.execute(f'''UPDATE public.api_position
	                              SET name = '{self.instance.name}', "isActive"={self.instance.isActive}
	                            WHERE id = {self.instance.id};''')


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