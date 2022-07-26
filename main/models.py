from django.conf import settings
from django.db import models


class ThemeModel(models.Model):
    name = models.CharField(max_length=150, unique=True)


class MainWordModel(models.Model):
    word = models.CharField(max_length=150, null=False, unique=True)
    path = models.CharField(max_length=150, null=True, unique=True)
    translate = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True, blank=True)

    genitive = models.TextField(null=True, blank=True)
    dative = models.TextField(null=True, blank=True)

    genus = models.CharField(
        choices=[(x.value,x.value) for x in settings.GENUSES],
        default=settings.GENUSES.masculine.value,
        max_length=50,
        blank=False,
        null=False,
    )

    group = models.CharField(
        choices=[(x.value,x.value) for x in settings.GROUPS],
        default=settings.GROUPS.noun.value,
        max_length=50,
        blank=False,
        null=False,
    )


class WordThemeModel(models.Model):
    word = models.ForeignKey(
        on_delete=models.CASCADE,
        to=MainWordModel,
    )
    theme = models.ForeignKey(
        on_delete=models.CASCADE,
        to=ThemeModel,
    )
