from django.shortcuts import render, get_object_or_404
from artists.models import *
from artists.utils import ITunesAdapter
from django.http import HttpResponse, HttpResponseNotAllowed
import json

def index(request, artist_id=None):

  # Get the selected artist if specified
  selected_artist = None
  if artist_id:
    selected_artist = get_object_or_404(Artist, pk=artist_id)

  return render(
    request,
    'artists/index.html',{
      "selected_artist": selected_artist,
      "artists": Artist.objects.all
      }
    )

def new(request):
  return render(request, 'artists/new.html')

def create(request):
  """
  Create a new artist, save it and populate it with albums
  """

  # Allow only POST requests
  if request.method == 'POST':
    artist_added = False
    artist_name = request.POST.get('artist_name')

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
  else:
    return HttpResponseNotAllowed(['post'])
