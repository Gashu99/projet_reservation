# Generated by Django 4.2.1 on 2023-05-21 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dall_diamm", "0002_chambre"),
    ]

    operations = [
        migrations.CreateModel(
            name="personne",
            fields=[
                (
                    "id_p",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=100)),
                ("prenom", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("Tel", models.CharField(max_length=50)),
            ],
        ),
    ]
