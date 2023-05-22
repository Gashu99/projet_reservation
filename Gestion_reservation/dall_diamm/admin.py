from django.contrib import admin
from .models import voiture,chambre,personne


class Adminvoiture(admin.ModelAdmin):
    list_display=('num_voit','nom_voit','prix')
    list_filter=['nom_voit']


class Adminchambre(admin.ModelAdmin):
    list_display=('id','nom_chmb','prix_chmb')

class Adminpersonne(admin.ModelAdmin):
    list_display=('nom','prenom','email','Tel')
    


# # Register your models here.
admin.site.register(voiture,Adminvoiture)
admin.site.register(chambre,Adminchambre)
admin.site.register(personne,Adminpersonne)

