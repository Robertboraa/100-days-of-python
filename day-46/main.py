import os
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

DATE = "2002-06-08"
URL = f"https://appbrewery.github.io/bakeboard-hot-100/{DATE}/"
CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.environ.get("SPOTIFY_REDIRECT_URI")

# Scrape songs
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
song_names = soup.find_all("h3", class_="chart-entry__title")
songs = [song.getText() for song in song_names]

# Spotify setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="playlist-modify-private playlist-modify-public",
    cache_path=".cache"
))

# Search and collect URIs
song_uris = []
for song in songs:
    result = sp.search(q=f"track:{song} year:{DATE[:4]}", type="track", limit=1)
    tracks = result["tracks"]["items"]
    if tracks:
        song_uris.append(tracks[0]["uri"])
        print(f"Found: {tracks[0]['name']}")
    else:
        print(f"Not found: {song}")

# Create playlist and add songs
user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"{DATE} Billboard 100", public=False)
sp.playlist_add_items(playlist["id"], song_uris)
print("Playlist created!")


