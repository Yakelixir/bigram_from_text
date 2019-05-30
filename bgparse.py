#! /usr/bin/env python

"""A script to parse text files """

from nltk.probability import FreqDist
import Counter

#from collections import Counter
#from nltk.corpus import brown



# Generate bigrams out of the new spaced string
def load_file():
    """How we load a file for parsing"""

def ntlk_parse():

    """Paring with a pure nltk approach"""

    from nltk.tokenize import word_tokenize
    sent = 'This is an example sentence'
    fdist = FreqDist()
    for word in word_tokenize(sent):
        fdist[word.lower()] += 1
    # An equivalent way to do this is with the initializer:

    fdist = FreqDist(word.lower() for word in word_tokenize(sent))

def parse_bigrams(data, seperator=' '):
    """Parse strings into """

    #<set filter here?>

    input_list = data.split(seperator)
    return zip(input_list, input_list[1:])


if __name__ == '__main__':

    SAMPLE = 'The quick brown fox and the quick blue hare.'
    TOKEN_FREQ = FreqDist(parse_bigrams(SAMPLE))
    print(TOKEN_FREQ)
