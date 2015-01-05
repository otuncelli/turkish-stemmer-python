from ..suffixes import NominalVerbSuffix
from ..transitions import Transition
from . import State

TF_VALUES, FT_VALUES, FF_VALUES = dict(), dict(), dict()

class NominalVerbState(State):
    def __init__(self, initialState, finalState, *suffixes):
        super(NominalVerbState, self).__init__(initialState, finalState, *suffixes)

        if self.initialState and (not self.finalState):
            self.VALUES = TF_VALUES
        elif (not self.initialState) and self.finalState:
            self.VALUES = FT_VALUES
        else:
            self.VALUES = FF_VALUES

    def NextState(self, suffix):
        return self.VALUES[suffix]

A = NominalVerbState(True, False, *NominalVerbSuffix.VALUES)
B = NominalVerbState(False, True, NominalVerbSuffix.S14)
C = NominalVerbState(False, True, NominalVerbSuffix.S10, NominalVerbSuffix.S12, NominalVerbSuffix.S13,NominalVerbSuffix.S14)
D = NominalVerbState(False, False, NominalVerbSuffix.S12,NominalVerbSuffix.S13)
E = NominalVerbState(False, True, NominalVerbSuffix.S1,NominalVerbSuffix.S2,NominalVerbSuffix.S3,NominalVerbSuffix.S4,NominalVerbSuffix.S5,NominalVerbSuffix.S14)
F = NominalVerbState(False, True)
G = NominalVerbState(False, False, NominalVerbSuffix.S14)
H = NominalVerbState(False, False, NominalVerbSuffix.S1,NominalVerbSuffix.S2,NominalVerbSuffix.S3,NominalVerbSuffix.S4,NominalVerbSuffix.S5,NominalVerbSuffix.S14)

ALL = (A,B,C,D,E,F,G,H)

for sfx in (NominalVerbSuffix.S1,NominalVerbSuffix.S2,NominalVerbSuffix.S3,NominalVerbSuffix.S4):
    TF_VALUES[sfx] = B

TF_VALUES[NominalVerbSuffix.S5] = C

for sfx in (NominalVerbSuffix.S6,NominalVerbSuffix.S7,NominalVerbSuffix.S8,NominalVerbSuffix.S9):
    TF_VALUES[sfx] = D

TF_VALUES[NominalVerbSuffix.S10] = E

for sfx in (NominalVerbSuffix.S12,NominalVerbSuffix.S13,NominalVerbSuffix.S14,NominalVerbSuffix.S15):
    TF_VALUES[sfx] = F

TF_VALUES[NominalVerbSuffix.S11] = H

for sfx in (NominalVerbSuffix.S1,NominalVerbSuffix.S2,NominalVerbSuffix.S3,NominalVerbSuffix.S4,NominalVerbSuffix.S5):
    FT_VALUES[sfx] = G

for sfx in (NominalVerbSuffix.S10,NominalVerbSuffix.S12,NominalVerbSuffix.S13,NominalVerbSuffix.S14):
    FT_VALUES[sfx] = F

for sfx in (NominalVerbSuffix.S1,NominalVerbSuffix.S2,NominalVerbSuffix.S3,NominalVerbSuffix.S4,NominalVerbSuffix.S5):
    FF_VALUES[sfx] = G

for sfx in (NominalVerbSuffix.S12,NominalVerbSuffix.S13,NominalVerbSuffix.S14):
    FF_VALUES[sfx] = F