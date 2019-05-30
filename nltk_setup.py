#! /usr/bin/env python

"""run and initiate nltk.download('all') """

import nltk

# setup or argparse

PERMISSION = input("Would you like to continue and install all nltk dependanies? [Y/n] ")

if PERMISSION == 'Y':
    try:
        nltk.download('all')
        COMPLETE = """We have completed the initial setup for ntlk download.
        You can now run bigramft.py"""
        print('\n', COMPLETE, '\n')
    except Exception as error:
        print('There was an error: ', error)
else:
    EXIT_MSG = """No worries we can have some bigram fun later when your ready to setup.
    Never rush quality!"""
    print(EXIT_MSG)
