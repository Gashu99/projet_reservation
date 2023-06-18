# Generated by Django 4.2.1 on 2023-06-14 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "dall_diamm",
            "0008_alter_personne_email_alter_personne_mot_de_passe_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="personne",
            name="email",
            field=models.EmailField(default="", max_length=254),
        ),
        migrations.AlterField(
            model_name="personne",
            name="mot_de_passe",
            field=models.CharField(default="", max_length=20),
        ),
        migrations.AlterField(
            model_name="personne",
            name="nom",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="personne",
            name="prenom",
            field=models.CharField(default="", max_length=100),
        ),
    ]
