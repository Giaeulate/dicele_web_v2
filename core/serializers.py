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


class SubgroupwordSerializer(ModelSerializer):
    options = SerializerMethodField()

    class Meta:
        model = Subgroupword
        fields = [x.name for x in Subgroupword._meta.fields] + ['options']

    def get_options(self, obj):
        # Recuperar las subopciones del campo actual
        suboptions = Subgroupword.objects.filter(parent=obj)
        # Serializar las subopciones si existen
        if suboptions:
            return SubgroupwordSerializer(suboptions, many=True).data
        return None


class CustomSubgroupwordSerializer(ModelSerializer):
    parent = PrimaryKeyRelatedField(read_only=True)
    options = SerializerMethodField()

    class Meta:
        model = Subgroupword
        fields = '__all__'

    def get_options(self, obj):
        options = Subgroupword.objects.filter(parent=obj)
        if options.exists():
            return CustomSubgroupwordSerializer(options, many=True).data
        return None


class MeaningSubGroupWordSerializer(ModelSerializer):
    sub_group_word = CustomSubgroupwordSerializer()

    class Meta:
        model = MeaningSubGroupWord
        fields = ('meaning', 'sub_group_word')
