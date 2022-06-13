produtos = list()
dados = list()

while True:
    nome = str(input('Nome do produto: '))
    dados.append(nome)
    preço = float(input('Preço: R$ '))
    dados.append(preço)
    estoque = int(input('Quantidade em estoque: '))
    dados.append(estoque)
    produtos.append(dados[:])
    dados.clear()
    continuidade = str(input('Deseja continuar [S/N]? ')).upper().strip()
    if continuidade == 'N':
        break
print(produtos)
# for i, v in enumerate(produtos):
#     print(i)
#     print(v[i][0])
