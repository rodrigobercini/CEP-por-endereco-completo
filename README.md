Find an english version of this README file [here](https://github.com/rodrigobercinimartins/CEP-por-endereco/blob/master/EN_README.md).

## Encontrando CEP a partir de endereços completos

```
"CEP é a sigla de Código de Endereçamento Postal, criado e utilizado pelos Correios para facilitar o encaminhamento
e a entrega das correspondências aos destinatários. O CEP é uma informação indispensável na correspondência,
pois identifica todos os detalhes do endereço."

```
[Significados](https://www.significados.com.br/cep/)

Há diversos serviços e repositórios que retornam um determinado endereço a partir do CEP. Este repositório faz o caminho contrário: encontra CEPs a partir de endereços completos.

## Bibliotecas necessárias
``` 
pip install beautifulsoup4
pip install requests
```

## Como usar

```
cep_finder(address, number, city, uf)
```
A função toma endereço, número, cidade e UF como argumentos.

Caracteres especiais não são permitidos e resultarão em erro. Exemplo:

Incorreto: cep_finder("av protásio alves", "17", "porto alegre", "RS') 

Correto: cep_finder("av protasio alves", "17", "porto alegre", "RS')

## Exemplo:

```
cep_finder('avenida protasio alves', '1889', 'Porto Alegre', 'RS')
```

Retorna:
```
'90450-190'
```
