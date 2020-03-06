# CEP finder by address

```
Código de Endereçamento Postal (Postal Addressing Code) is the
Brazilian postal code system commonly known as CEP.
```
[WikiPedia](https://en.wikipedia.org/wiki/C%C3%B3digo_de_Endere%C3%A7amento_Postal)

There are several services and libraries that can get an address by providing a CEP number. This repository works the other way around, the input is a complete address and the matching CEP number is the output.


# Libraries needed
``` 
pip install beautifulsoup4
pip install requests
```

# How to use

```
cep_finder(address, number, city, uf)
```
Special characters are not supported, so instead of "avenida protásio alves", the input should be "avenida protasio alves".

The function takes address, number, city and uf (state abbreviation) as arguments.

## Example:

Input:

cep_finder('avenida protasio alves', '1889', 'Porto Alegre', 'RS')

Output:
```
'90450-190'
```
