import requests
import pandas as pd

# Exercise 1 - Creating a class called genius
class Genius:
    def __init__(self, access_token):
        if not access_token:
            raise ValueError("Access token is required")
        self.access_token = access_token

    # Exercise 2

    def get_artist(self, search_term):

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
    # Returns a DataFrame with: search_term, artist_name, artist_id, followers_count
    def get_artists(self, search_terms):
        rows = []
        for term in search_terms:
            artist = self.get_artist(term)
            rows.append({
                'search_term': term,
                'artist_name': artist.get('name'),
                'artist_id': artist.get('id'),
                'followers_count': artist.get('followers_count')
            })
        return pd.DataFrame(rows)