from .views import GroupViewSet, WordViewSet, ThemeViewSet, WordThemeViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'group', GroupViewSet, basename="group")
router.register(r'wordtheme', WordThemeViewSet)
router.register(r'theme', ThemeViewSet)
router.register(r'word', WordViewSet)
urlpatterns = router.urls
