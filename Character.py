class Character:
    def __init__(self, ID, name, movie, gender):
        self.ID = ID
        self.name = name
        self.movie = movie
        self.gender = gender


    def get_gender(self):
        return self.gender
