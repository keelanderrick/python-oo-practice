"""Word Finder: finds random words from a dictionary."""


from random import randrange

class WordFinder:
    def __init__(self, path):
        f = open(path, "r")
        self.words = []
        self.count = 0
        for x in f:
            self.words.append(x[0:-1])
            self.count += 1
        print(str(self.count) + " words read")

    def random(self):
        return self.words[randrange(self.count)]

class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        f = open(path, "r")
        self.words = []
        self.count = 0
        for x in f:
            if(not (x[0] == '#' or x.isspace())):
                self.words.append(x[0:-1])
                self.count += 1
        print(str(self.count) + " words read")