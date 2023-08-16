from django.views.generic import ListView, DetailView
from django.urls import path

from . import views
from .models import Band, Album, Song

app_name = "bands"

urlpatterns = [
    # /bands/
    path(
        "",
        ListView.as_view(
            queryset=Band.objects.all(),
            template_name="bands/bands-list.html",
        ),
        name="bands-list",
    ),
    path(
        "<int:pk>/",
        DetailView.as_view(model=Band, template_name="bands/band-details.html"),
        name="band-details",
    ),
    path(
        "<int:band_id>/albums/<int:album_id>/",
        views.album_details,
        name="album-details",
    ),
]
