import requests
import os

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

    # make the request to search for the artist
    search_URL = "https://api.genius.com/search"
    params = {"q": search_term, "access_token": self.access_token}
    response = requests.get(search_URL, params=params)
    json_data = response.json()

    # variables for the search
    genius_id = json_data['response']['hits'][0]['result']['primary_artist']['id']
    genius_URL = f"https://api.genius.com/artists/{genius_id}?access_token={self.access_token}"
    
    # make the request to get the artist information
    genius_response = requests.get(genius_URL)
    artist_data = genius_response.json()

    # return the artist information
    try:
        return artist_data['response']['artist']
    except (KeyError, TypeError):
        raise ValueError("Artist information not found in the response.")

  # Exercise 3