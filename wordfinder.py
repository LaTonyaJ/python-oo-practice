"""Word Finder: finds random words from a dictionary."""
import random


class WordFinder:
    def __init__(self, path):
        f = open(path)
        self.words = self.parse(f)
        print(f"{len(self.words)} words read")

    def parse(self, f):
        """Turn the file contents into a List"""
        return[w.strip() for w in f]

    def random(self, f):
        """Select random words"""
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    def parse(self, f):
        return[w.strip() for w in f
               if w.strip() and not w.startswith('#')]
