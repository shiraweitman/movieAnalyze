class Conversation:

    def __init__(self, movie, character_set, lines, txt):
        self.movie = movie
        self.character_set = character_set
        self.male_characters = set()
        self.lines = lines
        self.txt = txt


    def get_characters(self):
        return self.character_set

    def get_male_characters(self):
        return self.male_characters

    def get_female_characters(self):
        return self.female_characters


    def get_lines(self):
        return self.lines

    def set_character(self, old_val, new_val):
        self.character_set.remove(old_val)
        self.character_set.add(new_val)

