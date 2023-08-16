from django.shortcuts import render

from .models import Band, Album


def album_details(request, band_id, album_id):
    band = Band.objects.get(pk=band_id)
    album = Album.objects.get(pk=album_id)
    return render(request, "bands/album-details.html", {"band": band, "album": album})
