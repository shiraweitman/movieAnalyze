class Movie:

    def __init__(self, ID, name, scenes, characters, genres, year):
        self.movieID = ID
        self.movie_name = name
        self.conversation = scenes
        self.characters = characters
        self.genres = genres
        self.year = year


    def set_conversations(self, conversations):
        self.conversation = conversations

    def set_characters(self, characters):
        self.characters = characters

    def get_characters(self):
        return self.characters

    def get_conversations(self):
        return self.conversation
