from .models import MainWordModel, ThemeModel, WordThemeModel
from rest_framework import serializers


class MainWordSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = MainWordModel


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ThemeModel


class WordThemeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = WordThemeModel
