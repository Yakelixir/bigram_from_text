#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
TESTING FOR BIGRAM FROM FILE PARSING

: DOCS : https://docs.python.org/3/library/unittest.html
"""

import os
import unittest

from bgparse import nltk_parse, filter_punkt_lower
from bigramft import read_file
from nltk import bigrams, word_tokenize

CWD_SAMPLE = os.getcwd() + '/files/sample.txt'
SAMPLE_READ = filter_punkt_lower(read_file(CWD_SAMPLE))
BIGRAMS = bigrams(word_tokenize(SAMPLE_READ))
SAMPLE_EXPECTED = {('the', 'quick'): 2,
                   ('quick', 'brown'): 1,
                   ('brown', 'fox'): 1,
                   ('fox', 'and'): 1,
                   ('and', 'the'): 1,
                   ('quick', 'blue'): 1,
                   ('blue', 'hare'): 1,
                   ('hare', 'δ'): 1,
                   ('δ', 'й'): 1,
                   ('й', 'ק'): 1,
                   ('ק', 'م'): 1,
                   ('م', '๗'): 1,
                   ('๗', 'あ'): 1,
                   ('あ', '叶'): 1,
                   ('叶', '葉'): 1,
                   ('葉', 'and'): 1,
                   ('and', '말'): 1
                   }
GEN_LIST = []
while True:
    try:
        YLD = next(BIGRAMS)
        GEN_LIST.append(YLD)
    except StopIteration:
        break

class testbigram_parse(unittest.TestCase):
    """
    Testing for bigramft.py and bgparse.py
    """

    def test_is_str(self):
        """
        test that the input is a str
        """
        self.assertIsInstance(SAMPLE_READ, str)

    def test_is_dict(self):
        """
        test that the input is a dict
        """
        self.assertIsInstance(nltk_parse(SAMPLE_READ), dict)

    def test_expected_output(self):
        """
        test to see if the nltk returned object is the same as our expect ouput from the sample
        """
        self.assertEqual(nltk_parse(SAMPLE_READ), SAMPLE_EXPECTED)

    def test_len_grams(self):
        """
        test that the number of words + 1
        that we find are equal to the number of bigrams
        """
        self.assertEqual(len(SAMPLE_READ.split(' ')) - 1, sum(SAMPLE_EXPECTED.values()))

    def test_sum_bigrams(self):
        """
        test that the total count of bigrams found equals the total count of frequencies
        this should fail as we know there are LTR marks \u200e
        """
        self.assertEqual(len(GEN_LIST), sum(SAMPLE_EXPECTED.values()))

    # def approach_delta(self):
    #     """
    #     compare the ouput of the nltk and non-nltk appraoches for funnzies and behavior notes
    #     """
    #     self.assert(nltk, non - nltk, msg=None)
    #
    #     # OR
    #     # assertDictEqual(expected, actual, msg=None)

if __name__ == '__main__':
    unittest.main()
