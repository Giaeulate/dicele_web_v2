""" Admin Model """
# pylint: disable=too-few-public-methods, missing-class-docstring, protected-access, no-member, wildcard-import, unused-wildcard-import
from django.contrib import admin
from core.models import *
from web.utils import get_custom_admin_list


# @admin.register(GroupWord)
# class GroupAdmin(admin.ModelAdmin):
#     list_display = get_custom_admin_list(GroupWord)


@admin.register(Subgroupword)
class SubgroupAdmin(admin.ModelAdmin):
    list_display = get_custom_admin_list(Subgroupword)


@admin.register(TypePronunciation)
class TypePronunciationAdmin(admin.ModelAdmin):
    list_display = get_custom_admin_list(TypePronunciation)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = get_custom_admin_list(Language)


@admin.register(Lema)
class LemaAdmin(admin.ModelAdmin):
    list_display = get_custom_admin_list(Lema)


@admin.register(Pronunciation)
class PronunciationAdmin(admin.ModelAdmin):
    list_display = get_custom_admin_list(Pronunciation)


@admin.register(Orthography)
class OrthographyAdmin(admin.ModelAdmin):
    list_display = get_custom_admin_list(Orthography)


@admin.register(ImageOrthography)
class ImageOrthographyAdmin(admin.ModelAdmin):
    list_display = get_custom_admin_list(ImageOrthography)


@admin.register(WordType)
class WordTypeAdmin(admin.ModelAdmin):
    list_display = get_custom_admin_list(WordType)


@admin.register(Meaning)
class MeaningAdmin(admin.ModelAdmin):
    list_display = get_custom_admin_list(Meaning)


@admin.register(TranslationMeaning)
class TranslationMeaningAdmin(admin.ModelAdmin):
    list_display = get_custom_admin_list(TranslationMeaning)
