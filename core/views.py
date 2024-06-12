''' views '''
# pylint: disable=too-few-public-methods, missing-class-docstring, no-member, wildcard-import, unused-wildcard-import
# from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework import serializers
from core.models import *
from core.serializers import *
from rest_framework.response import Response


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

    # def get(self, request):
    #     fields = Subgroupword.objects.filter(parent=None)
    #     serializer = SubgroupwordSerializer(fields, many=True)
    #     return Response(serializer.data)


class SubgroupwordDetail(RetrieveUpdateDestroyAPIView):
    queryset = Subgroupword.objects.all()
    serializer_class = SubgroupwordSerializer
    permission_classes = [AllowAny]

