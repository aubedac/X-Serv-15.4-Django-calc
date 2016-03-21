from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def suma(request, oper1, oper2):
    suma = int(oper1) + int(oper2)

    return HttpResponse(oper1 + " + " + oper2  + " = " + str(suma))

def resta(request, oper1, oper2):
     resta = int(oper1) - int(oper2)

     return HttpResponse(oper1 + " - " + oper2  + " = " + str(resta))

def multi(request, oper1, oper2):
    multi = int(oper1) * int(oper2)

    return HttpResponse(oper1 + " * " + oper2  + " = " + str(multi))

def div(request, oper1, oper2):
    try:
        div = int(oper1) / int(oper2)
    except ZeroDivisionError:
        return HttpResponse("Estas intentando dividir entre 0")

    return HttpResponse(oper1 + " / " + oper2  + " = " + str(div))

def error(request):
    return HttpResponse('404 Not Found')
