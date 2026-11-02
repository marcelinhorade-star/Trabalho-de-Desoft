
# linha = int(input('linha:'))
# coluna = int(input('coluna:'))
# orientacao = input('orientação:')
# tamanho = int(input('tamanho:'))

def define_posicoes (linha, coluna, orientacao, tamanho):
    lista_posicao = []
    i = 0
    if orientacao == 'vertical':
    
        while i < tamanho:
            lista_posicao.append ([linha + i, coluna])
            i += 1

    elif orientacao == 'horizontal':

        while i < tamanho:
            lista_posicao.append ([linha,coluna + i])
            i += 1
    return lista_posicao

# posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
# print(posicoes)

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio not in frota:
        frota[nome_navio] = []

    frota[nome_navio].append(posicoes)

    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = []

    i = 0
    while i < 10:
        linha = []
        j = 0
        while j < 10:
            linha.append(0)
            j += 1
        tabuleiro.append(linha)
        i += 1

    for nome_navio in frota:
        for navio in frota[nome_navio]:
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1

    return tabuleiro