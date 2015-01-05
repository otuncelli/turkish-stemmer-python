from ..transitions import Transition
from ..suffixes import *

__all__ = ["State"]

class State(object):
    def __init__(self, initialState, finalState, *suffixes):
        self.initialState = initialState
        self.finalState = finalState
        if suffixes is None:
            self.suffixes = ()
        else:
            self.suffixes = suffixes

    def AddTransitions(self, word, transitions, marked):
        for suffix in self.suffixes:
            if suffix.Match(word):
                transitions.append(Transition(self, self.NextState(suffix), word, suffix, marked))

    def NextState(self, suffix):
        raise NotImplementedError("Feature is not implemented.")