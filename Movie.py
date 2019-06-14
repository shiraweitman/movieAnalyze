class Movie:

    def __init__(self, ID, name, scenes, characters, genres):
        self.movieID = ID
        self.__movieName = name
        self.conversation = scenes
        self.characters = characters
        self.__genres = genres
