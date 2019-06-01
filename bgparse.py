#! /usr/bin/env python

"""A script to parse text files for bigrams
   maybe n-grams in the future"""

# Playing with nltk internals and writing something that is more "generic"

def ntlk_parse(data):

    """Parsing with a pure nltk approach"""

    from nltk import word_tokenize, bigrams, FreqDist

    tokens = word_tokenize(data.lower())
    print(tokens)
    bigrams = bigrams(tokens)
    fdist = FreqDist(bigrams)
    print(fdist.items)
    for wrd, cnt in fdist.items():
        print(wrd, ', ', cnt)

    return fdist

def bigram_parse(data):
    """Parse strings into """

    from collections import Counter
    # work needed with counter

    input_list = data.split(' ')
    bigrams = zip(input_list, input_list[1:])
    print(bigrams)
