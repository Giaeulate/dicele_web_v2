''' views '''
# pylint: disable=too-few-public-methods, missing-class-docstring, no-member, wildcard-import, unused-wildcard-import
# from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import *
from core.serializers import *


class LemaList(ListCreateAPIView):
    queryset = Lema.objects.all()
    serializer_class = LemaSerializer


class LemaDetail(RetrieveUpdateDestroyAPIView):
    queryset = Lema.objects.all()
    serializer_class = LemaSerializer
    permission_classes = [AllowAny]


class PronunciationList(ListCreateAPIView):
    queryset = Pronunciation.objects.all()
    serializer_class = PronunciationSerializer


class PronunciationDetail(RetrieveUpdateDestroyAPIView):
    queryset = Pronunciation.objects.all()
    serializer_class = PronunciationSerializer
    permission_classes = [AllowAny]


class TypePronunciationList(ListCreateAPIView):
    queryset = TypePronunciation.objects.all()
    serializer_class = TypePronunciationSerializer


class TypePronunciationDetail(RetrieveUpdateDestroyAPIView):
    queryset = TypePronunciation.objects.all()
    serializer_class = TypePronunciationSerializer
    permission_classes = [AllowAny]


class OrthographyList(ListCreateAPIView):
    queryset = Orthography.objects.all()
    serializer_class = OrthographySerializer


class OrthographyDetail(RetrieveUpdateDestroyAPIView):
    queryset = Orthography.objects.all()
    serializer_class = OrthographySerializer
    permission_classes = [AllowAny]


class MeaningList(ListCreateAPIView):
    queryset = Meaning.objects.all()
    serializer_class = MeaningSerializer


class MeaningDetail(RetrieveUpdateDestroyAPIView):
    queryset = Meaning.objects.all()
    serializer_class = MeaningSerializer
    permission_classes = [AllowAny]


class WordTypeList(ListCreateAPIView):
    queryset = WordType.objects.all()
    serializer_class = WordTypeSerializer


class WordTypeDetail(RetrieveUpdateDestroyAPIView):
    queryset = WordType.objects.all()
    serializer_class = WordTypeSerializer
    permission_classes = [AllowAny]


class SubgroupwordList(ListCreateAPIView):
    queryset = Subgroupword.objects.filter(parent=None)
    serializer_class = SubgroupwordSerializer


class SubgroupwordDetail(RetrieveUpdateDestroyAPIView):
    queryset = Subgroupword.objects.all()
    serializer_class = SubgroupwordSerializer
    permission_classes = [AllowAny]


class MeaningDetailView(APIView):
    def get(self, request, pk):
        try:
            meaning = Meaning.objects.get(pk=pk)
        except Meaning.DoesNotExist:
            return Response({'error': 'Meaning not found'}, status=404)
        try:
            msgw = MeaningSubGroupWord.objects.filter(meaning=meaning).first()
            subgroupword = msgw.sub_group_word
        except MeaningSubGroupWord.DoesNotExist:
            return Response({'error': 'Subgroupword not found for this Meaning'}, status=404)

        subgroupword_data = SubgroupwordSerializer(subgroupword).data
        parents_data = []
        parent = subgroupword.parent
        while parent is not None:
            parent_data = SubgroupwordSerializer(parent).data
            parents_data.append(parent_data)
            parent = parent.parent

        return Response({
            'meaning': MeaningSerializer(meaning).data,
            'sub_group_words': subgroupword_data,
            'parents': parents_data
        })
