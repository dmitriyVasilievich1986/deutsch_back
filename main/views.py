from .serializer import WortSerializer, GroupSerializer, ThemeSerializer
from .models import WortModel, GroupModel, ThemeModel
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets


def index_view(request, *args, **kwargs):
    return render(request, "base.html")


class ThemeViewSet(viewsets.ModelViewSet):
    serializer_class = ThemeSerializer
    queryset = ThemeModel.objects.all()


class WortViewSet(viewsets.ModelViewSet):
    serializer_class = WortSerializer
    queryset = WortModel.objects.all()


class GroupViewSet(viewsets.ModelViewSet):
    queryset = GroupModel.objects.all()
    serializer_class = GroupSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        payload = {
            "group": serializer.data,
            "wort": [WortSerializer(instance=x).data for x in instance.wort.all()]
        }
        return Response(payload)
