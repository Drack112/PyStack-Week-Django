# Generated by Django 3.2.8 on 2021-10-08 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("usuarios", "0001_initial"), ("cursos", "0002_comentarios")]

    operations = [
        migrations.CreateModel(
            name="NotasAulas",
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
                (
                    "nota",
                    models.CharField(
                        choices=[
                            ("p", "Péssimo"),
                            ("r", "Ruim"),
                            ("re", "Regular"),
                            ("b", "bom"),
                            ("o", "Ótimo"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "aula",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="cursos.aulas",
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="usuarios.usuario",
                    ),
                ),
            ],
        )
    ]
