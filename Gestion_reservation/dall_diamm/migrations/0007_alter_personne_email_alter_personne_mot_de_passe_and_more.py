# Generated by Django 4.2.1 on 2023-06-14 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dall_diamm", "0006_alter_personne_mot_de_passe"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personne",
            name="email",
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name="personne",
            name="mot_de_passe",
            field=models.CharField(default="", max_length=20),
        ),
        migrations.AlterField(
            model_name="personne",
            name="nom",
            field=models.CharField(max_length=100),
        ),
    ]
