#! /usr/bin/env python

"""A script to parse text files """

# Generate bigrams out of the new spaced string
def file_text(file):
    """Load a file and return the raw text"""

    f = open(file)
    text = f.read()
    return text

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

def parse_bigrams(data, seperator=' '):
    """Parse strings into """

    from collections import Counter

    input_list = data.split(seperator)
    bigrams = zip(input_list, input_list[1:])
    print(bigrams)


if __name__ == '__main__':

    SAMPLE = 'The quick brown fox and the quick blue hare.'
    ntlk_parse(SAMPLE)
    parse_bigrams(SAMPLE)
