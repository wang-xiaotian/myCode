#!/usr/bin/python3
""" RZFeeser | Alta3 Research
Learning to scrape webdata with BeautifulSoup
"""

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from bs4 import element

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            # stream=True means Requests cannot release the connection until closed
            # closing() will close "resp" at the end of this block
            if is_good_response(resp):
                return resp.content
                # .content() reads the HTML of the Requests object
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def readFlowers(url):
    raw_html = simple_get(url)
    html = BeautifulSoup(raw_html, 'html.parser')
    flowers = {}
    for h3 in html.select("h3"):
        if(not h3.is_empty_element):
            id = h3.get('id')
            if(not id == None):
                flowers[h3.text] = h3.next.next.next.text
    return flowers


def main():
    print(len(readFlowers('https://florgeous.com/types-of-flowers/')))
        

if __name__ == "__main__":
    main()
