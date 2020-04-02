# CEP finder by address

```
Código de Endereçamento Postal (Postal Addressing Code) is the
Brazilian postal code system commonly known as CEP.
```
[WikiPedia](https://en.wikipedia.org/wiki/C%C3%B3digo_de_Endere%C3%A7amento_Postal)

There are several services and libraries that can get an address by providing a CEP number. This repository works the other way around, the input is a complete address and the matching CEP number is the output.

## How to use

The package can be installed via pip:

```
pip install CEP-por-endereco-completo
```

The function takes address, number, city and uf (state abbreviation) as arguments.

```
cep_finder(address, number, city, uf)
```

## Example:

Input:
```
from CEP_por_endereco.cep_finder import cep_finder
cep_finder('avenida protasio alves', '1889', 'Porto Alegre', 'RS')
```

Output:
```
'90450-190'
```

## Libraries used
``` 
beautifulsoup4
requests
unicodedata
```