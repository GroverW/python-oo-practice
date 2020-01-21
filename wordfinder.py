"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    """
    >>> word_finder = WordFinder('originalwords.txt')
    4 words read

    >>> word_finder.random()
    'cat'

    >>> word_finder
    WordFinder words=cat cat dog animal

    """
    
    def __init__(self, file_path):
        "Read text file and split words into list. Count number of words"
        self.words = self.read_file(file_path)
        self.num_words = len(self.words)

        print(f"{self.num_words} words read")
    
    def __repr__(self):
        return f"WordFinder words={' '.join(self.words)}"

    def read_file(self, file_path):
        "Read text file and split into list of words."
        
        with open(file_path) as file:
            return [word for line in file for word in line.split(" ")]

    def random(self):
        "Return random word from word list of text file"
        random_word = randint(0,self.num_words - 1)

        return self.words[random_word]


class SpecialWordFinder(WordFinder):
    """
    >>> special_word_finder = SpecialWordFinder('words.txt')
    4 words read

    >>> " ".join(special_word_finder.words)
    cat cat dog animal
    """


    def read_file(self, file_path):
        """
        Reads text file, removes blank lines and lines starting with #
        Splits remaining text into list of words
        """
        
        with open(file_path) as file:
            return [word for line in file for word in line.split(" ") if line[0] != "#" and len(line.rstrip()) != 0]