from urllib import response
from django.shortcuts import redirect, render
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
                                and ap."isDeleted" = False
                            join public."api_сategory" ac 
                                on ae.category_id = ac.id 
                            order by ae."id" ''')
        for row in cursor.fetchall():
            data.append(row)
    return render(request, 'Employee.html', {'employeeList' : data})


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

def EditEmployeePage(request, id):
    employee = Employee()
    with connection.cursor() as cursor:
        print('id', str(id))
        cursor.execute('select * from public.api_employee ae where id = ' + str(id))
        employeeData = cursor.fetchone()
        print('employeeData', employeeData)
        cursor.execute('select * from public."api_сategory" where id =  ' + str(employeeData[5]))
        category = cursor.fetchone()
        print(category)

        cursor.execute('select * from api_position where id = ' + str(employeeData[4]))
        position = cursor.fetchone()
        print(position)

        employee.id = employeeData[0]
        employee.fullName = employeeData[1]
        employee.isMan = employeeData[2]
        employee.birthDay = employeeData[3]
        employee.position = Position(employeeData[4], position[1])

        employee.category = Сategory(employeeData[5], category[1])
        
    form = EmployeeForm(request.POST or None, instance=employee)

    if form.is_valid():
        form.save()
        return redirect('employee')
    return render(request, 'EditEmployee.html', {'form':form})


def PositionPage(request):
    data = []
    with connection.cursor() as cursor:
        cursor.execute('''SELECT 
                            id,
                            name, 
                            case 
                              WHEN "isActive" 
                                then 'Активна'
                                else 'Неактивна' end
                           FROM public.api_position where "isDeleted" = False
                           order by id''')
        for row in cursor.fetchall():
            data.append(row)
        print(data)
    return render(request, 'Position.html', {'positionList' : data})


def AddPositionPage(request):
    created = False
    if request.method == "POST":
        form = PositionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/AddPosition?created=True')
    else:
        if 'created' in request.GET:
            created = True
        form = PositionForm()
    return render(request, 'AddPosition.html', {'form' : form})


def EditPositionPage(request, id):
    position = Position()
    with connection.cursor() as cursor:
        cursor.execute('select * from api_position where "isDeleted" = False and id = ' + str(id))
        positionData = cursor.fetchone()

        position.id = positionData[0]
        position.name = positionData[1]
        position.isActive = positionData[2]

        
    form = PositionForm(request.POST or None, instance=position)

    if form.is_valid():
        form.save()
        return redirect('position')
    return render(request, 'EditEmployee.html', {'form':form})
