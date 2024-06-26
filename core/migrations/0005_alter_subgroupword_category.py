# Generated by Django 5.0.6 on 2024-06-15 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_meaningsubgroupword_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subgroupword",
            name="category",
            field=models.CharField(
                choices=[
                    ("clasificacion", "clasificacion"),
                    ("morfologia", "morfologia"),
                    ("sintaxis", "sintaxis"),
                    ("pragmatica", "pragmatica"),
                    ("cultura", "cultura"),
                    ("ejemplos", "ejemplos"),
                ],
                default=("clasificacion", "clasificacion"),
                max_length=50,
            ),
        ),
    ]
