from django.contrib import admin
from .models import voiture,chambre


class Adminvoiture(admin.ModelAdmin):
    list_display=('nom_voit','prix')
    list_filter=['nom_voit']


class Adminchambre(admin.ModelAdmin):
    list_display=('num_chmb','nom_chmb','prix_chmb','date_location')
    

# Register your models here.
admin.site.register(voiture,Adminvoiture)
admin.site.register(chambre,Adminchambre)
