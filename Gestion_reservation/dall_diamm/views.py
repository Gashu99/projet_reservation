from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import chambre
# Create your views here.
def index(request):
    context={}
    template=loader.get_template("dall_diamm/index.html")
    return HttpResponse(template.render(context,request))

def voiture(request):
    context={}
    template=loader.get_template("dall_diamm/voiture.html")
    return HttpResponse(template.render(context,request))



def form_inscription(request):
    context={}
    template=loader.get_template("dall_diamm/form_inscription.html")
    return HttpResponse(template.render(context,request))

def listechambre(request):
    context={"chambre":chambre.objects.all()}
    return render(request,"dall_diamm/listechambre.html",context)