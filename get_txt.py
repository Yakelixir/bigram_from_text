#! /usr/bin/env python

"""A module to reach out to sites to gather data and make text files"""

import requests
from bs4 import BeautifulSoup

# idea for a file handler like a han

def file_handler():
    """handle files"""

def results_handler():
    """handle results"""

def start(url):
    """Lets reach out to some sites to see what language there is out there for us
    GET """

    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, "html.parser")
    for headline_text in soup.findAll('a', {'class': 'hdrlnk'}):
        content = headline_text.string
