import requests
import os

class ITunesAdapter():
  """
  Communicates with apple's ITunes DB
  """
  _search_url = os.environ['ITUNES_SEARCH_URL']
  _lookup_url = os.environ['ITUNES_LOOKUP_URL']

  @classmethod
  def search_db(cls, term, options= {}):
    """
    Searches the db for the artist with the given term
    and returns a dictionary as a result.
    """

    # Set itunes defaults
    params = {
      "term": term,
      "media": "music",
      "entity": "album",
      "attribute": "artistTerm",
    }

    # Merge defaults with given options
    params = dict(list(params.items()) + list(options.items()))

    # Send to iTunes
    result = requests.get(cls._search_url, params= params)
    return result.json()

  @classmethod
  def lookup_albums_by_id(cls, id):
    """
    Searches the extrnal DB for albums using the iTunes id
    """
    params = {
      "id": id,
      "media": "music",
      "entity": "album",
    }

    # Send to iTunes
    result = requests.get(cls._lookup_url, params= params).json()
    albums = []

    # Parse the results
    if result["resultCount"] > 0:
      # Pop the first item, it is not an album
      albums = result["results"]
      albums.pop(0)

    return albums

  @classmethod
  def search_artist_id(cls, name):
    """
    Searches the DB and filters the result for an exact match
    returns the external id if found, otherwise None.
    """

    result = cls.search_db(name, { "entity": "musicArtist", "limit": 1 })
    id = None

    # Check if there are any results
    if result["resultCount"] > 0:
      artist_record = result["results"][0]

      # Check if the extenral results string matches the query
      if artist_record["artistName"].lower() == name.lower():
        id = artist_record["artistId"]

    return id