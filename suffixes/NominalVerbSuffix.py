#-*- coding: cp1254 -*-

from . import Suffix

S11 = Suffix("-cAsInA",    "casına|çasına|cesine|çesine",      None, True)
S4  = Suffix("-sUnUz",     "sınız|siniz|sunuz|sünüz",          None, True)
S14 = Suffix("-(y)mUş",    "muş|miş|müş|mış",                  "y",  True)
S15 = Suffix("-(y)ken",    "ken",                              "y",  True)
S2  = Suffix("-sUn",       "sın|sin|sun|sün",                  None, True)
S5  = Suffix("-lAr",       "lar|ler",                          None, True)
S9  = Suffix("-nUz",       "nız|niz|nuz|nüz",                  None, True)
S10 = Suffix("-DUr",       "tır|tir|tur|tür|dır|dir|dur|dür",  None, True)
S3  = Suffix("-(y)Uz",     "ız|iz|uz|üz",                      "y",  True)
S1  = Suffix("-(y)Um",     "ım|im|um|üm",                      "y",  True)
S12 = Suffix("-(y)DU",     "dı|di|du|dü|tı|ti|tu|tü",          "y",  True)
S13 = Suffix("-(y)sA",     "sa|se",                            "y",  True)
S6  = Suffix("-m",         "m",                                None, True)
S7  = Suffix("-n",         "n",                                None, True)
S8  = Suffix("-k",         "k",                                None, True)

# The order of the enum definition determines the priority of the suffix.
# For example, -(y)ken (S15 suffix) is  checked before -n (S7 suffix).
VALUES = (S11,S4,S14,S15,S2,S5,S9,S10,S3,S1,S12,S13,S6,S7,S8)