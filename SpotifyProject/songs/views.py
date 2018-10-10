from django.shortcuts import render

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


#Just to see if its working console side.....
"""
client_credentials_manager = SpotifyClientCredentials(
            client_id='03a2bd9729c1417e9754db9052b8a8bc',
            client_secret='0c3ccfbab93842a29c283ec3d80dbe4d')

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_playlists('roykebab')

while playlists:
     for i, playlist in enumerate(playlists['items']):
         print ("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'], playlist['name']))
     if playlists['next']:
         playlists = sp.next(playlists)
     else:
         playlists = None
"""

#MAIN VIEW

from django.http import HttpResponse

#Grab data from Spotify API and display it on the django website....
def index(request):

    client_credentials_manager = SpotifyClientCredentials(
            client_id='03a2bd9729c1417e9754db9052b8a8bc',
            client_secret='0c3ccfbab93842a29c283ec3d80dbe4d')
    
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    playlists = sp.user_playlists('roykebab')

    results = []

    while playlists:
        for i, playlist in enumerate(playlists['items']):
            results.append("%4d %s %s" % (i + 1 + playlists["offset"], playlist["uri"], playlist["name"]))
            results.append('\n')
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None

    return HttpResponse(results)


"""
def index(request):
    return HttpResponse("Hello")
"""

