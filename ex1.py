lista = []

while True:
    nome_produto = input('Insira o nome do objeto (Digite 0 se desejar sair): ').lower()
    avaliacao = int(input('Insira sua nota: '))


    if nome_produto == '0' and avaliacao == 0:
        print('Encerrando..')
        break
    else:
        print(f'Avaliação para {nome_produto} foi cadastrada!')
        lista.append((nome_produto, avaliacao))

def filtrar(nome):
    for n in lista:
        if n[0] == nome:
            if nome_produto != 0:
                produtos = {
                    'nome': nome,
                    'avaliacao':[n[1] for n in lista if n[0] == nome]
                }

                relatorio = {
                    'nome': nome,
                    'media': sum(produtos['avaliacao']) / len(produtos['avaliacao']),            
                }    
    return relatorio

filtro = input('Insira o nome do produto que deseja exibir a media das avaliações: ').lower()

print(lista)
print(filtrar(filtro))