from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def DeleteEmployee(request):
    if request.method != 'DELETE':
        return HttpResponse(status=400)

    return HttpResponse(status=200)
