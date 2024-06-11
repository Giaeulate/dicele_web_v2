from django.contrib import admin
from .models import *


@admin.register(FormField)
class FormFieldAdmin(admin.ModelAdmin):
    list_display = [x.name for x in FormField._meta.fields]
    # search_fields = ['',]


@admin.register(FormFieldOption)
class FormFieldOptionAdmin(admin.ModelAdmin):
    list_display = [x.name for x in FormFieldOption._meta.fields]
    # search_fields = ['',]