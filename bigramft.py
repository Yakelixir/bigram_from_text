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

    parser.add_argument("-h",
                        "--help",
                        action="help",
                        help=help_msg
                        )
    parser.add_argument("-f",
                        "--file",
                        dest="file",
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
    # parser.add_argument("-t",
    #                     "--test",
    #                     action='store_true',
    #                     help='include this flag to run testing with -f <path>'
    #                     )

    return parser.parse_args()


def read_file(file):

    """
    Load a file
    How do we want to handle this for input?
    # This should be turned into a generator [Future]
    """

    return open(file).read()
    # except UnicodeEncodeError as error:
    #     print(error)

def nice_print(results):

    """
    Put the pick in there, Pete, and turn it round real neat.
    Presentation is everything...

    :dict required:

    structure:
    <word> <word>, freq
    """

    for result, freq in results.items():
        print(f'"{result[0]} {result[1]}", {freq}')
    print()


if __name__ == '__main__':

    import argparse
    import bgparse
    import logging
    import os

    LOG_FILE = ''.join([os.getcwd(), 'bigramft.log'])
    LOGGER = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG,
                        filename=LOG_FILE,
                        filemode='w',  # over write for single use currently default is append
                        format='%(asctime)s : %(name)s - %(levelname)s - %(message)s')
    logging.warning('This will get logged to a file')

    try:

        ARGS = cmd_line_input()
        TEXT = read_file(ARGS.file)

        NO_PUNCT = bgparse.filter_punkt_lower(TEXT)
        NLTK_RETURN = bgparse.nltk_parse(NO_PUNCT)
        NON_NLTK_RETURN = bgparse.bigram_parse(NO_PUNCT)

        nice_print(NLTK_RETURN)
        nice_print(NON_NLTK_RETURN)

    except Exception as error:
        LOGGER.exception(error)
        print(f'{error} : Plese see the help message for usage tips or check the log')
