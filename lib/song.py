class Song:
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.count += 1
        Song.genres.add(genre)
        Song.artists.add(artist)

        self.add_to_genre_count()
        self.add_to_artist_count()

    def add_to_genre_count(self):
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1

    @classmethod
    def get_song_count(cls):
        return cls.count

    @classmethod
    def get_genres(cls):
        return cls.genres

    @classmethod
    def get_artists(cls):
        return cls.artists

    @classmethod
    def get_genre_count(cls):
        return cls.genre_count

    @classmethod
    def get_artist_count(cls):
        return cls.artist_count
