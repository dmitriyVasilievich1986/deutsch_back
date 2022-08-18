from .serializer import MainWordSerializer, ThemeSerializer, WordThemeSerializer
from .models import MainWordModel, ThemeModel, WordThemeModel
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.decorators import action
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

    @action(detail=False, methods=["GET"])
    def randomize(self, request, *args, **kwargs):
        return Response({"rand": MainWordModel.get_random_dativ()})


class GroupViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        payload = [
            {"id": i, "name": x.value}
            for i, x in enumerate(settings.GROUPS, 1)
        ]
        return Response(payload)

    def retrieve(self, request, pk=None, *args, **kwargs):
        if not pk in settings.GROUPS.__members__:
            raise NotFound
        return Response({"message": "ok"})


class WordThemeViewSet(viewsets.ModelViewSet):
    queryset = WordThemeModel.objects.all()
    serializer_class = WordThemeSerializer
