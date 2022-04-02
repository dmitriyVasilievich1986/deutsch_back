from .views import GroupViewSet, WortViewSet, ThemeViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'group', GroupViewSet)
router.register(r'theme', ThemeViewSet)
router.register(r'wort', WortViewSet)
urlpatterns = router.urls
