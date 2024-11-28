from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
import lyricsgenius
from main_window import TOKEN

genius = lyricsgenius.Genius(TOKEN)

Form, Window = uic.loadUiType("main_window.ui")

def get5_tracks():
    artist_name = input("Write the name of artist: ")
    artist_5_tracks = genius.search_artist(artist_name, max_songs=5, include_features=True)
    print(artist_5_tracks.songs)

def get_text():
    song_name = input("Write the name of song: ")
    artist_name = input("Write the name of artist: ")
    song_text = genius.search_song(song_name, artist_name)
    print(song_text.lyrics)

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

#form.pushButton.clicked.connect()
window.show()
app.exec()