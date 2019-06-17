class Conversation:

    lines_dict = {}
    LINES_SEPERATOR = ", "

    def __init__(self, movie, character_set, lines, text):
        self.movie = movie
        self.character_set = character_set
        self.male_characters = set()
        self.text = text
        self.lines = lines # one string with all lines
        for character in self.character_set:
            if character.get_gender() == "m":
                self.male_characters.add(character)

    def get_characters(self):
        return self.character_set

    def get_male_characters(self):
        return self.male_characters

    def get_lines(self):
        return self.lines

    def set_character(self, old_val, new_val):
        self.character_set.remove(old_val)
        self.character_set.add(new_val)

    def get_lines_text(self):
        conversation_text = ""
        lines = self.lines.split(self.LINES_SEPERATOR)
        for line in lines:
            line1 = line.strip("[")
            line2 = line1.strip("]")
            line3 = line2.strip("'")
            text = self.lines_dict.get(line3)
            conversation_text = conversation_text+text
        self.text = conversation_text
