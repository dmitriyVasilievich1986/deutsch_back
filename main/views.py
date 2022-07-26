from .serializer import MainWordSerializer, ThemeSerializer, WordThemeSerializer
from .models import MainWordModel, ThemeModel, WordThemeModel
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from django.conf import settings


def index_view(request, *args, **kwargs):
    return render(request, "base.html")


class ThemeViewSet(viewsets.ModelViewSet):
    serializer_class = ThemeSerializer
    queryset = ThemeModel.objects.all()


class WordViewSet(viewsets.ModelViewSet):
    serializer_class = MainWordSerializer
    queryset = MainWordModel.objects.all()


class GroupViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        return Response([x.value for x in settings.GROUPS])

    def retrieve(self, request, pk=None, *args, **kwargs):
        if not pk in settings.GROUPS.__members__:
            raise NotFound
        return Response({"message":"ok"})


class WordThemeViewSet(viewsets.ModelViewSet):
    queryset = WordThemeModel.objects.all()
    serializer_class = WordThemeSerializer
