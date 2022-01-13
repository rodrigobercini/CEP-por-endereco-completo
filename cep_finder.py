import re
import requests
from bs4 import BeautifulSoup
from unicodedata import normalize


class CepFinder:
    def __init__(self, address, number, city, uf, verbose=False):
        self.address = address
        self.number = number
        self.city = city
        self.uf = uf
        self.verbose = verbose

    def _generate_json_data(self) -> dict:
        '''
        Generate the json data to be sent to the Correios website.
        '''
        return {
            'UF': self.uf,
            'Localidade': self._replace_diacritics(self.city),
            'Tipo': '',
            'Logradouro': self._replace_diacritics(self.address),
            'Numero': self.number
        }

    def _generate_complete_address_string(self) -> str:
        '''
        Generate the complete address string to be sent to Mapacep website.
        '''
        return f'{self.address} {self.number} {self.city} {self.uf}'

    def _replace_diacritics(string) -> str:
        '''
        Replace a character with a diacritic with the same character without diacritic.
        Input: 'Álvaro'
        Output: 'Alvaro'
        '''
        return normalize('NFKD', string).encode('ASCII', 'ignore').decode('ASCII')
    
    def _validate_cep(self, cep, doc):
        if re.match('^\d{5}-\d{3}$', cep):
            return cep
        elif self.verbose:
            print('Error while scraping the request')
            return None
        else:
            return None

    def find_cep_mapacep(self) -> str:
        '''
        Get the CEP of an address using www.mapacep.com.br, limited to a few CEPs (not sure about the exact limit).
        '''
        data = {
            'keywords': self._generate_complete_address_string(),
            'submit': 'pesquisar'
        }
        url = "https://www.mapacep.com.br/"
        response = requests.post(url, data=data)
        doc = BeautifulSoup(response.text, 'html.parser')
        docx = doc.find_all('p')
        docx_string = str(docx[2]) # Select the second <p> tag, where the CEP is located
        lens = len(docx_string) 
        cep = docx_string[(lens-21):(lens-12)] # Get the CEP through reverse slicing
        
        return self._validate_cep(cep, doc)

    def find_cep_correios_website(self) -> str:
        '''
        Deprecated as the original endpoint was shutdown by Correios.
        Scrapes CEP by address from the Correios Official Website. The website blocks scraping after ~300 requests
        '''  
        data = self._generate_json_data()
        url = "http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCep.cfm"
        response = requests.post(url, data=data)
        doc = BeautifulSoup(response.text, 'html.parser')
        tags = doc.find_all('td')
        cep = tags[3].text

        return self._validate_cep(cep, doc)
