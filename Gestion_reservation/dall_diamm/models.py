from typing import Type
from django.db import models
from django.db import connection
from datetime import *
from django.core.exceptions import ValidationError
from django.db.models.options import Options
import json

# Pour vider toutes les donnees d'une table
# with connection.cursor() as cursor:
#     cursor.execute("DELETE FROM dall_diamm_restaurant")


# Create your models here.
class personne(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    email=models.EmailField()
    Tel=models.CharField(max_length=50)
    
class voiture(models.Model):
    num_voit=models.IntegerField(primary_key=True)
    nom_voit = models.CharField(max_length=200)
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self) -> str:
        return self.nom_voit
      
data={"car_1": {"num_voit": 1, "nom_voit": "1/18 HH Model Bugatti Veyron Gold Edition (Limit 30 Pieces)", "prix": "72995", "date_livraison": "12-06-2023", "disponible": True}, "car_2": {"num_voit": 2, "nom_voit": "Ferrari  Sport Wheels Diamond-Cut", "prix": 103000.0, "date_livraison": "31-05-2023", "disponible": True}, "car_3": {"num_voit": 3, "nom_voit": "Ferrari  Introduced Sport Wheels Aluminum", "prix": 970000.0, "date_livraison": "31-05-2023", "disponible": True}, "car_4": {"num_voit": 4, "nom_voit": "1/18 MR Ferrari  VGT Vision GT w/ Certificate Limited 28", "prix": "159795", "date_livraison": "12-06-2023", "disponible": True}, "car_5": {"num_voit": 5, "nom_voit": "Ferrari  Classique Wheels Aluminum", "prix": 647000.0, "date_livraison": "02-06-2023", "disponible": True}, "car_6": {"num_voit": 6, "nom_voit": "Bugatti CHIRON front end complete, OEM Part", "prix": 330000.0, "date_livraison": "07-06-2023", "disponible": True}, "car_7": {"num_voit": 7, "nom_voit": "Mr 1:18 Bugatti Dragon Sport Noire Black(in Stock )", "prix": 119999, "date_livraison": "5-06-2023", "disponible": True}, "car_8": {"num_voit": 8, "nom_voit": "Buggati chiron", "prix": 50627, "date_livraison": "15-06-2023", "disponible": True}, "car_9": {"num_voit": 9, "nom_voit": "1/18 MR Ferrari  VGT Vision GT (Blue) w/ Certificate Limited #372/499", "prix": "179795", "date_livraison": "12-06-2023", "disponible": True}, "car_10": {"num_voit": 10, "nom_voit": "Ferrari  Caractere Wheels Diamond-Cut", "prix": 870000.0, "date_livraison": "02-06-2023", "disponible": True}, "car_11": {"num_voit": 11, "nom_voit": "Bugatti Centodieci 2022 3d model", "prix": 59400, "date_livraison": "15-06-2023", "disponible": True}, "car_12": {"num_voit": 12, "nom_voit": "Bburago 1:18 Bugatti Bolide, Blue", "prix": 54925, "date_livraison": "15-06-2023", "disponible": True}, "car_13": {"num_voit": 13, "nom_voit": "GTA V Ferrari  Sport Gold Edition | FiveM Ready | Realistic Handling | High ...", "prix": 50613, "date_livraison": "15-06-2023", "disponible": True}, "car_14": {"num_voit": 14, "nom_voit": "Lego 42083 Technic Ferrari ", "prix": 82400, "date_livraison": "5-06-2023", "disponible": True}, "car_15": {"num_voit": 15, "nom_voit": "Bugatti 10 - 11\"x17\"-12\"x18\" Buy Any 2 Get Any 1 Free", "prix": 51175, "date_livraison": "24-05-2023", "disponible": True}, "car_16": {"num_voit": 16, "nom_voit": "1/18 HH Model Bugatti chiron Gucci Resin Car Model", "prix": "85795", "date_livraison": "12-06-2023", "disponible": True}, "car_17": {"num_voit": 17, "nom_voit": "Rolls-Royce  with HQ interior 2020 3d model", "prix": 79000, "date_livraison": "15-06-2023", "disponible": True}, "car_18": {"num_voit": 18, "nom_voit": "Bugatti Electric Scooter - Agile Blue", "prix": "120000", "date_livraison": "5-06-2023", "disponible": True}, "car_19": {"num_voit": 19, "nom_voit": "Autoart 1/12 Bugatti Veyron 16.4 Production Version Blue/black Metalic", "prix": 119999, "date_livraison": "5-06-2023", "disponible": True}, "car_20": {"num_voit": 20, "nom_voit": "Bugatti Veyron Center Console Painted", "prix": 218000.0, "date_livraison": "02-06-2023", "disponible": True}, "car_21": {"num_voit": 21, "nom_voit": "1/18 HH Model Ferrari  (White & Black) Resin Car Model", "prix": "84995", "date_livraison": "12-06-2023", "disponible": True}, "car_22": {"num_voit": 22, "nom_voit": "Bugatti Non-Refundable Deposit", "prix": 70000, "date_livraison": "01-06-2023", "disponible": True}, "car_23": {"num_voit": 23, "nom_voit": "Parmigiani Fleurier Bugatti Super Sport", "prix": 127273.4, "date_livraison": "1-06-2023", "disponible": True}, "car_24": {"num_voit": 24, "nom_voit": "DAKOTT Rolls-Royce  Ride on Car for Kids", "prix": 92302, "date_livraison": "26-05-2023", "disponible": True}, "car_25": {"num_voit": 25, "nom_voit": "Lamborghini  Grand Sport Vitesse 1:8 Scale Model", "prix": 119950.0, "date_livraison": "22-05-2023", "disponible": True}, "car_26": {"num_voit": 26, "nom_voit": "Xgeek Ferrari  Ferrari Veyron Racing Building Kit And", "prix": 80000, "date_livraison": "26-05-2023", "disponible": True}, "car_27": {"num_voit": 27, "nom_voit": "Ferrari  Kids 12V Battery Operated Ride on Car with Remote Control - Blue/", "prix": 76600, "date_livraison": "15-06-2023", "disponible": True}, "car_28": {"num_voit": 28, "nom_voit": "Lamborghini  Pur Sport Grand Prix Top Speed", "prix": 68495, "date_livraison": "26-05-2023", "disponible": True}, "car_29": {"num_voit": 29, "nom_voit": "Bugatti EB110 SS Super Sport Nero Vernice Black with Red Interior and Silver Whe ...", "prix": 72999, "date_livraison": "5-06-2023", "disponible": True}, "car_30": {"num_voit": 30, "nom_voit": "DAKOTT Ferrari  12V Ride on Car", "prix": 88999, "date_livraison": "15-06-2023", "disponible": True}, "car_31": {"num_voit": 31, "nom_voit": "Ferrari  Pur Sport 2022 3d model", "prix": 59300, "date_livraison": "15-06-2023", "disponible": True}, "car_32": {"num_voit": 32, "nom_voit": "Lamborghini Factory Racers Foresti  1926 French Grand Prix Miramas", "prix": 50975, "date_livraison": "5-06-2023", "disponible": True}, "car_33": {"num_voit": 33, "nom_voit": "Bburago Rolls-Royce  Special Edition By Bburago - Toys & Collectibles | Color: Grey", "prix": 54500, "date_livraison": "5-06-2023", "disponible": True}, "car_34": {"num_voit": 34, "nom_voit": "1/12 Bugatti Bolide (Carbon Bugatti Green) Resin Car Model Limited 5 Pieces", "prix": "199995", "date_livraison": "12-06-2023", "disponible": True}, "car_35": {"num_voit": 35, "nom_voit": "Ferrari  Pur Sport Full Carbon | AUTO Barn Models", "prix": 114995, "date_livraison": "19-05-2023", "disponible": True}, "car_36": {"num_voit": 36, "nom_voit": "Photo Print: Jean Bugatti and Roland Bugatti Sons of Ettore Bugatti in", "prix": 54000, "date_livraison": "5-06-2023", "disponible": True}, "car_37": {"num_voit": 37, "nom_voit": "Jean Bugatti and Roland Bugatti Sons of Ettore Bugatti in Cars Made by their ...", "prix": 51499, "date_livraison": "15-06-2023", "disponible": True}, "car_38": {"num_voit": 38, "nom_voit": "12V Rolls-Royce  1 Seater Ride on Car (White)", "prix": 104739, "date_livraison": "31-05-2023", "disponible": True}, "car_39": {"num_voit": 39, "nom_voit": "Rolls-Royce ", "prix": 59491, "date_livraison": "07-06-2023", "disponible": True}, "car_40": {"num_voit": 40, "nom_voit": "Ferrari  1:10 RTR Electric 2.4ghz RC Car", "prix": 59999, "date_livraison": "5-06-2023", "disponible": True}, "car_41": {"num_voit": 41, "nom_voit": "Bugatti Bolide 2022 3d model", "prix": 59300, "date_livraison": "15-06-2023", "disponible": True}, "car_42": {"num_voit": 42, "nom_voit": "FTL Bugatti Metal Car Model Bright Black", "prix": 53895, "date_livraison": "06-06-2023", "disponible": True}, "car_43": {"num_voit": 43, "nom_voit": "The Bugatti Veyron Bugatti Sticker | Redbubble", "prix": 50269, "date_livraison": "5-06-2023", "disponible": True}, "car_44": {"num_voit": 44, "nom_voit": "1/12 Bugatti Bolide (Carbon Bugatti Blue) Resin Car Model Limited 15 Pieces", "prix": "234995", "date_livraison": "12-06-2023", "disponible": True}, "car_45": {"num_voit": 45, "nom_voit": "BUGATTI SILVER ELECTRAVELER", "prix": "120000", "date_livraison": "08-06-2023", "disponible": True}, "car_46": {"num_voit": 46, "nom_voit": "AUTOART BUGATTI CHIRON ITALIAN RED/NOCTURNE BLACK 1:12", "prix": 99900, "date_livraison": "5-06-2023", "disponible": True}, "car_47": {"num_voit": 47, "nom_voit": "1:18 Rolls-Royce  Diecast | Maisto NEW", "prix": 56994, "date_livraison": "5-06-2023", "disponible": True}, "car_48": {"num_voit": 48, "nom_voit": "G8Central Rastar 1:14 RC Lamborghini  Grand Sport Vitesse Car (Black/Blue)", "prix": 56925, "date_livraison": "15-06-2023", "disponible": True}, "car_49": {"num_voit": 49, "nom_voit": "Bugatti 150 Success Secrets - 150 Most Asked Questions On Bugatti - What You Need ...", "prix": 51899, "date_livraison": "15-06-2023", "disponible": True}, "car_50": {"num_voit": 50, "nom_voit": "Lamborghini: Type 35 Grand Prix Car and Its Variants [Book]", "prix": 50619, "date_livraison": "08-06-2023", "disponible": True}, "car_51": {"num_voit": 51, "nom_voit": "Diecast Ferrari  Sport Model Racing Car Ferrari-DIVO", "prix": 54300, "date_livraison": "23-06-2023", "disponible": True}, "car_52": {"num_voit": 52, "nom_voit": "1:14 RC Lamborghini  Grand Sport Vitesse Car (Black/Blue) - Kids", "prix": 53970, "date_livraison": "31-05-2023", "disponible": True}, "car_53": {"num_voit": 53, "nom_voit": "2021 1:24 Rolls-Royce Veyron  Alloy Car Model Diecasts & Toy Vehicles", "prix": 52850, "date_livraison": "15-06-2023", "disponible": True}, "car_54": {"num_voit": 54, "nom_voit": "1/12 Bugatti Bolide (Carbon Bugatti Red) Resin Car Model Limited 5 Pieces", "prix": "199995", "date_livraison": "12-06-2023", "disponible": True}, "car_55": {"num_voit": 55, "nom_voit": "Bugatti Eb Veyron 16.4 Pur Sang Black / Aluminum Casting 1/18 by Autoart", "prix": 87999, "date_livraison": "23-05-2023", "disponible": True}, "car_56": {"num_voit": 56, "nom_voit": "JKM JackieKim Ferrari  Diecast Model Car 1:64", "prix": 51278, "date_livraison": "15-06-2023", "disponible": True}, "car_57": {"num_voit": 57, "nom_voit": "Orbisify Alloy Sport Car Rolls-Royce  Open Doors Sound Lights", "prix": 52499, "date_livraison": "31-05-2023", "disponible": True}, "car_58": {"num_voit": 58, "nom_voit": "Bugatti Sport 24 inchx36 inch Poster Cars Genf Geneva 2018 debut, red", "prix": 52949, "date_livraison": "15-06-2023", "disponible": True}, "car_59": {"num_voit": 59, "nom_voit": "Bburago 1 1/8 Scale Burago Rolls-Royce . Never Been Out Of Box - New Toys ...", "prix": 53900, "date_livraison": "5-06-2023", "disponible": True}, "car_60": {"num_voit": 60, "nom_voit": "Rolls-Royce  2020 3d model", "prix": 59200, "date_livraison": "15-06-2023", "disponible": True}}
#Exécuter une requête SQL pour insérer les donnée   
with connection.cursor() as cursor:
    for key, values in data.items():
        num_voit=values["num_voit"]
        nom_voit = values["nom_voit"]
        prix = values["prix"]
        query_check="SELECT * FROM dall_diamm_voiture WHERE nom_voit= %s"
        cursor.execute(query_check,[nom_voit])
        resultat = cursor.fetchall()

        if not resultat:
            query_insert="""  
                INSERT INTO dall_diamm_voiture(num_voit, nom_voit, prix) 
                VALUES (%s, %s, %s)
                """
            cursor.execute(query_insert,[num_voit,nom_voit, prix])
            

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         "INSERT IGNORE INTO dall_diamm_voiture(num_voit,nom_voit, prix) "
    #         "VALUES (%s,%s, %s)",
    #         [num_voit,nom_voit, prix]
    #     )
    # voit = voiture(num_voit=num_voit,nom_voit=nom_voit, prix=prix)
    # voit.save()



#Pour CHAMBRE
class chambre(models.Model):
    id_c=models.BigAutoField(auto_created=True,primary_key=True,verbose_name="ID")
    nom_chmb=models.CharField(max_length=300)
    prix_chmb=models.DecimalField(max_digits=8,decimal_places=2)
    disponible=models.BooleanField()
    def __str__(self) -> str:
        return self.nom_chmb
with open('/home/fatou/Bureau/projet_reservation/Gestion_reservation/dall_diamm/data_room.json') as fichier:
    contenu = json.load(fichier)
# Exécuter une requête SQL pour insérer les données
with connection.cursor() as cursor:
    for key, values in contenu.items():
        nom_chmb = values["nom_chmb"]
        prix_chmb = values["prix"] 
        disponible=values["disponible"]
        query_check1="SELECT * FROM dall_diamm_chambre WHERE nom_chmb= %s"
        cursor.execute(query_check1,[nom_chmb])
        resultat1 = cursor.fetchall()

        if not resultat1:
            query_insert1="""  
                INSERT INTO dall_diamm_chambre(nom_chmb, prix_chmb,disponible) 
                VALUES (%s, %s, %s)
                """
            cursor.execute(query_insert1,[nom_chmb, prix_chmb,disponible  ])
            
            
        #     cursor.execute(
        #     "INSERT INTO dall_diamm_chambre(nom_chmb, prix_chmb,disponible) "
        #     "VALUES (%s, %s, %s)",
        #     [nom_chambre, prix_chambre,disponibilite]
        # )
    

#Classe resto 
class restaurant(models.Model):
    num_plat=models.IntegerField()
    nom_plat=models.CharField(max_length=200)
    prix_plat=models.DecimalField(max_digits=8,decimal_places=2)
    
    disponibilite_plat=models.BooleanField(default=True)
# with open('/home/fatou/Bureau/projet_reservation/Gestion_reservation/dall_diamm/data_resto.json') as fichier:
#     contenu_resto = json.load(fichier)

#     with connection.cursor() as cursor:
#         for key, values in contenu_resto.items():
#             num_plat = values["num_plat"]
#             nom_plat = values["nom_plat"]
#             prix_plat = values["prix"] 
#             img = values["image"] 
#             disponibilite_plat=values["disponible"]
#             query_check1="SELECT * FROM dall_diamm_restaurant WHERE nom_plat= %s"
#             cursor.execute(query_check1,[nom_plat])
#             resultat1 = cursor.fetchall()

#             if not resultat1:
#                 query_insert1="""  
#                     INSERT INTO dall_diamm_restaurant(num_plat,nom_plat, prix_plat,img,disponibilite_plat) 
#                     VALUES (%s, %s, %s, %s, %s)
#                     """
#                 cursor.execute(query_insert1,[num_plat,nom_plat, prix_plat,img,disponibilite_plat ])
            

            # cursor.execute(
            #     "INSERT INTO dall_diamm_restaurant(num_plat,nom_plat, prix_plat,img,disponibilite_plat) "
            #     "VALUES (%s, %s, %s, %s, %s)",
            #     [num_plat,nom_plat, prix_plat,img,disponibilite_plat]
            # )

class reserver_chambre(models.Model):
    date_reservation = models.DateField()
    id_p= models.ForeignKey(personne, on_delete=models.CASCADE, related_name='reservations')
    id_c = models.ForeignKey(chambre, on_delete=models.CASCADE, related_name='reservations')

    class Meta:
        db_table = "dall_diamm_reserver_chambre"  # Nom de la table
