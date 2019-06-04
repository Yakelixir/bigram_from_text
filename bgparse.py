#! /usr/bin/env python

"""
A script to parse text files for bigrams
probably n-grams in the future
"""

# Playing with nltk internals and writing something that is more "generic"

def nltk_parse(data):

    """
    Parsing with a pure nltk approach
    :str required:
    """

    from nltk import bigrams, word_tokenize, FreqDist

    return FreqDist(bigrams(word_tokenize(data)))

def bigram_parse(data):

    """
    Parse strings into bigrams without nltk
    :str required:
    """

    from collections import Counter

    count = Counter()

    input_list = data.split(' ')
    zip_bigrams = zip(input_list, input_list[1:])
    for element in zip_bigrams:
        count[element] += 1

    return count

def filter_punkt_lower(raw_data):

    """
    apply lower case
    filter out punctuation
    # str vs unicode consideration for translate() behavior
    # python3.6 consideration for using regex here...

    special consideration for \u200e a LTR mark...
    example and considerations from...
    https://stackoverflow.com/questions/47861089/correct-length-of-a-string-of-non-english-characters-in-python3

    >> x = 'צוֹר'
    >> x
    'צוֹר\u200e' # note the control character escape sequence
    >> print(len(x))
    5
    >> print(len(x.replace('\u200e', ''))
    4

    : maketrans()
    The third argument is a string, whose characters will
    # be mapped to None in the result

    ### Consideration to replace this with
    >> ''.join(c for c in x if unicodedata.category(c) not in ['Mn', 'Cf'])
    import consideration needed for unicodedata
    """

    import string
    lower_str = raw_data.lower()
    special_char = '\u200e'
    punct = string.punctuation
    new_str = lower_str.translate(str.maketrans('', '', punct)).replace(special_char, '')

    return new_str
