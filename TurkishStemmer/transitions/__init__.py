__all__ = ["Transition"]

class Transition(object):
    def __init__(self, startState, nextState, word, suffix, marked):
        self.startState = startState
        self.nextState = nextState
        self.word = word
        self.suffix = suffix
        self.marked = False

    def similarTransitions(self, transitions):
        for transition in transitions:
            if (self.startState == transition.startState and 
                self.nextState == transition.nextState):
                yield transition