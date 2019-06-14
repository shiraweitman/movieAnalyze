
import Character
import Movie
import conversation


class Bechdel:

    male_references = ["him", "his", "he"]

    def __init__(self, movie):
        self.__movie = movie

    """ return true if passed test 1 (movie has at least two women in it """
    def first(self):
        number_of_women = 0
        for character in self.__movie.get_characters():
            if character.get_gender() == "f":
                number_of_women+=1
            if number_of_women == 2:
                return True
        return False

    """ test two: at least two women talk to each other
     returns a specific conversation if found, False if didnt fins
     conversation"""
    def second(self):
        passed_test_two = False
        passed_test_three = False
        for conversation in self.__movie.get_conversations:
            if self.get_gender_in_conversation(conversation):
                passed_test_two = True
                if self.test_three(conversation):
                    passed_test_three = True
        return False

    """ test three: the women in the conversation talk about something
    beside a man"""
    def test_three(self, conversation):
        male_characters = conversation.get_male_characters()
        for word in conversation.get_lines().split():
            if word in Bechdel.male_references or word in male_characters:
                return False
        return True

    """checks if this conversation has at least two female characters
    """
    def get_gender_in_conversation(self, conversation):
        number_of_women = 0
        for character in conversation.get_characters:
            if character.get_gender() == "f":
                number_of_women+=1
            if number_of_women == 2:
                return True
        return False


character1 = Character.Character("1", "BIANCA", "m11", "f")
character2 = Character.Character("1", "CHASTITY ", "m11", "f")

my_set = (character1, character2)
scene = conversation.Conversation("m11", my_set, "Did you change your hair? No. You "
                                      "might "
                                   "wanna think about it ")
movie = Movie.Movie("m11", "air force one", [scene], my_set, "action")

bechdel = Bechdel(movie)
print(bechdel.second())
