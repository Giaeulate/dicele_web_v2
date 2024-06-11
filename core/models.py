# models.py

from django.db import models


class FormField(models.Model):
    FIELD_TYPE_CHOICES = [
        ('text', 'Text'),
        ('number', 'Number'),
        ('date', 'Date'),
        ('select', 'Select'),
        ('checkbox', 'Checkbox'),
    ]

    label = models.CharField(max_length=100)
    field_type = models.CharField(max_length=20, choices=FIELD_TYPE_CHOICES)
    required = models.BooleanField(default=True)

    def __str__(self):
        return self.label


class FormFieldOption(models.Model):
    field = models.ForeignKey(
        FormField, related_name='options', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)  # Cambio de value a label
    field_type = models.CharField(
        max_length=20, choices=FormField.FIELD_TYPE_CHOICES)  # Nuevo campo field_type
    required = models.BooleanField(default=True)  # Nuevo campo required
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='options', on_delete=models.CASCADE)

    def __str__(self):
        return self.label
