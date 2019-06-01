#! /usr/bin/env python

"""
!!!Run it from here!!!
ARGS
RUN SCRIPTS
1. collect text
2. make txt files and store
3. get txt file and parse
3.
"""

import argparse


def cmd_line_input():

    """command line interface for input"""

    help_msg = """
    usage: bigramft.py [-h] [-u] [-f]

    A program to check text from files for bigrams.

    optional arguments:
    ####Args#########Output#####Desc####
        -h, --help   str        show this help message and exit
        -u, --url    list       supply a single or several url(s) for requests.get() to target

        >>> -u 'google.com' 'gohealth.com' ...               

        -f, --file   list       file location that we should target     
        """

    parser = argparse.ArgumentParser(description='Comand line parse for input options',
                                     add_help=False)

    parser.add_argument('-h',
                        '--help',
                        action='help',
                        default=argparse.SUPPRESS,
                        help=help_msg
                       )
    parser.add_argument("-f",
                        "--file",
                        nargs='+',
                        help='set a file target ex. -f path/file.txt path/file2.txt etc'
                       )
    parser.add_argument("-u",
                        "--url",
                        nargs='+',
                        help='set a url target ex. -u google.com somesite.com etc'
                       )

    return parser.parse_args()


def file_text(file):
    """Load a file
       Call nltk_parse on the raw text"""

    file_output = open(file)
    text = file_output.read()
    bgparse.nltk_parse(text)

if __name__ == '__main__':

    try:
        import bgparse
        #ARGS = cmd_line_input()
        #ARGS_FILE_PATH = ARGS.file
        #print(ARGS)

        FPATH = '/Users/truth/PycharmProjects/Bigram_from_text/bigram_from_text/files/sample.txt'
        SAMPLE = 'The quick brown fox and the quick blue hare.'
        file_text(FPATH)
        bgparse.nltk_parse(SAMPLE)
        bgparse.bigram_parse(SAMPLE)
        file_text(FPATH)
        #file_text(ARGS_FILE_PATH)
    except Exception as error:
        print(error, '\n', 'Plese see the help message for usage tips')
