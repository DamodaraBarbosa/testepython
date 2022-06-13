import funções


produtos = list()
dados = list()

while True:
    nome = str(input('Nome do produto: '))
    vnome = nome.replace(" ", "")
    while vnome.isalpha() == False:
        funções.erro()
        nome = str(input('Nome do produto: '))
        vnome = nome.replace(" ", "")
    dados.append(nome)
    try:
        preço = float(input('Preço do produto: R$ '))
    except ValueError:
        funções.erro()
        while True:
            try:
                preço = float(input('Preço do produto: R$ '))
                break
            except ValueError:
                funções.erro()
    dados.append(preço)
    try:
        estoque = int(input('Quantidade no estoque: '))
    except ValueError:
        funções.erro()
        while True:
            try:
                estoque = int(input('Quantidade no estoque: '))
                break
            except ValueError:
                funções.erro()
    dados.append(estoque)
    produtos.append(dados[:])
    dados.clear()
    continuidade = str(input('Deseja continuar [S/N]? ')).upper().strip()
    while continuidade not in 'SN':
        funções.erro()
        continuidade = str(input('Deseja continuar [S/N]? ')).upper().strip()
    if continuidade == 'N':
        break
funções.tabela(produtos)
for i, v in enumerate(produtos):
    print(i)
    print(v)

