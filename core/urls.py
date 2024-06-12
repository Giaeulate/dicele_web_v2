from django.urls import path
from .views import *
from django.conf.urls.static import static

app_name = 'core'

urlpatterns = [
    path('lema/', LemaList.as_view(), name='lema-list-page'),
    path('lema/<slug:pk>/', LemaDetail.as_view(), name='lema-detail-page'),

    path('type_pronunciation/', TypePronunciationList.as_view(),
         name='type_pronunciation-list-page'),
    path('type_pronunciation/<slug:pk>/', TypePronunciationDetail.as_view(),
         name='type_pronunciation-detail-page'),

    path('pronunciation/', PronunciationList.as_view(),
         name='pronunciation-list-page'),
    path('pronunciation/<slug:pk>/', PronunciationDetail.as_view(),
         name='pronunciation-detail-page'),

    path('orthography/', OrthographyList.as_view(), name='orthography-list-page'),
    path('orthography/<slug:pk>/', OrthographyDetail.as_view(),
         name='orthography-detail-page'),

    path('meaning/', MeaningList.as_view(), name='meaning-list-page'),
    path('meaning/<slug:pk>/', MeaningDetail.as_view(),
         name='meaning-detail-page'),

    path('word_type/', WordTypeList.as_view(), name='word_type-list-page'),
    path('word_type/<slug:pk>/', WordTypeDetail.as_view(),
         name='word_type-detail-page'),


    path('sub_group_word/', SubgroupwordList.as_view(),
         name='sub_group_word-list-page'),
    path('sub_group_word/<slug:pk>/', SubgroupwordDetail.as_view(),
         name='sub_group_word-detail-page'),
]
