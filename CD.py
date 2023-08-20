class CD:

    def __init__(self, name, artist, album):
        self.name = name
        self.artist = artist
        self.album = album

    def __str__(self):
        return self.name + " by " + self.artist + ("" if self.album == 'single' else " from " + self.album)
