from django.db import models

class Artist(models.Model):
  class Meta:
    # Set default order
    ordering = ['name']

  name = models.CharField(max_length=200, unique=True)
  external_id = models.IntegerField(null=True)

  def __str__(self):
    return self.name

  @classmethod
  def create_from_source(cls, name, external_db_adapter):
    """
    Creates an Artists instance using an external DB. 
    Returns the artist instance or None if no artist was found.
    This method does not persist the instance
    """
    # Get the unique id in the ext db
    name = name.lower()
    external_id = external_db_adapter.search_artist_id(name)
    if external_id:
      return Artist(name=name, external_id=external_id)
    else:
      return None
    # if id:
    #   albums = external_db_adapter.lookup_albums_by_id(id)

    #   # Create an artist instance
    #   artist = Artist(name: name)
    #   artist.save()

    # else:
    #   return None

class Album(models.Model):
  class Meta:
    # Set default order
    ordering = ['name']
    
  artist = models.ForeignKey(Artist)
  name = models.CharField(max_length=200)
  cover_url = models.CharField(max_length=800)

  def __str__(self):
    return self.name

  @classmethod
  def create_albums_from_source_by_artist(cls, artist_source_id, external_db_adapter):
    """
    Searches the external DB using the artist_source_id which is the
    artist's unique id in the external DB and returns a list of all
    albums.
    This method does not persist the instance
    """
    results = external_db_adapter.lookup_albums_by_id(artist_source_id)
    albums = []
    for result in results:
      name = result["collectionName"]
      cover_url = result["artworkUrl60"]
      albums.append(Album(name=name, cover_url=cover_url))
    return albums