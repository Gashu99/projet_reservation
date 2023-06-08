from django.urls import path
from . import views



urlpatterns=[
    path('',views.index,name='index'),
    path('form_inscription/',views.form_inscription,name='form_inscription'),
    path('connexion/',views.connexion,name='connexion'),
    path('listechambre/',views.listechambre, name='listechambre'),
    path('voitures/', views.voitures,name='voitures'),
    path('<int:chambre_id>/',views.show,name='show'),
    path('formreservation_chambre/',views.formreservation_chambre,name='formreservation_chambre'),
    path('formreservation_chambre/<int:chambre_id>/',views.formreservation_chambre,name='formreservation_chambre'),
    path('reservationVoiture/', views.reservationVoit, name='reservationVoiture'),
    path('reservationVoiture/<int:idVoiture>',views.details_voiture,name='reservationVoiture'),
]



