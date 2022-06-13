def linha():
    print('\033[1;33m--\033[m'*34)


def erro():
    print('\033[1;31mValor inválido, digite novamente!\033[m')


def tabela (lista):
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

    def analise():