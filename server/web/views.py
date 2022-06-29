from urllib import response
from django.shortcuts import render
from django.db import connection
from .form import *
from .models import *
from django.http import HttpResponseRedirect



def EmployeePage(request):
    #data = {'employeeList' : [{'id' : 1, 'fullName' : 'Sergey.Semkin', 'sex' : 'Man', 'age' : 22, 'position' : 'Programer', 'category' : 'Middel'},{'id' : 1, 'fullName' : 'Sergey.Semkin', 'sex' : 'Man', 'age' : 22, 'position' : 'Programer', 'category' : 'Middel'},{'id' : 1, 'fullName' : 'Sergey.Semkin', 'sex' : 'Man', 'age' : 22, 'position' : 'Programer', 'category' : 'Middel'},{'id' : 1, 'fullName' : 'Sergey.Semkin', 'sex' : 'Man', 'age' : 22, 'position' : 'Programer', 'category' : 'Middel'},{'id' : 1, 'fullName' : 'Sergey.Semkin', 'sex' : 'Man', 'age' : 22, 'position' : 'Programer', 'category' : 'Middel'},{'id' : 1, 'fullName' : 'Sergey.Semkin', 'sex' : 'Man', 'age' : 22, 'position' : 'Programer', 'category' : 'Middel'}]}
    data = []
    with connection.cursor() as cursor:
        cursor.execute('''SELECT 
                                ae."id",
                                "fullName", 
                                CASE WHEN "isMan" THEN 'Мужчина' ELSE  'Женщина' END,
                                CAST(date_part('year',age(ae."birthDay"::date)) as integer) as age,
                                ap."name", ac."name"
                            FROM api_employee ae
                            join api_position ap
                                on ae.position_id = ap.id
                            join public."api_сategory" ac 
                                on ae.category_id = ac.id  ''')
        for row in cursor.fetchall():
            data.append(row)
    return render(request, 'Employee.html', {'employeeList' : data})


def PositionPage(request):
    data = []
    with connection.cursor() as cursor:
        cursor.execute('''SELECT "id", "name" FROM public.api_position''')
        for row in cursor.fetchall():
            data.append(row)
        print(data)
    return render(request, 'Position.html', {'positionList' : data})


def AddEmployeePage(request):
    created = False
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/AddEmployee?created=True')
    else:
        if 'created' in request.GET:
            created = True
        form = EmployeeForm()
    return render(request, 'AddEmployee.html', {'form' : form})


def AddPositionPage(request):
    data = {}
    return render(request, 'AddPosition.html', data)

def EditEmployeePage(request, id):
    employee = Employee()
    with connection.cursor() as cursor:
        cursor.execute(''' select id, fullName, isMan, birthDay, position, category from api_employee where id = {id} ''')
        for row in cursor.fetchone()
    
    return render(request, 'AddEmployee.html', form)


def EditPositionPage(request, id):
    data = {}
    return render(request, 'AddPosition.html', data)
