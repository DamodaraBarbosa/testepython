def linha():
    print('\033[1;33m--\033[m'*30)


def erro():
    print('\033[1;31mValor inválido, digite novamente!\033[m')


def tabela ():
    linha()
    print('\033[1;33mDADOS DOS PRODUTOS\033[m')
    linha()
    print('\033[1;33mCÓDIGO\033m', end='')
    print('\033[1;33mNOME\033[m', end='')
    print('\033[1;33mPREÇO (R$)\033[m', end='')
    print('\033[1;33mESTOQUE (unid.)\033[m',end='')
    for i, v in enumerate(produtos):
        print(i)
        print(v)