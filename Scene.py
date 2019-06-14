class Scene:

    def __init__(self, movie, character_set, lines):
        self.movie = movie
        self.character = character_set
        self.lines = lines

    def set_character(self, old_val, new_val):
        self.character.remove(old_val)
        self.character.add(new_val)
