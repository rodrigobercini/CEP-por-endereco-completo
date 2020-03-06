from bs4 import BeautifulSoup
import requests

################################################
#####
# Retorna CEPs a partir de endereços completos do site Oficial dos Correios
# Após 300~ CEPs, a extração é bloqueada temporariamente
# Caracteres especiais não são suportados
# Examplo: cep_finder('Av Protasio Alves', '199', 'RS', 'Porto Alegre')
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
        tags = doc.find_all('td') # Encontra todas as tags 'td'
        cep = tags[3].text # Extrai o texto da terceira tag, onde se encontra o CEP
        if cep[5] == '-': # Gerenciando erros
            return cep
        else:
            return 'Erro'
    except:
        return 'Erro'


################################################
##### Alternativa ao cep_finder()
# Retorna CEPs a partir de endereços completos do site MapaCep. Também há um limite para extração
# Example: cep_finder_mapacep('Av Protasio Alves', '199','Porto Alegre' , 'RS')
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
        docx_string = str(docx[2]) # Seleciona a segunda tag 'p', onde se encontra o CEP
        lens = len(docx_string) # Prepara variável para slicing
        cep = docx_string[(lens-21):(lens-12)] # Extrai o CEP através de slicing reverso
        if cep[5] == '-': # Gerenciando Erros
            return cep
        elif:
        else:
            return 'Erro'
    except:
        return 'Erro'
