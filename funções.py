import enum


def linha():
    print('\033[1;33m--\033[m'*34)


def linha2():
    print('\033[1;33m=-\033[m'*34)


def erro():
    print('\033[1;31mValor inválido, digite novamente!\033[m')


def tabela(lista):
    linha()
    print(f'{"DADOS DOS PRODUTOS":>42}')
    linha()
    print(f'{"CÓDIGO"}', end='')
    print(f'{"NOME":>15}', end='')
    print(f'{"PREÇO (R$)":>20}', end='')
    print(f'{"ESTOQUE (unid.)":>25}')
    for i, v in enumerate(lista):
        print(i, end=' ')
        print(f'\033[1;31m{lista[i][0]:>20}\033[m', end= ' ')
        print(f'\033[1;32m{lista[i][1]:>13}\033[m', end=' ')
        print(f'\033[1;37m{lista[i][2]:>22}\033[m')
    linha()


def opções():
    linha2()
    print('1. Busca de dados por código.')
    print('2. Análise do preço dos produtos.')
    print('3. Análise do estoque dos produtos.')
    print('0. Finalizar programa')
    linha2()


def tratamento(opção, lista):
    if opção == 1:
        código = int(input('Digite o código do produto que deseja buscar os dados: '))
        while código not in range(len(lista)):
            erro()
            código = int(input('Digite o código do produto que deseja buscar os dados: '))
        linha()
        print(f'{"DADOS DO PRODUTO":>37} - Código: {código}')
        linha()
        for i, v in enumerate(lista):
            if código == i:
                print(f'Nome: \033[1;31m{lista[i][0]}\033[m', end= '       ')
                print(f'| Preço: \033[1;32mR$ {lista[i][1]}\033[m', end= '       ')
                print(f'| Estoque: \033[1;37m{lista[i][2]} unidades\033m')
    elif opção == 2:
        soma = 0
        nomemaior = ''
        nomemenor = ''
        maior = 0
        menor = 0
        for i, v in enumerate(lista):
            if i == 0:
                maior = menor = lista[i][1]
                nomemaior = nomemenor = lista[i][0]
            else:
                if lista[i][1] > maior:
                    maior = lista[i][1]
                    nomemaior = lista[i][0]
                if lista[i][1] < menor:
                    menor = lista[i][1]
                    nomemenor = lista[i][0]
            soma += lista[i][1]
        media = soma/len(lista)
        print(f'A média do preço dos produtos é \033[1;35mR$ {media:.2f}\033[m.')
        print(f'O produto mais barato é \033[1;31m{nomemenor}\033[m custando \033[1;32mR$ {menor}\033[m.')
        print(f'O produto mais caro é \033[1;31m{nomemaior}\033[m custando \033[1;32mR$ {maior}\033[m.')
        linha()
        expansão = str(input('Deseja uma análise mais detalhada dos preços [S/N]? ')).upper().strip()
        linha()
        while expansão == '' or expansão not in 'SN':
            erro()
            expansão = str(input('Deseja uma análise mais detalhada dos preços [S/N]? ')).upper().strip()
            linha()
        if expansão == 'S':
            for i, v in enumerate(lista):
                if lista[i][1] < media:
                    print(f'O produto \033[1;31m{lista[i][0]}\033[m com preço \033[1;32mR$ {lista[i][1]}\033[m está abaixo da média de preços (\033[1;35mR$ {media:.2f}\033[m).')
                else:
                    print(f'O produto \033[1;31m{lista[i][0]}\033[m com preço \033[1;32mR$ {lista[i][1]}\033[m está acima da média de preços (\033[1;35mR$ {media:.2f}\033[m).')
    elif opção == 3:
        soma = 0
        maior = 0
        nomemaior = ''
        menor = 0
        nomemenor = ''
        for i, v in enumerate(lista):
            soma += lista[i][2]
            if i == 0:
                maior = menor = lista[i][2]
                nomemaior = nomemenor = lista[i][0]
            else:
                if lista[i][2] > maior:
                    maior = lista[i][2]
                    nomemaior = lista[i][0]
                if lista[i][2] < menor:
                    menor = lista[i][2]
                    nomemenor = lista[i][0]
        media = soma/len(lista)
        print(f'A média de produtos no estoque é de \033[1;35m{media:.2f} unidades.\033[m')
        print(f'O produto com menor estoque é \033[1;31m{nomemenor}\033[m com \033[1;37m{menor} unidades\033[m no estoque.')
        print(f'O produto com maior estoque é \033[1;31m{nomemaior}\033[m com \033[1;37m{maior} unidades\033[m no estoque.')
        linha()
        expansão = str(input('Deseja uma análise mais detalhada do estoque dos produtos [S/N]? ')).upper().strip()
        while expansão == '' or expansão not in 'SN':
            erro()
            expansão = str(input('Deseja uma análise mais detalhada do estoque dos produtos [S/N]? ')).upper().strip()
        linha()
        for i, v in enumerate(lista):
            if lista[i][2] < media:
                print(f'O produto \033[1;31m{lista[i][0]}\033[m possui estoque \033[1;37m({lista[i][2]} unidades)\033[m abaixo da média \033[1;35m({media:.2f} unidades)\033[m.')
            else:
                print(f'O produto \033[1;31m{lista[i][0]}\033[m possui estoque \033[1;37m({lista[i][2]} unidades)\033[m acima da média \033[1;35m({media:.2f} unidades)\033[m.')

                    

