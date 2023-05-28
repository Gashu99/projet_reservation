from django.urls import path
from . import views



urlpatterns=[
    path('',views.index,name='index'),
    path('form_inscription/',views.form_inscription,name='form_inscription'),
    path('listechambre/',views.listechambre,name='listechambre'),
    path('voiture/',views.voiture,name='voiture'),
    path('<int:chambre_id>/',views.show,name='show'),
    path('formreservation_chambre/',views.formreservation_chambre,name='formreservation_chambre'),
]