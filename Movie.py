class Movie:

    def __init__(self, ID, name, scenes, characters, genres, year):
        self.movieID = ID
        self.movie_name = name
        self.conversation = scenes
        self.characters = characters
        self.genres = genres
        self.year = year

        self.male_char = set()
        self.female_char = set()
        self.conversation_num = len(self.conversation)


    def set_conversations(self, conversations):
        self.conversation = conversations

    def set_characters(self, characters):
        self.characters = characters

    def get_characters(self):
        return self.characters

    def get_conversations(self):
        return self.conversation

    def set_character_genders(self):
        for character in self.characters:
            if character.get_gender()== "f":
                self.female_char.add(character)
            if character.get_gender() == "g":
                self.male_char.add(character)

    def get_females(self):
        return self.female_char

    def get_male(self):
        return self.male_char
