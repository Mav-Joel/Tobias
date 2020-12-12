from django.shortcuts import render
from django.http import HttpResponse
from .models import Reseau
from django.template import loader
import os
import subprocess
# Create your views here.

def index(request):
    template = loader.get_template('index/index.html')
    return HttpResponse(template.render(request=request))

def getSlotFromDb(request,slot):
    Slots = ["Bonjour","Au revoir"]
    return HttpResponse(Slots[int(slot)])

def search(request):
    template = loader.get_template('index/index.html')

    try : 
        #What you are getting from the url 
        query = request.GET['query']
        if not query : 

            return HttpResponse("Aucun paramètre reçu")

        else : 
            allowed = Reseau.objects.get(nature="{}".format(query))
            message = allowed.information
            
            return HttpResponse(template.render(request=request)+query+" is "+message)
    except : 
        return HttpResponse("Pour effectuer une recherche il vous faut saisir : .../search/?query=VOTRE_RECHERCHE")
    