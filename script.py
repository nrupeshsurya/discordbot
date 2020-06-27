import json
import os
import requests
import spotipy 
import spotipy.util as util
import youtube_dl
import urllib


def func(link):
    username = 'enter_username_here'             #username goes here
    scope = 'user-read-private' 
                                                  
    link = link[34:45]
    youtube_url = f"https://www.youtube.com/watch?v={link}"
    video = youtube_dl.YoutubeDL({'quiet': True}).extract_info(
            youtube_url, download=False
        )
    try:
        artist = video['artist']
        songNamee = video['track']
        searchquery = 'track:'+songNamee+' '+'artist:'+artist
    except:
        artist = ''
        songNamee = ''
        searchquery = video['title']

    if songNamee==None:
        searchquery = video['title']


    # print(artist)
    # print(songNamee)

    try:
        token = util.prompt_for_user_token(username,scope,client_id='enter_client_id',client_secret='enter_client_secret',redirect_uri='enter_redirect_url')
    except:
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username,scope,client_id='enter_client_id',client_secret='enter_client_secret',redirect_uri='enter_redirect_url')
    spotifyObject = spotipy.Spotify(auth=token)

    data = spotifyObject.search(q=searchquery)

    # out_file = open("myfile.json", "w")  
    # json.dump(data, out_file, indent = 6)                       
    # out_file.close()

    new_url = 'https://open.spotify.com/track/'
    try:
        new_url+= data['tracks']['items'][0]['id']
        return new_url
    except:
        return 'Cannot find the song!'





