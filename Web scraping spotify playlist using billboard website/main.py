import spotipy
from bs4 import BeautifulSoup
import requests
from spotipy.oauth2 import SpotifyOAuth
import os

user_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

billboard_url = f"https://www.billboard.com/charts/hot-100/{user_input}/"

response = requests.get(billboard_url)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
song_titles_words = [title.getText().split() for title in soup.select(selector="li h3")]
song_tiles = [" ".join(words) for words in song_titles_words]
print(song_tiles)

# ------------------------------------- SPOTIFY SETUP ---------------------------------
CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
REDIRECT_URI = "http://example.com"

scope = "playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"))

user = sp.current_user()["id"]

year = f"hot-100: {user_input.split('-')[0]}"
song_uris = []
for song in song_tiles:
    result = sp.search(q=f"track: {song} year: {year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")

playlist = sp.user_playlist_create(user=user, name=f"{year} Billboard top 100", public=False, collaborative=False,
                                   description="Top 100 Billboard songs done by web scraping")

# Define the maximum number of tracks to add in each request
batch_size = 50

# Split the list of song URIs into batches
song_uris_batches = [song_uris[i:i+batch_size] for i in range(0, len(song_uris), batch_size)]

# Iterate over each batch and add tracks to the playlist
for song_uris_batch in song_uris_batches:
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris_batch)
