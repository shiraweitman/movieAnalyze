class Movie:

    def __init__(self, ID, name, scenes, characters, genres):
        self.movieID = ID
        self.movieName = name
        self.conversation = scenes
        self.characters = characters
        self.genres = genres

    def set_conversations(self, conversations):
        self.conversation = conversations

    def set_characters(self, characters):
        self.characters = characters

    def get_characters(self):
        return self.characters

    def get_conversations(self):
        return self.conversation
