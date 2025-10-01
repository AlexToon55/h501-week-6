# Exercise 1
import os
from apputil import Genius

genius = Genius(access_token="access_token")




# Exercise 2

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
search_term = "Missy Elliott"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={ACCESS_TOKEN}"

# here, we make a "GET" request to the Genius server
response = requests.get(genius_search_url)
json_data = response.json()


#Exercise 3