import sys
import os
import spotipy
import spotipy.util as util
from random import randint
#Enviromental variables
os.environ["SPOTIPY_CLIENT_ID"] = ""
os.environ["SPOTIPY_CLIENT_SECRET"] = ""
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost/"
#The scopes that we need for read and write.
scope = 'user-library-read playlist-modify-public'

#We receive username when running the script, also you can set it manually.
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Usage: %s username") % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, scope)
tracks=[]
if token:
    sp = spotipy.Spotify(auth=token)
    #The number in range, is the number of songs that you want in your playlist
    for a in range(50):
        #'library_size' represents the number of songs that you have in your library (not necesary the exact amount).
        library_size=50
        ran=randint(0,library_size)
        results = sp.current_user_saved_tracks(limit=1, offset=ran)
        for item in results['items']:
            track = item['track']
            tracks.append(track['id'])
            #print (str(a+1)+".- "+track['id']+" "+str(track['name'].encode('ascii', 'ignore')) + ' - ' + str(track['artists'][0]['name'].encode('ascii', 'ignore')))
    sp.trace = False
    results = sp.user_playlist_replace_tracks(username, 'playlist_id', tracks)
    print (results)
else:
    print ("Can't get token for", username)
