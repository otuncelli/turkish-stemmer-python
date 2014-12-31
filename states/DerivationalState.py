from ..suffixes import DerivationalSuffix
from ..transitions import Transition
from . import State

class DerivationalState(State):
    def __init__(self, initialState, finalState, *suffixes):
        super(DerivationalState, self).__init__(initialState, finalState, *suffixes)

    def NextState(self, suffix):
        if self.initialState:
            return B

A = DerivationalState(True, False, *DerivationalSuffix.VALUES)
B = DerivationalState(False, True)