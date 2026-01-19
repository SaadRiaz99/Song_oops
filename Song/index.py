class Song:
    def __init__(self, song, artist, duration):
        self.song = song
        self.artist = artist
        self.duration = duration

    def detail(self):
        return f"{self.song} by {self.artist} ({self.duration} min)"


class Music:
    def __init__(self):
        self.current_song = None
        self.is_playing = False

    def play(self, song):
        self.current_song = song
        self.is_playing = True
        print(f"▶ Playing: {song.detail()}")

    def pause(self):
        if self.is_playing:
            self.is_playing = False
            print(" Song Paused")
        else:
            print("No song is playing")

    def stop(self):
        if self.current_song:
            print(" Song Stopped")
            self.current_song = None
            self.is_playing = False
        else:
            print("No song to stop")



song1 = Song("Ishq", "Anuv Jain", 4.3)
song2 = Song("Alag Aasmaan", "Anuv Jain", 3.8)

player = Music()

player.play(song1)
player.pause()
player.play(song2)
player.stop()
