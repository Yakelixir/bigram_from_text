#! /usr/bin/env python

"""A script to parse text files for bigrams
   maybe n-grams in the future"""

# Playing with nltk internals and writing something that is more "generic"

def nltk_parse(data):

    """Parsing with a pure nltk approach"""

    from nltk import word_tokenize, bigrams, FreqDist

    tokens = word_tokenize(data)
    bigrams = bigrams(tokens)
    fdist = FreqDist(bigrams)
    for result, cnt in fdist.items():
        print(result, ', ', cnt)

    return fdist

def bigram_parse(data):
    """Parse strings into """

    from collections import Counter
    # work needed with counter

    input_list = data.split(' ')
    bigrams = zip(input_list, input_list[1:])
    count = Counter()
    for element in bigrams:
        count[element] += 1
    print(count)

    return count

def filter_punkt(raw_data):
    """apply lower case
       filter out punctuation"""

    import string
    new_str = raw_data.lower().translate(str.maketrans('', '', string.punctuation))

    return new_str
