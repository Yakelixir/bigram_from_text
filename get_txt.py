#! /usr/bin/env python

"""
A module to reach out to sites to gather data to make text files
Options: Scrape or request
"""

def start_scrape(url):
    """
    Lets reach out to some sites to see what language there is out there for us
    GET
    """

    import requests
    from bs4 import BeautifulSoup

    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    for headline_text in soup.findAll('a', {'class': 'hdrlnk'}):
        content = headline_text.string

def start_req_get(url, payload=''):
    """

    :param payload:
    :return:
    """

    import requests
    import json
    response = requests.get(url, {'payload': payload})
    print(f'{url} STATUS CODE: {response.status_code}')
    resp = response.content.decode('utf8')
    data = json.loads(resp)
    print(data['args'])


if __name__ == '__main__':


    # future work to make this dynamic maybe...
    # maybe a get for all entries
    # load the results of all ids

    # static test code for scraping and requests
    URL_ROOT = 'http://www.omdbapi.com/'
    ENTRY_ID = 'tt3896198'
    KEY = '51a59419'
    URL = f'{URL_ROOT}?i={ENTRY_ID}&apikey={KEY}'

    start_scrape(URL)
