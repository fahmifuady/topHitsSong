# membuat data yang bersumber dari spotify

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

# keperluan auth
os.environ["SPOTIPY_CLIENT_ID"] = "your client id"
os.environ["SPOTIPY_CLIENT_SECRET"] = "your client secret"
os.environ["SPOTIPY_REDIRECT_URI"] = 'http://localhost:8888/callback'

# Sets up authentication and scope.
auth_manager = SpotifyOAuth(scope="playlist-modify-public", 
                            open_browser=False)

print(auth_manager.get_authorize_url())


auth_manager.get_access_token("your access token", as_dict=False)

spotify = spotipy.Spotify(auth_manager=auth_manager)

user_dict = spotify.current_user()
print(user_dict)