from lxml.html.clean import Cleaner
import requests
from bs4 import BeautifulSoup

def cleaning_low(dirty_html):
    cleaner = Cleaner(
                  embedded=False,
                  style=False,
                  inline_style=False,
                  scripts=False,
                  javascript=False,
                  annoying_tags=False,
                  remove_unknown_tags=False,
                  safe_attrs_only=True,
                  safe_attrs=frozenset(['img','src','color', 'href', 'title', 'class', 'name', 'id']),
                  remove_tags=('span', 'font')
            )
    return cleaner.clean_html(dirty_html)

def cleaning_medium(dirty_html):
    cleaner = Cleaner(
                  embedded=False,
                  style=False,
                  inline_style=False,
                  scripts=True,
                  javascript=True,
                  annoying_tags=True,
                  remove_unknown_tags=False,
                  safe_attrs_only=True,
                  safe_attrs=frozenset(['img','src','color', 'href', 'title', 'class', 'name', 'id']),
                  remove_tags=('span', 'font')
            )
    return cleaner.clean_html(dirty_html)

def cleaning_high(dirty_html):
    cleaner = Cleaner(
                  embedded=True,
                  style=True,
                  inline_style=True,
                  scripts=True,
                  javascript=True,
                  annoying_tags=True,
                  remove_unknown_tags=True,
                  safe_attrs_only=False,
                  safe_attrs=frozenset(['img','src','color', 'href', 'title', 'class', 'name', 'id']),
                  remove_tags=('span', 'font')
            )
    return cleaner.clean_html(dirty_html)


def safesite(url,value):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    html_code = soup.prettify()
    if(value=="low"):
        cleanhtml = cleaning_low(html_code)
    
    elif(value=="med"):
        cleanhtml = cleaning_medium(html_code)
    
    elif(value=="high"):
        cleanhtml = cleaning_high(html_code)

    return cleanhtml
