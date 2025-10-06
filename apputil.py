import requests

# Exercise 1 - Creating a class called genius
class Genius:
  def __init__(self, access_token):
      if not access_token:
          raise ValueError("Access token is required")
      self.access_token = access_token

  # Exercise 2
  #Create a method for our `Genius` class called `.get_artist(search_term)` which does the following:
  # 1. Extract the (most likely, "Primary") Artist ID from the first "hit" of the `search_term`.
  # 2. Use the [API path](https://docs.genius.com/#artists-h2) for this Artist ID to pull information about the artist.
  # 3. **Return** the dictionary containing the resulting JSON object.

def get_artist(self, search_term):
    # Searching the artist — include token + per_page in the URL
    search_URL = f"http://api.genius.com/search?q={search_term}&access_token={self.access_token}&per_page=15"
    response = requests.get(search_URL)
    json_data = response.json()
    hits = json_data['response']['hits']

    genius_id = hits[0]['result']['primary_artist']['id']
    genius_URL = f"http://api.genius.com/artists/{genius_id}?access_token={self.access_token}"
    genius_response = requests.get(genius_URL)
    artist_data = genius_response.json()

    return artist_data['response']['artist']


  # Exercise 3