#! /usr/bin/env python

"""
A script to parse text files for bigrams
probably n-grams in the future
"""

# Playing with nltk internals and writing something that is more "generic"

def nltk_parse(data):

    """
    Parsing with a pure nltk approach
    """

    from nltk import word_tokenize, bigrams, FreqDist


    tokens = word_tokenize(data)
    bigrams = bigrams(tokens)
    fdist = FreqDist(bigrams)
    for result, cnt in fdist.items():
        print(result, cnt)

    return fdist

def bigram_parse(data):

    """
    Parse strings into bigrams without nltk
    """

    from collections import Counter

    input_list = data.split(' ')
    bigrams = zip(input_list, input_list[1:])
    count = Counter()
    for element in bigrams:
        count[element] += 1
    print(count)

    return count

def filter_punkt(raw_data):

    """
    apply lower case
    filter out punctuation
    # str vs unicode consideration for translate() behavior
    # python3.6 consideration for using regex here...
    """

    import string
    lower_str = raw_data.lower()

    # The third argument is a string, whose characters will
    # be mapped to None in the result
    new_str = lower_str.translate(str.maketrans('', '', string.punctuation))

    return new_str
