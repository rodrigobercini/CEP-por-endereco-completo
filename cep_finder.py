from bs4 import BeautifulSoup
import requests

################################################
#####
# Scrapes CEP by address from Correios Official Website, blocks scraping after ~300 requests
# No special characters allowed
# Example: cep_finder('Av Protasio Alves', '199', 'RS', 'Porto Alegre')
#####
################################################

def cep_finder(address, number, city, uf):     
    try:     
        data = {
            'UF': uf,
            'Localidade': city,
            'Tipo': '',
            'Logradouro': address,
            'Numero': number
        }
        url = "http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCep.cfm"
        response = requests.post(url, data=data)
        doc = BeautifulSoup(response.text, 'html.parser')
        tags = doc.find_all('td') # Finds all 'td' tags
        cep = tags[3].text # Extract text of the third tag, where the CEP is located
        if cep[5] == '-': # Error handler
            return cep
        else:
            return 'Error'
    except:
        return 'Error'


################################################
##### Alternative to cep_finder()
# Scrapes CEP by address using www.mapacep.com.br, limited to a few CEPs (not sure about the exact limit)
# Example: cep_finder_mapacep('Av Protasio Alves', '199','Porto Alegre' , 'RS')
# Output: 
#####
################################################


def cep_finder_mapacep(address,number,city,uf):    
    try:
        complete_address = ' '.join([address, str(number), city, uf])
        data = {
            'keywords': complete_address,
            'submit': 'pesquisar'
        }
        url = "https://www.mapacep.com.br/"
        response = requests.post(url, data=data)
        doc = BeautifulSoup(response.text, 'html.parser')
        docx = doc.find_all('p')
        docx_string = str(docx[2]) # Select the second <p> tag, where the CEP is located
        lens = len(docx_string)
        cep = docx_string[(lens-21):(lens-12)] # Get the CEP through reverse slicing
        if cep[5] == '-': # Error handler
            return cep
        elif:
        else:
            return 'Erro'
    except:
        return 'Erro'
