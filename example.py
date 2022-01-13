from cep_finder import CepFinder

if __name__ == '__main__':
    cep_finder = CepFinder(
        address = 'Rua Jardim João XXIII'
        , number = '120'
        , city = 'Salvador'
        , uf = 'BA'
        , verbose = True
    )
    cep = cep_finder.find_cep_mapacep()
    print(cep)