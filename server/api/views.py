from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.db import connection


@csrf_exempt
def DeleteEmployee(request, id):
    if request.method != 'DELETE':
        return HttpResponseBadRequest(JsonResponse({'msg':'Wrong Method'}))
    print('delete employee id ',id)
    with connection.cursor() as cursor:
        cursor.execute('delete from api_employee where id = ' + str(id) + ' RETURNING id;')
        print(cursor.fetchall())

    return JsonResponse({'msg': 'Removal completed'})

@csrf_exempt
def DeletePosition(request, id):
    if request.method != 'DELETE':
        return HttpResponseBadRequest(JsonResponse({'msg':'Wrong Method'}))
    
    with connection.cursor() as cursor:
        cursor.execute('delete from api_employee where id = ' + str(id) + ' RETURNING id;')
        print(cursor.fetchall())

    return JsonResponse({'msg': 'Removal completed'})
