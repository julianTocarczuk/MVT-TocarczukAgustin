from django.shortcuts import render
from appfamilia.models import Familiar
from django.template import loader
from django.http import HttpResponse

def mostrar_familiar(request):

    familiar = Familiar.objects.all()

    datos = {"nombre" : familiar}
    
    archivo = loader.get_template("family.html")

    documento = archivo.render(datos)
    
    return HttpResponse(documento)