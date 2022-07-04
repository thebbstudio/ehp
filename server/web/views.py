from urllib import response
from django.shortcuts import redirect, render
from django.db import connection
from .form import *
from .models import *
from django.http import HttpResponseRedirect


def EmployeePage(request):
    with connection.cursor() as cursor:
        # Запрос всех данных по сотрудникам
        cursor.execute('''SELECT 
                                ae."id",
                                "fullName", 
                                CASE WHEN "isMan" THEN 'Мужчина' ELSE  'Женщина' END,
                                CAST(date_part('year',age(ae."birthDay"::date)) as integer) as age,
                                coalesce(ap."name", 'Не определно'), 
                                coalesce(ac."name", 'Не определно')
                            FROM api_employee ae
                            left join api_position ap
                                on ae.position_id = ap.id
                                and ap."isDeleted" = False
                                and ap."isActive" = True
                            left join public."api_сategory" ac 
                                on ae.category_id = ac.id 
                            order by ae."id" ''')
        # Передача данных в Шаблон
        return render(request, 'Employee.html', {'employeeList' : cursor.fetchall()})


def AddEmployeePage(request):
    if request.method == "POST":
        # Создаём форма с данным с формы
        form = EmployeeForm(request.POST)

        # Сохраняем форму если валидная и передаём Created = True
        if form.is_valid():
            form.CustomInsert()
            return HttpResponseRedirect('/addEmployee/?created=True')
    else:
        # Если метод не POST то значит форма не сохраняется, 
        # а запрашивается нужна пустая форма
        form = EmployeeForm()
    
    # Передача данных в Шаблон
    return render(request, 'AddEmployee.html', {'form' : form})


def EditEmployeePage(request, id):
    employee = Employee()
    with connection.cursor() as cursor:
        #  Получаем Данные сотрудника
        cursor.execute('select * from public.api_employee ae where id = ' + str(id))
        employeeData = cursor.fetchone()

        #  Получаем Категорию сотрудника
        cursor.execute('select * from public."api_сategory" where id =  ' + str(employeeData[5]))
        category = cursor.fetchone()

        #  Получаем Должность сотрудника
        cursor.execute('select * from api_position where id = ' + str(employeeData[4]))
        position = cursor.fetchone()

        # Собираем сотрудника
        employee.SetData(employeeData[0], employeeData[1], 
                        employeeData[2], employeeData[3],
                        Position(employeeData[4], position[1]), 
                        Сategory(employeeData[5], category[1]))

    # Передаём в конструктор формы Сотрудника с заполеными данными или нет
    form = EmployeeForm(request.POST or None, instance=employee)

    # Если форма валидная, значит была заполена и происходит редирект на список сотрудников
    if form.is_valid():
        form.CustomUpdate()
        return redirect('employee')

    return render(request, 'EditEmployee.html', {'form':form})


def PositionPage(request):
    with connection.cursor() as cursor:
        # Выборка всех неудалённые должности С заменной значение isActive на более приемлемые
        cursor.execute('''  SELECT 
                                id,
                                name, 
                            case 
                              WHEN "isActive" 
                                then 'Активна'
                                else 'Неактивна' end
                           FROM public.api_position where "isDeleted" = False
                           order by id''')

        # Передача данных в Шаблон
        return render(request, 'Position.html', {'positionList' : cursor.fetchall()})


def AddPositionPage(request):
    # Создаём форма с данным с формы
    if request.method == "POST":
        form = PositionForm(request.POST)
        # Сохраняем форму если валидная и передаём Created = True
        if form.is_valid():
            form.CustomInsert()
            return HttpResponseRedirect('/addPosition/?created=True')
    else:
        # Если метод не POST то значит форма не сохраняется, 
        # а запрашивается нужна пустая форма
        form = PositionForm()
    
    # Передача данных в Шаблон
    return render(request, 'AddPosition.html', {'form' : form})


def EditPositionPage(request, id):
    position = Position()
    with connection.cursor() as cursor:
        #  Получаем данные должности
        cursor.execute('select * from api_position where "isDeleted" = False and id = ' + str(id))
        positionData = cursor.fetchone()
        # Собираем должности
        position.SetData(positionData[0], positionData[1], positionData[2])
        
    form = PositionForm(request.POST or None, instance=position)

    # Если форма валидная, значит сейчас данные сохраняем, и редиректим на список должностей
    if form.is_valid():
        form.CustomUpdate()
        return redirect('position')
    
    # Передача данных в Шаблон    
    return render(request, 'EditEmployee.html', {'form':form})
