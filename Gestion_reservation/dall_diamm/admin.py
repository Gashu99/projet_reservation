from django.contrib import admin
from .models import voiture,chambre,personne,restaurant


class Adminvoiture(admin.ModelAdmin):
    list_display=('num_voit','nom_voit','prix')
    list_filter=['nom_voit']


class Adminchambre(admin.ModelAdmin):
    list_display=('id_c','nom_chmb','prix_chmb')

class Adminpersonne(admin.ModelAdmin):
    list_display=('nom','prenom','email','Tel')
    
class Adminrestaurant(admin.ModelAdmin):
    list_display=('num_plat','nom_plat', 'prix_plat')

class Adminreserver_chambre(admin.ModelAdmin):
    list_display=('date_reservation','id_p', 'id_c')


# # Register your models here.
admin.site.register(voiture,Adminvoiture)
admin.site.register(chambre,Adminchambre)
admin.site.register(personne,Adminpersonne)
admin.site.register(restaurant,Adminrestaurant)
#admin.site.register(reserver_chambre,Adminreserver_chambre)

