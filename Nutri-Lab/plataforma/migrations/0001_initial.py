# Generated by Django 4.0.1 on 2022-07-06 18:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Pacientes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=50)),
                (
                    "sexo",
                    models.CharField(
                        choices=[("F", "Feminino"), ("M", "Maculino")], max_length=1
                    ),
                ),
                ("idade", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("telefone", models.CharField(max_length=19)),
                (
                    "nutri",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
