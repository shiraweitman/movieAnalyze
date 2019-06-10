import re
import Scene


class MovieParser:

    Location_pattern = re.compile("^\s*(INT\.|EXT\.)")
    Name_pattern = re.compile("                               [A-Z]{2,}")
    End_of_speach = re.compile("^$")

    def __init__ (self, path):
        self.__file_path =path
        self.__file = open(path, "r")
        self.__characters = set()





    def get_scene(self):
        conversation = []
        speach = ""
        line = self.__file.readline()
        while line:
            match_name = re.search(MovieParser.Name_pattern, line)
            if match_name:
                conversation.append(self.get_conversation(line))
            line = self.__file.readline()

    def get_conversation(self, line):
        conversation = []

        match_name = re.search(MovieParser.Name_pattern, line)
        while match_name:
            name = line.strip()
            print(name)
            self.__characters.add(name)
            conversation.append(self.get_speach())
            line = self.__file.readline()
            match_name = re.search(MovieParser.Name_pattern, line)

        return conversation

    def get_speach(self,):
        speech = ""
        line = self.__file.readline()
        match = re.search(MovieParser.End_of_speach, line)
        while not match:
            speech = speech+line
            line = self.__file.readline()
            match = re.search(MovieParser.End_of_speach, line)
        print(speech)
        return speech



# movie = MovieParser("movie")
# movie.get_scene()
s = Scene.Scene()



