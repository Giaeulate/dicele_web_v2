# Generated by Django 5.0.6 on 2024-06-11 18:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_alter_formfield_field_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="formfieldoption", old_name="value", new_name="label",
        ),
        migrations.AlterField(
            model_name="formfield",
            name="field_type",
            field=models.CharField(
                choices=[
                    ("text", "Text"),
                    ("number", "Number"),
                    ("date", "Date"),
                    ("select", "Select"),
                    ("checkbox", "Checkbox"),
                ],
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="formfieldoption",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="options",
                to="core.formfieldoption",
            ),
        ),
    ]