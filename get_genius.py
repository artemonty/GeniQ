import lyricsgenius
token = '7ONB6EQoOZ645wKwMmFoU7vbUk0lntjMXQeehfQ-EC2qtW_zy_yObk5fMieyXLVS'

genius = lyricsgenius.Genius(token)

def get5_tracks():
    artist_name = input("Write the name of artist: ")
    artist_5_tracks = genius.search_artist(artist_name, max_songs=5, include_features=True)
    print(artist_5_tracks.songs)

def get_text():
    song_name = input("Write the mame of his song: ")
    artist_name = input("Write the name of artist: ")
    song_text = genius.search_song(song_name, artist_name)
    print(song_text.lyrics)

get_text()