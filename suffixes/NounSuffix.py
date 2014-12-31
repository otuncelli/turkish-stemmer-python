#-*- coding: utf-8 -*-

from . import Suffix

S16 = Suffix("-nDAn",     "ndan|ntan|nden|nten",      None,       True)
S7  = Suffix("-lArI",     "ları|leri",                None,       True)
S3  = Suffix("-(U)mUz",   "mız|miz|muz|müz",          "ı|i|u|ü",  True) 
S5  = Suffix("-(U)nUz",   "nız|niz|nuz|nüz",          "ı|i|u|ü",  True) 
S1  = Suffix("-lAr",      "lar|ler",                  None,       True)
S14 = Suffix("-nDA",      "nta|nte|nda|nde",          None,       True)
S15 = Suffix("-DAn",      "dan|tan|den|ten",          None,       True)
S17 = Suffix("-(y)lA",    "la|le",                    "y",        True)
S10 = Suffix("-(n)Un",    "ın|in|un|ün",              "n",        True)
S19 = Suffix("-(n)cA",    "ca|ce",                    "n",        True)
S4  = Suffix("-Un",       "ın|in|un|ün",              None,       True)
S9  = Suffix("-nU",       "nı|ni|nu|nü",              None,       True) 
S12 = Suffix("-nA",       "na|ne",                    None,       True)
S13 = Suffix("-DA",       "da|de|ta|te",              None,       True)
S18 = Suffix("-ki",       "ki",                       None,       False)
S2  = Suffix("-(U)m",     "m",                        "ı|i|u|ü",  True)
S6  = Suffix("-(s)U",     "ı|i|u|ü",                  "s",        True)
S8  = Suffix("-(y)U",     "ı|i|u|ü",                  "y",        True)
S11 = Suffix("-(y)A",     "a|e",                      "y",        True)

# The order of the enum definition determines the priority of the suffix.
# For example, -(y)ken (S15 suffix) is  checked before -n (S7 suffix).
VALUES = (S16,S7,S3,S5,S1,S14,S15,S17,S10,S19,S4,S9,S12,S13,S18,S2,S6,S8,S11)