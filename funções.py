def linha():
    print('\033[1;33m--\033[m'*30)


def erro():
    print('\033[1;31mValor inválido, digite novamente!\033[m')


def tabela (lista):
    linha()
    print('\033[1;33mDADOS DOS PRODUTOS\033[m')
    linha()
    print('Nome do produto', end='')
    print('Preço (R$)', end='')
    print('Quantidade em estoque',end='')