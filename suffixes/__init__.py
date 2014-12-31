import re

__all__ = ["Suffix"]

class Suffix(object):
    def __init__(self, name, pattern, optionalLetter, checkHarmony):
        self.name = name
        self.pattern = re.compile("(" + pattern + ")$", re.UNICODE)

        if optionalLetter is None:
            self.optionalLetterCheck = False
            self._optionalLetterPattern = None
        else:
            self.optionalLetterCheck = True
            self._optionalLetterPattern = re.compile("(" + optionalLetter + ")$", re.UNICODE)

        self.checkHarmony = checkHarmony

    def Match(self, word):
        return self.pattern.search(word)

    def OptionalLetter(self, word):
        if self.optionalLetterCheck:
            match = self._optionalLetterPattern.search(word)
            if match:
                return match.group()

    def RemoveSuffix(self, word):
        return self.pattern.sub("", word)

    @property
    def CheckHarmony(self):
        return self.checkHarmony

