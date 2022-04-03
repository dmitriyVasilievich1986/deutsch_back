from .models import GroupModel, WortModel, ThemeModel, WortThemeModel
from rest_framework import serializers


class WortSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = WortModel


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ThemeModel


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = GroupModel


class WortThemeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = WortThemeModel
