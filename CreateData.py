
import Scene
import Character
import Movie
import conversation

SEPERATOR = " +++$+++ "


def read_file(file_path):
    lines = []
    with open(file_path) as file:
        for line in file:
            line = line.strip()
            lines.append(line)
    return lines


class CreateData:

    movies_names = read_file(r"C:\Users\shira weitman\Documents\שנה ב\Semester"
                             r" A\python\movieAnalyze\cornell movie-dialogs "
                             r"corpus\movie_titles_metadata.txt")

    movie_conversation = read_file(r"C:\Users\shira weitman\Documents\שנה ב"
                                   r"\Semester A\python\movieAnalyze\cornell "
                                   r"movie-dialogs corpus\movie_conversations."
                                   r"txt")

    movie_character = read_file(r"C:\Users\shira weitman\Documents\שנה ב"
                                r"\Semester A\python\movieAnalyze\cornell "
                                r"movie-dialogs corpus\movie_characters_"
                                r"metadata.txt")

    def split_list(self, data_list, new_list):
        for i in range(len(data_list)):
            new_item = data_list[i].split(SEPERATOR)
            new_list.append(new_item)

    def create_conversation(self):
        scenes_list = []
        self.split_list(self.movie_conversation, conversation_data)
        for conversation in conversation_data:
            character_set = set()
            character_set.add(conversation[0])
            character_set.add(conversation[1])
            scene = conversation.Conversation(conversation[2], character_set,
                                   conversation[3])
            scenes_list.append(scene)
        return scenes_list

    def create_character(self):
        character_set = set()
        self.split_list(self.movie_character, character_data)
        for character in character_data:
            new_character = Character.Character(character[0], character[1],
                                                character[2], character[4])
            character_set.add(new_character)
        return character_set

    def match_character(self, movie_id):
        characters = self.create_character()
        movie_characters = set()
        for character in characters:
            if character.movie == movie_id:
                movie_characters.add(character)
        return movie_characters

    def match_conversation(self, movie_id):
        conversations = self.create_conversation()
        movie_conversation = []
        new_id = movie_id.strip("m")
        id = int(new_id)
        for i in range(id, len(conversations)):
            if conversations[i].movie == movie_id:
                movie_conversation.append(conversations[i])
                if conversations[i+1].movie != movie_id:
                    break
        return movie_conversation

    def create_movie(self):
        movies_list = []
        self.split_list(self.movies_names, movie_data)
        for movie in movie_data:
            movie_conversation = self.match_conversation(movie[0])
            movie_characters = self.match_character(movie[0])
            movie = Movie.Movie(movie[0], movie[1], movie_conversation,
                                movie_characters, movie[5])
            self.create_character_obj(movie)
            movies_list.append(movie)
        return movies_list

    def create_character_obj(self, movie):
        # go over the conversation in the movie to set their characters
        for conv in movie.conversation:
            for conv_char in conv.character:
                if type(conv_char) == str:
                    for movie_char in movie.characters:
                        if movie_char.ID == conv_char:
                            conv.set_character(conv_char, movie_char)


# data = CreateData()
# movie_data = []
# conversation_data = []
# character_data = []
#
# character = Character.Character("u161", "GENERAL NORTHWOOD", "m11", "?")
# character2 = Character.Character("u159", "GENERAL NORTHWOOD", "m11", "m")
# my_set = set()
# my_set.add("u161")
# my_set.add("u159")
# movie_set = set()
# movie_set.add(character)
# movie_set.add(character2)
# scene = Scene.Scene("m11", my_set, ['L16842', 'L16843', 'L16844'])
# movie = Movie.Movie("m11", "air force one", [scene], movie_set, "action")
#
# data.create_character_obj(movie)
# for conv in movie.conversation:
#     for finals in conv.character:
#         print(finals.gender)


