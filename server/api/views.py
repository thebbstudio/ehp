from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.db import connection


@csrf_exempt
def DeleteEmployee(request, id):
    # Если метод не DELETE, возвращаем ответ BadRequest 
    if request.method != 'DELETE':
        return HttpResponseBadRequest(JsonResponse({'msg':'Wrong Method'}))

    with connection.cursor() as cursor:
        # Делаем запрос на удаление
        cursor.execute('delete from api_employee where id = ' + str(id) + ' RETURNING id;')
    
    # Сообщаем, что всё хорошо
    return JsonResponse({'msg': 'Removal completed'})

@csrf_exempt
def DeletePosition(request, id):
    # Если метод не DELETE, возвращаем ответ BadRequest 
    if request.method != 'DELETE':
        return HttpResponseBadRequest(JsonResponse({'msg':'Wrong Method'}))

    with connection.cursor() as cursor:
        # Делаем запрос на удаление
        cursor.execute('delete from api_employee where id = ' + str(id) + ' RETURNING id;')

    # Сообщаем, что всё хорошо
    return JsonResponse({'msg': 'Removal completed'})
