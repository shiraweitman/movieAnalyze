
import Character
import Movie
import Conversation


class Bechdel:

    male_references = ["him", "his", "he"]
    female_references = ["her", "she", "her's"]
    NOT_PASSED = False
    PASSED = True


    def __init__(self, movie):
        self.__movie = movie
        self.test1 = False
        self.test2 = False
        self.test3 = False
        self.overall = False
        self.conversation_passed = 0

        self.men1 = False
        self.men2 = False
        self.men3 = False
        self.overall_men = False



    def run_bechdel_test(self):
        self.first()
        self.bechdel_men1()
        self.second()
        print(self.__movie.movie_name)
        print(str(self.test1) + " bechdel test 1")
        print(str(self.test2) + " bechdel test 2")
        print(str(self.test3) + " bechdel test 3")
        if(self.test1&self.test2&self.test3):
            self.overall = True
            print(self.__movie.movie_name+ " passed bechdel test")
        else: print(self.__movie.movie_name+ " did not pass bechdel test")
        if (self.men1 & self.men2 & self.men3):
            self.overall_men = True
            print(self.__movie.movie_name+ " passed men bechdel test")




    """ return true if passed test 1 (movie has at least two women in it """
    def first(self):
        number_of_women = 0
        if len(self.__movie.get_females()) >=2:
            self.test1 = True

    """ test two: at least two women talk to each other
     returns a specific conversation if found, False if didnt fins
     conversation"""
    def second(self):
        for conversation in self.__movie.get_conversations():
            if self.get_gender_in_conversation(conversation, "f"):
                self.test2 = Bechdel.PASSED
                if self.test_three(conversation):
                    self.conversation_passed+=1 #count how many
                    # conversations pass bechdel test
                    self.test3 = Bechdel.PASSED
            if self.get_gender_in_conversation(conversation, "m"):
                self.men2 = True
                if(self.bechdel_men3(conversation)):
                    self.men3 = True



        return

    """ test three: the women in the conversation talk about something
    beside a man"""
    def test_three(self, conversation):
        male_characters = conversation.get_male_characters()
        for word in conversation.text.split():
            if word in Bechdel.male_references or word in male_characters:
                return False
        return True

    """checks if this conversation has at least two female characters
    """
    def get_gender_in_conversation(self, conversation, gender):
        gender_counter = 0
        for character in conversation.get_characters():
            if character.get_gender() == "f":
                gender_counter+=1
            if gender_counter == 2:
                return True
        return False

    def bechdel_men1(self):
        if(len(self.__movie.get_male())>=2):
            self.men1 = True

    def bechdel_men3(self, conversation):
        female_characters = conversation.get_female_characters()
        for word in conversation.text.split():
            if word in Bechdel.female_references or word in female_characters:
                return False
        return True




character1 = Character.Character(1,"CAMERON", "10 things", "m")
character2 = Character.Character(2,"MICHAEL", "10 things", "m")
characters_1 = set()
characters_1.add(character1)
characters_1.add(character2)
text = "That girl -- I -- You burn, you pine, you perish? Who is she? Bianca Stratford.  Sophomore. Don't even think about it "
con1 = Conversation.Conversation("7",characters_1,[], text)

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
con2 = Conversation.Conversation("7",characters_2,[], text2)
movie_characters = set()
movie_characters.add(character1)
movie_characters.add(character2)
movie_characters.add(character3)
movie_characters.add(character4)
#
text2 = "Can you turn down the Screaming Menstrual Bitches?  I'm trying to " \
        "becoming normal? It means that Gigglepuss is playing at Club Skunk and" \
        " we're going. Oh, I thought you might have a date.I don't know why" \
        " I'm bothering to ask, but are you going to Bogey Lowenstein's " \
        "party Saturday night? What do you think? I think you're'a ' \
        'freak.  I think you do this to torture me.  And I think you suck. "
con2 = Conversation.Conversation("7",characters_2,[], text2)
movie_characters = set()
movie_characters.add(character1)
movie_characters.add(character2)
movie_characters.add(character3)
movie_characters.add(character4)
#
movie = Movie.Movie(1, "try movie", [con1, con2], movie_characters,
                    "comedy", 1991)
movie.set_character_genders()
test = Bechdel(movie)
test.run_bechdel_test()





