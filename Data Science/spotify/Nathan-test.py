import json
#request library
import requests
import pandas as pd

CLIENT_ID = 'a29366a152fb4eadb703fa817717df26'
CLIENT_SECRET = '8d21bad7bc684df8b69109abb04d030f'

AUTH_URL = 'https://accounts.spotify.com/api/token'

#POSTing a request to our client credentials
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()


access_token = auth_response_data['access_token']

#saving header info here
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

BASE_URL = 'https://api.spotify.com/v1/'

# Track ID from the URI
track_id = '3rmo8F54jFF8OgYsqTxm5d?si=80c3d70ce1f14b97'

# actual GET request with proper header
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

#audio features
r = r.json()

artist_id = '6eUKZXaKkcviH0Ku9w2n3V'

#pulling all of the artists albums
r = requests.get(BASE_URL + 'artists/' + artist_id + '/albums', 
                headers=headers,  
                params={'include_groups':'album', 'limit': 50})
d = r.json()

#look at album that were pulled and release dates:
for album in d['items']:
    print(album['name'], '---', album['release_date'])

data = []   # will hold all track info
albums = [] # to keep track of duplicates

# loop over albums and get all tracks
for album in d['items']:
    album_name = album['name']

    # here's a hacky way to skip over albums we've already grabbed
    trim_name = album_name.split('(')[0].strip()
    if trim_name.upper() in albums or int(album['release_date'][:4]) < 2012:
        continue
    albums.append(trim_name.upper()) # use upper() to standardize
    
    # this takes a few seconds so let's keep track of progress    
    print(album_name)
    
    # pull all tracks from this album
    r = requests.get(BASE_URL + 'albums/' + album['id'] + '/tracks', 
        headers=headers)
    tracks = r.json()['items']
    
    for track in tracks:
        # get audio features (key, liveness, danceability, ...)
        f = requests.get(BASE_URL + 'audio-features/' + track['id'], 
            headers=headers)
        f = f.json()
        
        # combine with album info
        f.update({
            'track_name': track['name'],
            'album_name': album_name,
            'short_album_name': trim_name,
            'release_date': album['release_date'],
            'album_id': album['id']
        })
        
        data.append(f)

        df = pd.DataFrame(data)


        #convert release_date to an actual date, and sort by it
        df['release_date'] = pd.to_datetime(df['release_date'])
        df = df.sort_values(by='release_date')

        df = df[~df['track_name'].str.contains('Live|Mix|Track')]

        df.head()


