import json
import os
import requests
import spotipy 
import spotipy.util as util
import youtube_dl
import urllib
from ytmusicapi import YTMusic

def func(link):
    ytmusic = YTMusic()

    username = 'enter_username'             #username goes here
    scope = 'user-read-private'
    link = link[0:53]
    # link = input("Enter the spotify link of the song: ")   
    song_id=''   
    l = len(link)
    for i in range(l):
        if link[l-i-1]=='/':
            break
        song_id+=link[l-i-1]
    song_id = song_id[::-1]
    

    try:
        token = util.prompt_for_user_token(username,scope,client_id='enter_client_id',client_secret='enter_client_secret',redirect_uri='enter_redirect_url')
    except:
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username,scope,client_id='enter_client_secret',client_secret='enter_client_secret',redirect_uri='enter_redirect_url')
    spotifyObject = spotipy.Spotify(auth=token)

    data = spotifyObject.track(song_id)

    songName = data['name']

    artistName = data['artists'][0]['name']

    search = ytmusic.search(query=songName+' '+artistName,filter='songs')
    search1 = ytmusic.search(query=songName+' '+artistName)
    url='https://music.youtube.com/watch?v='
    try:
        url+=search[0]['videoId']
    except:
        url+=search[1]['videoId']
    # print("the ytmusic url for the song is: "+url)
    return url

# if __name__=='__main__':
#     func()

