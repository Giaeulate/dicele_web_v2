''' serializers '''

from rest_framework.serializers import *
from .models import *


class TypePronunciationSerializer(ModelSerializer):
    class Meta:
        model = TypePronunciation
        fields = '__all__'


class LemaSerializer(ModelSerializer):
    class Meta:
        model = Lema
        fields = '__all__'


class PronunciationSerializer(ModelSerializer):
    class Meta:
        model = Pronunciation
        fields = '__all__'


class OrthographySerializer(ModelSerializer):
    class Meta:
        model = Orthography
        fields = '__all__'


class MeaningSerializer(ModelSerializer):
    class Meta:
        model = Meaning
        fields = '__all__'


class WordTypeSerializer(ModelSerializer):
    class Meta:
        model = WordType
        fields = '__all__'


# class SubgroupwordSerializer(ModelSerializer):
#     class Meta:
#         model = Subgroupword
#         fields = '__all__'

class SubgroupwordSerializer(ModelSerializer):
    options = SerializerMethodField()

    class Meta:
        model = Subgroupword
        # fields = ['id', 'name', 'field_type', 'active', 'options']
        fields = [x.name for x in Subgroupword._meta.fields] + ['options']

    def get_options(self, obj):
        # Recuperar las subopciones del campo actual
        suboptions = Subgroupword.objects.filter(parent=obj)
        # Serializar las subopciones si existen
        if suboptions:
            return SubgroupwordSerializer(suboptions, many=True).data
        return None


# class FormFieldSerializer(ModelSerializer):
#     options = SerializerMethodField()

#     class Meta:
#         model = FormField
#         fields = ['id', 'name', 'field_type', 'active', 'options']

#     def get_options(self, obj):
#         # Recuperar las opciones directamente asociadas al campo de formulario
#         options = Subgroupword.objects.filter(field=obj, parent=None)
#         # Serializar las opciones si existen
#         if options:
#             return SubgroupwordSerializer(options, many=True).data
#         return None
