class Character:
    def __init__(self, ID,name, movie, gender):
        self.__ID = ID
        self.__movie = movie
        self.__gender = gender

    def get_gender(self):
        return self.__gender
