import requests

from bs4 import BeautifulSoup

class ParseWikiLanguages:
    def __init__(self):
        self._url = 'https://wikipedia.com'
        self._allLanguages = []
        self._languages = []
    
    def _get_raw_html_page(self):
        return requests.get(self._url)
    
    def parse_html_page(self):
        page = self._get_raw_html_page()
        parsed = BeautifulSoup(page.text, 'html.parser')
        self._allLanguages = parsed.findAll('a', class_='link-box')

        for data in self._allLanguages:
            self._languages.append(data.find('strong').text)

        print(self._languages)  

if __name__== '__main__':
    ParseWikiLanguages().parse_html_page()