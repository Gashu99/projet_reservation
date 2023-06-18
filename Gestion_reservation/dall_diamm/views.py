from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from .models import chambre,personne,reserver_chambre,voiture,reservationVoitures,restaurant
from .forms import formreservation_chambres
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login
import re


# Create your views here.
def index(request):
    context={}
    template=loader.get_template("dall_diamm/index.html")
    return HttpResponse(template.render(context,request))

def restaurant_view(request):
    
    context={"restaurant":restaurant.objects.all()}
    return render(request,"dall_diamm/restaurant.html",context)

def paiement(request):
    context={}
    template=loader.get_template("dall_diamm/paiement.html")
    return HttpResponse(template.render(context,request))


def voitures (request):
    context={"voiture":voiture.objects.all()}
    return render(request,"dall_diamm/voitures.html",context)

def details_voiture(request, idVoiture):
    voiture_obj = get_object_or_404(voiture,idV= idVoiture)
    return render(request,"dall_diamm/reservationVoiture.html" ,{"voiture_obj":voiture_obj})


def reservationVoit(request):
    # Récupérer les valeurs des champs du formulaire
    prenom = request.POST.get('prenom', '')
    nom = request.POST.get('nom', '')
    email = request.POST.get('email', '')
    telephone = request.POST.get('telephone', '')
    vehicule_id = request.POST.get('vehicule', '')
    service = request.POST.get('service', '')
    date_loc = request.POST.get('dateLoc', '')
    vehicule = get_object_or_404(voiture, idV=vehicule_id)  # Initialisation de la variable vehicule
    permis = request.FILES['permis']

    if request.method == 'POST':
        # Vérifier les contraintes sur le nom, le prénom et le numéro de téléphone
        if not re.match("^[a-zA-Z]+$", prenom):
            messages.error(request, "Le prénom doit contenir uniquement des lettres.")
        if not re.match("^[a-zA-Z]+$", nom):
            messages.error(request, "Le nom doit contenir uniquement des lettres.")
        if not re.match("^(77|76|78|75|70)\d{7}$", telephone):
            messages.error(request, "Le numéro de téléphone doit commencer par 77, 76, 78, 75 ou 70 et doit contenir au total 9 chiffres.")

        # Si aucune erreur de validation n'est détectée, enregistrer les données dans la base de données
        if not messages.get_messages(request):
            vehicule = get_object_or_404(voiture, idV=vehicule_id)
            reservationV = reservationVoitures(prenom=prenom, nom=nom, email=email, telephone=telephone, vehicule=vehicule, service=service, date_loc=date_loc, permis=permis)
            reservationV.save()

            messages.success(request, "La réservation a été enregistrée avec succès.")
            return redirect('voitures')  # Remplacez 'nom_de_la_vue' par le nom de la vue vers laquelle vous souhaitez rediriger l'utilisateur après la réservation
        else:
            return render(request, 'dall_diamm/reservationVoiture.html', {'voiture_obj': vehicule, 'permis': permis,'prenom': prenom, 'nom': nom, 'email': email, 'telephone': telephone, 'vehicule': vehicule, 'service': service, 'date_loc': date_loc})

    return render(request, 'dall_diamm/reservationVoiture.html', {'voiture_obj': vehicule,'permis': permis, 'prenom': prenom, 'nom': nom, 'email': email, 'telephone': telephone, 'vehicule': vehicule, 'service': service, 'date_loc': date_loc})



def form_inscription(request):
    if request.method == 'POST':
        nm = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        mdp=request.POST.get('motdepasse')
        cmdp=request.POST.get('confirmationmdp')
        #Envoie de mail lors de l'inscription
        
        # Effectuez ici le traitement des données du formulaire
        if mdp==cmdp:
            subject = 'Inscription'
            message = 'Felicitation vous etes inscrit ..'
            from_email = 'gassamafatoubintou7@gmail.com'
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            pers=personne(nom=nm,prenom=prenom,email=email,Tel='776777622',mot_de_passe=mdp)
            pers.save()
            return redirect("index")
        else:
            
            messages.error(request, "Les mots de passe ne correspondent pas.")  
            form = {'nom': nm, 'prenom': prenom, 'email': email,'mdp':'','cmdp':''}
            return render(request, 'dall_diamm/form_inscription.html',{'form':form})
    else:
        storage = messages.get_messages(request)
        storage.used = True  # Marquer les messages 
        context={}
    return render(request, 'dall_diamm/form_inscription.html',context)

   


#Pour l'envoie de message 
def send_email(request):
    subject = 'Inscription'
    message = 'Felicitation vous etes inscrit .'
    from_email = 'your_email@example.com'
    recipient_list = ['recipient1@example.com', 'recipient2@example.com']
    
    send_mail(subject, message, from_email, recipient_list)


def connexion(request):
    if request.method == 'POST':
        em = request.POST.get('mail')
        mdp = request.POST.get('motdp')
        pers = authenticate(request, email=em, password=mdp)
        if pers.is_active:
            # Les informations d'identification sont valides, connecter l'utilisateur
            login(request, pers)
            return redirect('formreservation_chambre')
        else:
            # Les informations d'identification sont incorrectes
            messages.error(request, "Identifiants invalides. Veuillez réessayer.")

    context={}
    
    return render(request,"dall_diamm/connexion.html",context)

from django.contrib.auth import authenticate, login

# def connexion(request):
#     if request.method == 'POST':
#         em = request.POST.get('mail')
#         mdp = request.POST.get('motdp')
#         utilisateur = authenticate(request, email=em, password=mdp)
#         if utilisateur is not None:
#             if utilisateur.is_active:
#                 # Les informations d'identification sont valides, connecter l'utilisateur
#                 login(request, utilisateur)
#                 return redirect('formreservation_chambre')
#             else:
#                 # Les informations d'identification sont correctes, mais le compte est désactivé
#                 messages.error(request, "Votre compte est désactivé.")
#         else:
#             # Les informations d'identification sont incorrectes
#             messages.error(request, "Identifiants invalides. Veuillez réessayer.")

#     context = {}
#     return render(request, "dall_diamm/connexion.html", context)


def listechambre(request):
    valeur=request.POST.get('chercher')
    print(valeur)
    context={"chambre":chambre.objects.all()[:9]}
    return render(request,"dall_diamm/listechambre.html",context)


def rechercher(request):
    valeur=request.POST.get('chercher')
    context={"ch":chambre.objects.all().filter(prix_chmb=valeur)}
    return render(request,"dall_diamm/listechambre.html",context)


def show(request,chambre_id):
    context={'ch':get_object_or_404(chambre, pk = chambre_id)}
    return render(request,"dall_diamm/show.html",context)


def formreservation_chambre(request):
    # id = request.GET.get('id_c')
   
    # ch=get_object_or_404(chambre, pk = chambre_id)
    if request.method=='POST':
        form=formreservation_chambres(request.POST)
        if form.is_valid():
            id_ch=form.cleaned_data['numero_chambre']
            nom=form.cleaned_data['username']
            pre=form.cleaned_data['prenom']
            tel=form.cleaned_data['Tel']
            mail=form.cleaned_data['mail']
            date_res=form.cleaned_data['date_res']
            soneper=personne.objects.filter(nom=nom,prenom=pre,email=mail,Tel=tel).exists()
            if soneper:
                ch=get_object_or_404(chambre, pk = id_ch)
                # pers=personne(nom=nom,prenom=pre,email=mail,Tel=tel)
                pers, created = personne.objects.get_or_create(nom=nom, prenom=pre, email=mail, Tel=tel)
                resch=reserver_chambre.objects.create(date_reservation=date_res,id_c=ch,id_p=pers)
                
                resch.save()
                
                return redirect("paiement")
            else:
                return redirect('form_inscription')
    else:
        form=formreservation_chambres()
    context={'form':form}
    return render(request,"dall_diamm/formreservation_chambre.html",context)


def adminis(request):
    context={}
    template=loader.get_template("dall_diamm/admin.html")
    return HttpResponse(template.render(context,request))

def paiement(request):
    context={}
    template=loader.get_template("dall_diamm/paiement.html")
    return HttpResponse(template.render(context,request))

from django.db import connection
def searchUrl(request):
    if request.method =="POST":
        marque=request.POST.get("marque")
        couleur=request.POST.get("couleur")
        transmission=request.POST.get("transmission")
        with connection.cursor() as cursor:
            query ="""
                SELECT * FROM dall_diamm_voiture
                where marque = %s AND transmission  = %s AND couleur = %s
            """
            cursor.execute(query,[marque,transmission,couleur])
            voit_dispo =cursor.fetchall()
            print(voit_dispo)
            context= {'voit_dispo': voit_dispo}
        return render(request,"dall_diamm/search_voit.html",context)