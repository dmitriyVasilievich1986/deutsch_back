from django.db import models


class GroupModel(models.Model):
    name = models.CharField(max_length=150, unique=True)


class ThemeModel(models.Model):
    name = models.CharField(max_length=150, unique=True)


class WortModel(models.Model):
    wort = models.CharField(max_length=150, null=False, unique=True)
    translate = models.CharField(max_length=150, null=False)
    group = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="wort",
        to=GroupModel,
        null=True,
    )


class WortThemeModel(models.Model):
    wort = models.ForeignKey(
        on_delete=models.DO_NOTHING,
        to=WortModel,
    )
    theme = models.ForeignKey(
        on_delete=models.DO_NOTHING,
        to=ThemeModel,
    )
