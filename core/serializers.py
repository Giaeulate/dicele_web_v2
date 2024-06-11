from rest_framework import serializers
from .models import FormField, FormFieldOption


class FormFieldOptionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()

    class Meta:
        model = FormFieldOption
        fields = ['id', 'label', 'field_type', 'required', 'options']

    def get_options(self, obj):
        # Recuperar las subopciones del campo actual
        suboptions = FormFieldOption.objects.filter(parent=obj)
        # Serializar las subopciones si existen
        if suboptions:
            return FormFieldOptionSerializer(suboptions, many=True).data
        return None


class FormFieldSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()

    class Meta:
        model = FormField
        fields = ['id', 'label', 'field_type', 'required', 'options']

    def get_options(self, obj):
        # Recuperar las opciones directamente asociadas al campo de formulario
        options = FormFieldOption.objects.filter(field=obj, parent=None)
        # Serializar las opciones si existen
        if options:
            return FormFieldOptionSerializer(options, many=True).data
        return None
