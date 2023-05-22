from django.urls import path
from . import views



urlpatterns=[
    path('',views.index,name='index'),
    path('form_inscription/',views.form_inscription,name='form_inscription'),
    path('listechambre/',views.listechambre,name='listechambre'),
    path('voiture/',views.voiture,name='voiture'),
]