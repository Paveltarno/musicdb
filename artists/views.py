from django.shortcuts import render
from artists.models import *
from artists.utils import ITunesAdapter
import json

def index(request):
  return render(request, 'artists/index.html')

def add_artist(request, artist_name):
  artist_added = False

  # Query the artist
  artist = Artist.create_from_source(artist_name, ITunesAdapter)
  if artist:
    artist.save()

    # Check for the artists albums
    albums = Album.create_albums_from_source_by_artist(artist.external_id, ITunesAdapter)
    for album in albums:
      artist.album_set.add(album)
    artist_added = True

  message = "Albums Added." if artist_added else "Artist not found."
  return HttpResponse(json.dumps({'message': message}), content_type="application/json")
