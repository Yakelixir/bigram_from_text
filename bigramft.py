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
import sys


def cmd_line_input():

    """command line interface for input"""

    help_msg = """
    usage: bigramft.py [-h] [-u] [-f]

    A program to update components on servers.

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


# Try running with these args
#
# "Hello" 123 --enable
if __name__ == '__main__':

    if sys.version_info < (3, 0, 0):
        sys.stderr.write("You need python 3.0 or later to run this script\n")
        sys.exit(1)

    try:
        ARGS = cmd_line_input()
        print(ARGS)
    except:
        print('Plese see the help message for usage tips')
