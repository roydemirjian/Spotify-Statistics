from django.shortcuts import render

import sys

import spotipy
#from spotipy.oauth2 import SpotifyClientCredentials

import spotipy.util as util

from django.http import HttpResponse

#Grab data from Spotify API and display it on the django website....
import os
#import json
from json.decoder import JSONDecodeError


"""
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
    
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else: 
        #print "Usage: %s username" % (sys.argv[0],)
        sys.exit()
    
    scope = 'user-library-read'

    try:
        token = util.prompt_for_user_token(username, redirect_uri = 'http://localhost:8000/info/')
    except(AttributeError, JSONDecodeError):
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, redirect_uri = 'http://localhost:8000/info/')

    results =[]

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        while playlists:
            for i, playlist in enumerate(playlists['items']):
                results.append("%4d %s %s" % (i + 1 + playlists['offest'], playlist['uri'], playlist['name']))
                results.append('\n')
            if playlists['next']:
                playlists = sp.next(playlists)
            else:
                playlists = None


    return HttpResponse("hello")


