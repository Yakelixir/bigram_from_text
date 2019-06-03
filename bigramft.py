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

    """
    command line interface for input
    """

    help_msg = """
    usage: bigramft.py [-h] [-u] [-f]
    required: text files

    A program to check text from files for bigrams and count distribution.

    optional arguments:
    ::::Args:::::::::Output:::::Desc::::
    
        -h, --help   str        show this help message and exit
        -u, --url    list       supply a single or several url(s) for requests.get() to target

        >>> -u 'google.com' 'gohealth.com' ...
        
    required arguments:
    ::::Args:::::::::Output:::::Desc::::

        -f, --file   list       file location that we should target
               """

    parser = argparse.ArgumentParser(description='Comand line parse for input options',
                                     add_help=False)

    parser.add_argument('-h',
                        '--help',
                        action='help',
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


def file_to_grams(files):

    """
    Load a file
    Filter punctuation
    Call nltk_parse on the raw text
    How do we want to handle this for input
    """

    for file in files:
        # possible split here to conncurency considerations (FUTURE)
        # noticable behavior difference when handling LTR (INVESTIGATING)

        try:
            text = open(file).read()
            if isinstance(text, str):
                no_punct_text = bgparse.filter_punkt(text)
                nice_print(bgparse.nltk_parse(no_punct_text))
                nice_print(bgparse.bigram_parse(no_punct_text))
            else:
                pass
        except Exception as error:
            print('something went wrong reading your file', end='')
            print(error)
            pass
        # except UnicodeEncodeError as error:
        #     print(error)

def nice_print(results):

    """
    print it nice and neat

    :dict required:

    structure:
    <word> <word>, freq
    """

    for result, freq in results.items():
        print(f'"{result[0]} {result[1]}", {freq}')
    print()


if __name__ == '__main__':

    try:
        import bgparse

        ARGS = cmd_line_input()
        file_to_grams(ARGS.files)
    except Exception as error:
        print(__name__, error, '\n', 'Plese see the help message for usage tips')
