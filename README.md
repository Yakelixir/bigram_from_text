# bigram_from_text
An app that will take any text file and find bigrams

INSTALL

1. chmod +x install.sh

Set up permissions to install.

2. ./install.sh

This will check for python3, setup a virtualenv, and install dependancies through pip. This will then run bigram_setup.py

3. source $PWD/nltk_vrtenv/bin/activate or source <path>/nltk_vrtenv/bin/activate

Actiavte the virtual environment

4. ./nltk_setup.py

This will run nltk.download('all') which is recomended for setup
You should be ready for beer and pixie sticks now



RUNNING

1. python3 bigramft.py -f <file_path>

Argparse ineraction [-f required]



TESTING

1. python test_bigramft.py

unittests from $PWD/test_bigramft.py



DEVELOPMENT NOTES

    """
    
    usage: bigramft.py [-h] [-u] [-f]
    required: text files

    A program to check text from files for bigrams and count distribution.

    optional arguments:
    ::::Args:::::::::Output:::::Desc::::
    we                  a
        -h, --help   str        show this help message and exit
        -u, --url    list       supply a single or several url(s) for requests.get() to target

        >>> -u 'google.com' 'gohealth.com' ...
        
    required arguments:
    ::::Args:::::::::Output:::::Desc::::

        -f, --file   list       file location that we should target
    
   
   
   
    
    Notes for Development:
    Get this stable in MVP form                             [done]
    * Something to collect text and make files              [fut]
    * Argparse for CLI                                      [done]
        * File location required
    * A place to store data                                 [fut]
    ** How do we want to store this?
    * Parsing                                               [done]
    ** USE NLTK internal vs regex!!
    ** Corpus ->
    ** Entry ->
    ** Page ->
    ** Paragraph ->
    ** Sentence ->
    ** Word ->
    * Histogram output                                      [done]
    * Conncurrency of Requests -> Factory Processing Line     [    ]
    * Generator usage for processing line / croutines         [    ]
    * Parsing seperator in args                               [    ]
    """