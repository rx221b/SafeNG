from lxml.html.clean import Cleaner
import requests
from bs4 import BeautifulSoup

def cleaning(dirty_html):
    cleaner = Cleaner(
                  embedded=False,
                  style=True,
                  inline_style=True,
                  scripts=True,
                  javascript=True,
                  annoying_tags=False,
                  remove_unknown_tags=False,
                  safe_attrs_only=True,
                  safe_attrs=frozenset(['img','src','color', 'href', 'title', 'class', 'name', 'id']),
                  remove_tags=('span', 'font')
            )
    return cleaner.clean_html(dirty_html)


def safesite(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    html_code = soup.prettify()
    cleanhtml = cleaning(html_code)
    return cleanhtml
    f = open("demofile2.html", "w")
    f.write(cleanhtml)
    f.close()
