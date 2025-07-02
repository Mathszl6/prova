sistema = input('Insira os nomes separados por virgula: ').lower()
nomes = sistema.split(',')


vogais = {
        'a': 'a',
        'e': 'e',
        'i': 'i',
        'o': 'o',
        'u': 'u',
    }


def processar(nomes):
    nomes_vogais = []
    nomes_cons = []

    for nome in nomes:
        if nome[0] in vogais:
            nomes_vogais.append(nome)
        else:
            nomes_cons.append(nome)
    return (nomes_vogais, nomes_cons)

print(processar(nomes))