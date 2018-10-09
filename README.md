# Turkish Stemmer for Python

Note : Most of the documentation taken from [elasticsearch-analysis-turkishstemmer](https://github.com/skroutz/elasticsearch-analysis-turkishstemmer) project. 

Stemmer algorithm for Turkish language.

## Introduction to Turkish language morphology

> Turkish is an agglutinative language and has a very rich morphological
  stucture. In Turkish, you can form many different words from a single stem by
  appending a sequence of suffixes. For example The word "doktoruymuşsunuz"
  means "You had been the doctor of him". The stem of the word is "doktor" and
  it takes three different suffixes -sU, -ymUş, and -sUnUz.

From "Snowball Description":

> Words are usually composed of a stem and of at least two or three affixes
  appended to it.

> We can analyze noun suffixes in Turkish in two groups. Noun suffixes (eg.
  "doktor-um" meaning "my doctor") and nominal verb suffixes (eg. "doktor-dur"
  meaning ‘is a doctor’). The words ending with nominal verb suffixes can be
  used as verbs in sentences. There are over thirty different suffixes
  classified in these two general groups of suffixes.

> In Turkish, the suffixes are affixed to the stem according to definite
  ordering rules.

From "An affix stripping morphological analyzer for Turkish" paper:

> Turkish has a special place within the natural languages not only being a
  fully concatenative language but also having the suffixes as the only affix
  type. Another feature of the language is that, someone who knows Turkish can
  easily analyze a word even if he/she does not know its stem.

> The phonological rules of Turkish are significant factors that influence
  this feature.
  Ex: (any word)lerim => (any word)-ler-im
  "ler" plural suffix, "im" 1st singular person possessive.

### Rules

1. The only affix type in Turkish is the suffix.

2. A plural suffix cannot follow a possesive suffix.

3. A suffix in Turkish can have multiple allomorphs in order to provide sound
   harmony in the word to which it is affixed.

4. In Turkish each vowel indicates a distinct syllable.

5. In Turkish, single syllable words are mostly the stem itself

6. If a word has nominal __verb__ suffixes, they always appear at the end of
   the word. They follow __noun__ suffixes or the stem itself at the absence
   of noun suffixes

7. In Turkish, “-lAr” suffix can be used both as a nominal verb suffix (third
   person plural present tense) and as a noun suffix (plural inflection).

8. In Turkish, words do not end with consonants 'b', 'c', 'd', and 'ğ'.
   However, when a suffix starting with a vowel is affixed to a word ending
   with 'p', 'ç', 't' or 'k', the last consonant is transformed into 'b', 'c',
   'd', or 'ğ' respectively. The postlude routine transforms last consonants
   'b', 'c','d', or 'ğ'' back to 'p', 'ç', 't' or 'k', respectively, after
   stemming is complete.

### Suffix Classes

Class                        | Type
-----------------------------|----------------
Nominal verb suffixes        | Inflectional
Derivational suffixes        | Derivational
Noun suffixes                | Inflectional
Tense & person verb suffixes | Inflectional
Verb suffixes                | Inflectional

### Suffix allomorphs

Suffix allomorphs are used to create a good sound harmony. They do not change
the meaning of the word. If a suffix has a capital letter then it has an
allomorh. If a suffix has a letter in parentheses then it can be omitted.
Possible allomorphs are given below:

Letter | Allomorph
-------|------------
U      | ı,i,u,ü
C      | c,ç
A      | a,e
D      | d,t
I      | ı,I

### Nominal Verb Suffixes

a/a | Suffix
----|------------------
1   | –(y)Um
2   | –sUn
3   | –(y)Uz
4   | –sUnUz
5   | –lAr
6   | –md
7   | –n
8   | –k
9   | –nUz
10  | –DUr
11  | –cAsInA
12  | –(y)DU
13  | –(y)sA
14  | –(y)mUş
15  | –(y)ken

Suffix transition ordering for nominal verbs can be seen in References[5]

### Noun Suffixes

a/a | Suffixes
----|-------------
1   | –lAr
2   | –(U)m
3   | –(U)mUz
4   | –(U)n
5   | –(U)nUz
6   | –(s)U
7   | –lArI
8   | –(y)U
9   | –nU
10  | –(n)Un
11  | –(y)A
12  | –nA
13  | –DA
14  | –nDA
15  | –DAn
16  | –nDAn
17  | –(y)lA
18  | –ki
19  | –(n)cA

Suffix transition ordering for nouns can be seen in References[5]

### Derivational Suffixes

a/a | Suffixes
----|----------
1   | –lUk
2   | –CU
3   | –CUk
4   | –lAş
5   | –lA
6   | –lAn
7   | –CA
8   | –lU
9   | –sUz

Initially, we will handle only a small subset of the above suffixes which are
more common in our domain.

### Vowel Harmony

This routine checks whether __the last two__ vowels of the word obey vowel
harmony rules. A brief description of Turkish vowel harmony follows.

Turkish vowel harmony is a two dimensional vowel harmony system, where vowels
are characterised by two features named frontness and roundness. There are
vowel harmony rules for each feature.

1. Vowel harmony rule for frontness: Vowels in Turkish are grouped into two
   according to where they are produced. Front produced vowels are formed at
   the front of the mouth ('e', 'i', 'ö', 'ü') and back produced vowels are
   produced nearer to throat ('a', 'ı', 'o', 'u'). According to the vowel
   harmony rule, words cannot contain both front and back vowels. This is one
   of the reasons why suffixes containing vowels can take different forms to
   obey vowel harmony.

2. Vowel harmony rule for roundness: Vowels in Turkish are grouped into two
   according to whether lips are rounded while producing it. 'o', 'ö', 'u' and
   'ü' are rounded vowels whereas 'a', 'e', 'ı' and 'i' are unrounded.
   According to the vowel harmony rules, if the vowel of a syllable is
   unrounded, the following vowel is unrounded as well. If the vowel of a
   syllable is rounded, the following vowels are 'a', 'e', 'u' or 'ü'.

### Last consonant

Another interesting case in detecting suffixes in Turkish is that, for some
suffixes, if the word ends with a vowel, a consonant is inserted between the
rest of the word and the suffix. These merging consonants can be 'y', 'n' or
's'. When a merging consonant can be inserted before the suffix, the
representation of the suffix starts with the optional consonant surrounded by
paranthesis (eg. –(y)Um, -(n)cA). For these kinds of suffixes, if existence of
a merging consonant is considered, the candidate stem is checked whether it
ends with a vowel.

If there is no 'y' consonant before the suffix, only the real part of the
suffix (eg. -Um) is marked for stemming. If there is a 'y' consonant and it is
preceded by a vowel, 'y' is treated as a merging consonant and both 'y' and
the candidate suffix (eg. -Um) is marked for stemming. If there is a consonant
just before 'y', the decision is that the consonant 'y' and the candidate
suffix are really a part of the stem. In such a case, cursor is not advanced
to prevent over-stemming. The last case can occur especially when the stem
originates from another language like in 'lityum' (meaning the element
Lithium). If the check for vowel harmony was not made, the word would be
stemmed to 'lit', for '–(y)Um' would be treated as a suffix affixed to it. But
according to morphological rules of Turkish, the final word would be 'litim',
not 'lityum' if 'lit' were really the stem of the word and the suffix '–(y)Um'
were affixed to it. So detecting 'lit' as the stem of the word would be an over
-stemming.

### Merging Vowel

Similar to merging consonants, there are merging vowels for some suffixes
starting with consonants. They can be preceded by merging vowels like in '-(U)
mUz' suffix when they are affixed to a stem ending with a consonant. In such a
case, a U vowel ('ı', 'i', 'u' or 'ü' depending on vowel harmony) is inserted
between the stem and real suffix (e.g. '-mUz') for ease of pronunciation.

### Some examples

Word / Analysis                | Meaning / Stem
------------------------------ |--------------------------------
Kalelerimizdekilerden          | From the ones at one of our castles
Kale-lAr-UmUz-DA-ki-lAr-DAn    | Kale
Çocuğuymuşumcasına             | As if I were her child
Çocuk-(s)U-(y)mUş-(y)Um-cAsInA | Çocuk
Kedileriyle                    | With their cats
Kedi-lAr-(s)U-(y)lA            | Kedi
Çocuklarımmış                  | Someone told me that they were my children
çocuk-lAr-(U)m-(y)mUş          | Çocuk
Kitabımızdı                    | It was our book
kitap-UmUz-(y)DU               | Kitap

## Future Work

* Add more verbs suffixes.
* Add more derivational suffixes.

## References

1. [Turkish Stemmer used in Lucene](http://snowball.tartarus.org/algorithms/turkish/stemmer.html)
2. [Java Implementation](http://snowball.tartarus.org/archives/snowball-discuss/att-0875/02-TurkishStemmer.java)
3. [Snowball Implementation](http://snowball.tartarus.org/algorithms/turkish/stem_Unicode.sbl)
4. [Snowball Description](http://snowball.tartarus.org/algorithms/turkish/accompanying_paper.doc)
5. [An affix stripping morphological analyzer for Turkish](http://web.itu.edu.tr/~gulsenc/papers/iasted.pdf)
6. [Lead Generation](https://en.wikipedia.org/wiki/Lead_generation)
7. [Vowel Harmony](https://en.wikipedia.org/wiki/Vowel_harmony#Turkish)
8. [Turkish Suffixes](https://en.wiktionary.org/wiki/Appendix:Turkish_suffixes)
9. [Turkish Grammar](https://en.wikipedia.org/wiki/Turkish_grammar)
10. [Turkish Language](https://en.wikipedia.org/wiki/Turkish_language)
11. [Tartarus](http://tartarus.org/)
12. [Information Retrieval on Turkish Texts](http://www.users.muohio.edu/canf/papers/JASIST2008offPrint.pdf)

## Installation

```
pip install TurkishStemmer
```
or
```
python setup.py install
```
or

Copy the module folder inside PythonXX/Lib/site-packages or inside your application directory.

## Usage
```python
>>> from TurkishStemmer import TurkishStemmer
>>> stemmer = TurkishStemmer()
>>> stemmer.stem("okuldakilerden")
okul
```

## Contributing

1. Fork it ( `https://github.com/<my-github-username>/turkish-stemmer-python/fork` )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## License

turkish-stemmer-python is licensed under the Apache Software License, Version 2.0.
