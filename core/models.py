""" Core Model """
# pylint: disable=too-few-public-methods, missing-class-docstring, no-member
import uuid
from django.db import models


class AutoDateTimeAbstract(models.Model):
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AutoDateTimeIdAbstract(AutoDateTimeAbstract):
    id = models.CharField(primary_key=True, max_length=150,
                          default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TypePronunciation(AutoDateTimeAbstract):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Tipo de pronunciación'
        verbose_name_plural = 'Tipos de pronunciación'

    def __str__(self):
        return f"{self.name}"


class Language(AutoDateTimeAbstract):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Idioma'
        verbose_name_plural = 'Idiomas'

    def __str__(self):
        return f"{self.name}"


class Lema(AutoDateTimeAbstract):
    name = models.CharField(
        primary_key=True, max_length=150, verbose_name='Lema')
    regular_form = models.CharField(
        max_length=150, verbose_name='Forma regular')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Lema'
        verbose_name_plural = 'Lemas'

    def __str__(self):
        return f"{self.name}"


class Pronunciation(AutoDateTimeAbstract):
    name = models.CharField(max_length=255, verbose_name='Pronunciación')
    type_pronunciation = models.ForeignKey(
        TypePronunciation, on_delete=models.CASCADE, verbose_name='Tipo de pronunciación')
    variant = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Variante')
    observation = models.TextField(
        blank=True, null=True, verbose_name='Observación')
    prosodic_variant = models.CharField(
        max_length=255, blank=True, null=True, verbose_name='Variante Prosódica')
    variant_observation = models.TextField(
        blank=True, null=True, verbose_name='Observación Variante Prosódica')
    lema = models.ForeignKey(Lema, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Pronunciación'
        verbose_name_plural = 'Pronunciaciones'

    def __str__(self):
        return f"{self.name}"


class Orthography(AutoDateTimeAbstract):
    syllabic_division = models.CharField(
        max_length=150, verbose_name='División silábica')
    observation = models.TextField(
        blank=True, null=True, verbose_name='Observación')
    lema = models.ForeignKey(Lema, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Ortografía'
        verbose_name_plural = 'Ortografías'

    def __str__(self):
        return f"{self.id} - {self.syllabic_division}"


class ImageOrthography(AutoDateTimeAbstract):
    image = models.ImageField(
        blank=True, null=True, verbose_name='Imagen', upload_to='core/orthography/')
    orthography = models.ForeignKey(
        Orthography, on_delete=models.CASCADE, verbose_name='Ortografía')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Imagen de la ortografía'
        verbose_name_plural = 'Imagenes de la ortografía'

    def __str__(self):
        return f"{self.id}"


class WordType(AutoDateTimeAbstract):
    name = models.CharField(max_length=150, verbose_name='Tipo de palabra')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Tipo de Palabra'
        verbose_name_plural = 'Tipos de Palabra'

    def __str__(self):
        return f"{self.name}"


mcer_choices = [
    ('A1', 'A1'),
    ('A2', 'A2'),
    ('B1', 'B1'),
    ('B2', 'B2'),
    ('C1', 'C1'),
    ('C2', 'C2'),
]


class Meaning(AutoDateTimeAbstract):
    name = models.CharField(max_length=150, verbose_name='Acepción')
    index = models.IntegerField(default=0, verbose_name='Índice')
    mcer = models.CharField(max_length=5, verbose_name='MCER',
                            choices=mcer_choices, default=mcer_choices[0])
    word_type = models.ForeignKey(
        WordType, on_delete=models.CASCADE, verbose_name='Tipo de palabra')
    image = models.ImageField(blank=True, null=True,
                              verbose_name='Imagen', upload_to='core/meaning/')
    lema = models.ForeignKey(Lema, on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Acepción'
        verbose_name_plural = 'Acepciones'

    def __str__(self):
        return f"{self.name}"


class TranslationMeaning(AutoDateTimeAbstract):
    name = models.CharField(max_length=150, verbose_name='Traducción')
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, verbose_name='Idioma')
    meaning = models.ForeignKey(
        Meaning, on_delete=models.CASCADE, verbose_name='Acepción')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Traducción'
        verbose_name_plural = 'Traducciones'

    def __str__(self):
        return f"{self.name}"


# class GroupWord(AutoDateTimeAbstract):
#     word_type = models.ForeignKey(
#         WordType, on_delete=models.CASCADE, verbose_name='Tipo de palabra')
#     name = models.CharField(max_length=100)

#     class Meta:
#         ordering = ('id',)
#         verbose_name = 'Grupo'
#         verbose_name_plural = 'Grupos'

#     def __str__(self):
#         return f"{self.name}"


class FormField(AutoDateTimeAbstract):
    FIELD_TYPE_CHOICES = [
        ('text', 'Text'),
        ('number', 'Number'),
        ('date', 'Date'),
        ('select', 'Select'),
        ('checkbox', 'Checkbox'),
    ]

    name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=20, choices=FIELD_TYPE_CHOICES)

    def __str__(self):
        return self.name


category_choices = [
    ('morph', 'Morfología'),
    ('sintx', 'Sintaxis'),
]

FIELD_TYPE_CHOICES = [
        ('text', 'Text'),
        ('number', 'Number'),
        ('date', 'Date'),
        ('select', 'Select'),
        ('checkbox', 'Checkbox'),
    ]

class Subgroupword(AutoDateTimeAbstract):
    group = models.ForeignKey(WordType, on_delete=models.CASCADE, related_name='subgroups')
    # type = models.ForeignKey(FormField, related_name='options', on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=FIELD_TYPE_CHOICES)
    name = models.CharField(max_length=100)
    field_type = models.CharField(max_length=20, choices=FormField.FIELD_TYPE_CHOICES)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='options', on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=category_choices)

    # group = models.ForeignKey(WordType, on_delete=models.CASCADE, related_name='subgroups')
    # parent_subgroup = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='child_subgroups')
    # name = models.CharField(max_length=100)
    # type = models.CharField(max_length=100, default='select')
    # description = models.TextField(blank=True, null=True)
    # category = models.CharField(max_length=50, choices=category_choices)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Sub Grupo'
        verbose_name_plural = 'Sub Grupos'

    def __str__(self):
        return f"{self.name}"
