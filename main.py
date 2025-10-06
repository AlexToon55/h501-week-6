from apputil import Genius

# access token setup
from dotenv import load_dotenv
load_dotenv("environment.env")

genius = Genius(access_token="access_token")


# Smoke test - the following code should return a dictionary of artist information:

genius.get_artist("Radiohead")
