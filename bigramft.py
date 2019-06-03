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
    required: text files

    A program to check text from files for bigrams and count distribution.

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
                        "--files",
                        nargs='+',
                        required=True,  # required for now
                        help="""set a file target ex. 
                        -f path/file.txt path/file2.txt etc
                        You can set one or as many as you like"""
                        )
    parser.add_argument("-u",
                        "--url",
                        nargs='+',
                        help="""set a url target ex.
                        -u google.com somesite.com etc
                        You can set one or as many as you like"""
                        )

    return parser.parse_args()


def file_text(files):

    """Load a file
       Filter punctuation
       Call nltk_parse on the raw text
       How do we want to handle this for input"""

    for file in files:
        # possible split here to conncurency considerations
        # noticable behavior difference when handling

        try:
            text = open(file).read()
            print(text)
            if isinstance(file, str):
                no_punkt_text = bgparse.filter_punkt(text)
                bgparse.nltk_parse(no_punkt_text)
                bgparse.bigram_parse(no_punkt_text)
            else:
                pass
        except:
            print('something went wrong')
            pass
        # except UnicodeEncodeError as error:
        #     print(error)


if __name__ == '__main__':

    try:
        import bgparse
        import string

        ARGS = cmd_line_input()
        file_text(ARGS.files)
    except Exception as error:
        print(__name__, error, '\n', 'Plese see the help message for usage tips')
