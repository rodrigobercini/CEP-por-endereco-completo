# Finding the CEP (brazilian zip code) of a complete address

```
Código de Endereçamento Postal (Postal Addressing Code) is the
Brazilian postal code system commonly known as CEP.
```
[WikiPedia](https://en.wikipedia.org/wiki/C%C3%B3digo_de_Endere%C3%A7amento_Postal)

There are several services and libraries that can get an address by providing a CEP number. This repository works the other way around, the input is a complete address and the matching CEP number is the output.

## Correios official website endpoint is not available anymore

When I first wrote this piece of code, the Correios website allowed to search for a CEP using its complete address. This is not possible anymore as you can see on this page (the original endpoint):

http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCep.cfm

I'm currently using the Mapacep website for the requests.

https://www.mapacep.com.br/

## Running an example

1) Clone the repository:

```
git clone https://github.com/rodrigobercini/CEP-por-endereco-completo.git
```

2) Install the requirements via pip:

```
pip install -r requirements.txt
```

3) Run the example file:

```
python example.py
```

## Package in PyPI 

The package currently available in PyPI is outdaded. I haven't created a CI/CD pipeline when I first uploaded the library and I don't have time to update the files there. Also, I've made some structural changes to the methods and I don't want to break people's projects (even though I highly doubt there is someone using this library).
