from django.urls import path, include
from main.views import index_view

urlpatterns = [
    path('api/', include("main.urls")),
    path('<path:resource>', index_view),
    path('', index_view),
]
