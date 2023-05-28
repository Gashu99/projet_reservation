from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from .models import chambre,personne
from .forms import formreservation_chambres
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
    context={"chambre":chambre.objects.all()[:9]}
    return render(request,"dall_diamm/listechambre.html",context)


def show(request,chambre_id):
    context={'chambre':get_object_or_404(chambre, pk = chambre_id)}
    return render(request,"dall_diamm/show.html",context)


def formreservation_chambre(request):
    
    if request.method=='POST':
        form=formreservation_chambres(request.POST)
        if form.is_valid():
            nom=form.cleaned_data['username']
            pre=form.cleaned_data['prenom']
            pa=form.cleaned_data['password']
            cpa=form.cleaned_data['confirmpassword']
            tel=form.cleaned_data['Tel']
            mail=form.cleaned_data['mail']
            pers=personne(nom=nom,prenom=pre,email=mail,Tel=tel)
            pers.save()

            return redirect("index")
    else:
        form=formreservation_chambres()
    context={'form':form}
    return render(request,"dall_diamm/formreservation_chambre.html",context)

   