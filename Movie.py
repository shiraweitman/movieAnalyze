class Movie:

    def __init__(self, ID, name, conversations, characters, genres):
        self.__movieID = ID
        self.__movieName = name
        self.__conversation = conversations
        self.__characters = characters
        self.__genres = genres

    def set_conversations(self, conversations):
        self.__conversation = conversations

    def set_characters(self, characters):
        self.__characters = characters

    def get_characters(self):
        return self.__characters

    def get_conversations(self):
        return self.__conversation
