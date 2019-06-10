
import Scene
import Character
import Movie

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
            scene = Scene.Scene(conversation[2], conversation[0],
                                conversation[1], conversation[3])
            scenes_list.append(scene)
        return scenes_list


data = CreateData()
movie_data = []
conversation_data = []
character_data = []
list = data.create_conversation()

for obj in list:
    print(obj.lines+"\n")


