import pprint

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="Your_Spotify_ID",
                                               client_secret="Your_Spotify_secret",
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"
                                               ))
user_id = sp.current_user()["id"]

user_date_input = input("What year you would like to travel to? Please, input date in format YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{user_date_input}/"
# 2000-08-12
# {user_date_input}
response = requests.get(url=URL)
data = response.text

soup = BeautifulSoup(data, "html.parser")
first_song = soup.find(name="h3", id="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")
song_names_spans = soup.find_all("h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

songs = soup.find_all(name="div", class_="o-chart-results-list-row-container")
singers_list = []

for song in songs:
    singers = song.find_all(name="span", class_="c-label")
    singer_lists = [singer.getText()[1:-1] for singer in singers]
    singe = singer_lists[1]
    singers_list.append(singe)

print(len(singers_list))

song_list = [song.getText().replace('\n', '') for song in song_names_spans]
song_list.insert(0, first_song.getText().replace('\n', ''))
songs_uris = []
i = 0

for song in song_list:
    result = sp.search(q=f"track:{song} artist:{singers_list[i]}", type="track")
    print(result)
    i += 1
    try:
        uri = result["tracks"]["items"][0]["uri"]
        songs_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{user_date_input} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uris)


