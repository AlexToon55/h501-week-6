from apputil import Genius
from pathlib import Path
from dotenv import load_dotenv
import os

# Load environment variables from the .env file

env_path = Path(__file__).with_name("environ.env")
load_dotenv("environ.env")
#print("token loaded", bool(os.getenv("ACCESS_TOKEN")))

genius = Genius(os.getenv("ACCESS_TOKEN"))


# Smoke test - the following code should return a dictionary of artist information:

genius.get_artist("Radiohead")
