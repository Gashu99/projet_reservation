from django.contrib import admin
from .models import voiture,chambre,personne,reserver_chambre




class Adminchambre(admin.ModelAdmin):
    list_display=('id_c','nom_chmb','prix_chmb')

class Adminpersonne(admin.ModelAdmin):
    list_display=('nom','prenom','email','Tel')
    
class Adminreserver_chambre(admin.ModelAdmin):
    list_display = ('date_reservation', 'get_nom_chambre', 'get_nom_personne')

    def get_nom_chambre(self, obj):
        return obj.id_c.nom_chmb

    def get_nom_personne(self, obj):
        return obj.id_p.nom

    get_nom_chambre.short_description = 'Nom de la chambre'
    get_nom_personne.short_description = 'Nom de la personne'

# # Register your models here.
admin.site.register(chambre,Adminchambre)
admin.site.register(personne,Adminpersonne)
admin.site.register(reserver_chambre,Adminreserver_chambre)

