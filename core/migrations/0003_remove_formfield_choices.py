# Generated by Django 4.1.7 on 2024-05-22 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_formfieldoption"),
    ]

    operations = [
        migrations.RemoveField(model_name="formfield", name="choices",),
    ]
