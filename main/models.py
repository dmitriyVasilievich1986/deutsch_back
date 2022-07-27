from django.conf import settings
from django.db import models
from random import choice


class ThemeModel(models.Model):
    name = models.CharField(max_length=150, unique=True)


class MainWordModel(models.Model):
    word = models.CharField(max_length=150, null=False, unique=True)
    path = models.CharField(max_length=150, null=True, unique=True)
    translate = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True, blank=True)

    accusative = models.TextField(null=True, blank=True)
    genitive = models.TextField(null=True, blank=True)
    dative = models.TextField(null=True, blank=True)

    pronoun_i = models.TextField(null=True, blank=True)
    pronoun_you = models.TextField(null=True, blank=True)
    pronoun_he = models.TextField(null=True, blank=True)
    pronoun_you_many = models.TextField(null=True, blank=True)
    pronoun_we = models.TextField(null=True, blank=True)
    pronoun_they = models.TextField(null=True, blank=True)

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

    @staticmethod
    def get_random_dativ():
        pron, pron_rs, pron_ru = MainWordModel.get_random_pronoun()

        verb_rs, verb_ru = MainWordModel.get_word_random(group="verb",declination=f"pronoun_{pron}")
        adj_rs, adj_ru = MainWordModel.get_word_random(group="adjective")
        noun_rs, noun_ru = MainWordModel.get_word_random()

        phrase = f"{pron_rs} {verb_rs} {adj_rs} {noun_rs} / {pron_ru} {verb_ru} {adj_ru} {noun_ru}"
        return phrase

    @staticmethod
    def get_random_pronoun():
        random_pronoun = choice(list(settings.PRONOUN.keys()))
        pronoun_rs = settings.PRONOUN[random_pronoun]["rs"]
        pronoun_ru = settings.PRONOUN[random_pronoun]["ru"]
        return random_pronoun, pronoun_rs, pronoun_ru

    @staticmethod
    def get_word_random(declination: str="accusative", group="noun"):
        item = choice(MainWordModel.objects.filter(group=group))
        item_rs = item.__dict__[declination]
        item_ru = item.translate
        return item_rs, item_ru


class WordThemeModel(models.Model):
    word = models.ForeignKey(
        on_delete=models.CASCADE,
        to=MainWordModel,
    )
    theme = models.ForeignKey(
        on_delete=models.CASCADE,
        to=ThemeModel,
    )
