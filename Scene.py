class Scene:

    lines_dict = {}
    LINES_SEPERATOR = ", "

    def __init__(self, movie, character_set, lines, text):
        self.movie = movie
        self.character = character_set
        self.lines = lines
        self.text = text

    def set_character(self, old_val, new_val):
        if old_val in self.character:
            self.character.remove(old_val)
            self.character.add(new_val)

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
