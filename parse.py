# import needs bibles / modules
import requests
import csv

from datetime import datetime
from bs4 import BeautifulSoup


class ParseCosts:
    def __init__(self):
        self._url = 'https://www.google.com/finance/quote/USD-EUR'
        self._now = datetime.now()
        self._names = []
        self._costs = []
        self._current_names = []
        self._current_costs = []

    def _get_connection(self):
        '''get raw html page'''
        return requests.get(self._url)
    
    def _get_html_code(self):
        '''get html code'''
        _req = self._get_connection()
        return BeautifulSoup(_req.text, 'html.parser')      

    def _get_current_name(self):
        '''get current name for .csv file'''
        return f'{self._now.strftime("%Y")}-{self._now.strftime("%m")}-{self._now.strftime("%d")}'

    def _get_and_return_any_prises(self):
        '''take html code, parse it and writing in lists '''
        parsed = self._get_html_code()
        find_files = parsed.findAll('div', class_='VKMjFc')

        #in this i take names
        for data in find_files:
            self._names.append(data.find('div','pKBk1e').text)

        #in this i take prices
        for data in find_files:
            self._costs.append(data.find('div', 'YMlKec').text)

        #delete repeats
        for cnt in range(0, len(self._names)):
            if cnt % 2 != 0:
                self._current_names.append(self._names[cnt])
                self._current_costs.append(self._costs[cnt])    

    def create_and_write_current_costs(self):
        '''writing prisec in .csv file'''
        _ = self._get_and_return_any_prises()
        name = self._get_current_name()

        with open(f'{name}.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows([self._current_names, self._current_costs])

if __name__ == '__main__':
    ParseCosts().create_and_write_current_costs()