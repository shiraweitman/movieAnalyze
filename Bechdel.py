
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
        for conversation in self.__movie.get_conversations():
            if self.get_gender_in_conversation(conversation):
                passed_test_two = True
                if self.test_three(conversation):
                    passed_test_three = True
        return passed_test_two, passed_test_three

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
        for character in conversation.get_characters():
            if character.get_gender() == "f":
                number_of_women+=1
            if number_of_women == 2:
                return True
        return False


character1 = Character.Character(1,"CAMERON", "10 things", "m")
character2 = Character.Character(2,"MICHAEL", "10 things", "m")
characters_1 = set()
characters_1.add(character1)
characters_1.add(character2)
text = "That girl -- I -- You burn, you pine, you perish? Who is she? Bianca Stratford.  Sophomore. Don't even think about it "
con1 = conversation.Conversation("7",characters_1, text)

character3 = Character.Character(3,"BIANCA", "10 things", "f")
character4 = Character.Character(4,"KAT", "10 things", "f")
characters_2 = set()
characters_2.add(character3)
characters_2.add(character4)

text2 = "Can you turn down the Screaming Menstrual Bitches?  I'm trying to " \
        "becoming normal? It means that Gigglepuss is playing at Club Skunk and" \
        " we're going. Oh, I thought you might have a date.I don't know why" \
        " I'm bothering to ask, but are you going to Bogey Lowenstein's " \
        "party Saturday night? What do you think? I think you're'a ' \
        'freak.  I think you do this to torture me.  And I think you suck. "
con2 = conversation.Conversation("7",characters_2, text2)
movie_characters = set()
movie_characters.add(character1)
movie_characters.add(character2)
movie_characters.add(character3)
movie_characters.add(character4)


movie = Movie.Movie(1, "try movie",[con1, con2], movie_characters,"comedy")

test = Bechdel(movie)
print(test.second())





