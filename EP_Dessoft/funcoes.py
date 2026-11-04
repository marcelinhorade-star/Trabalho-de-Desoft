
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

def afundados(frota, tabuleiro):
    quantidade = 0

    for nome_navio in frota:
        for navio in frota[nome_navio]:
            acertos = 0

            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]

                if tabuleiro[linha][coluna] == 'X':
                    acertos += 1

            if acertos == len(navio):
                quantidade += 1

    return quantidade

def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for posicao in posicoes:
        linha_navio = posicao[0]
        coluna_navio = posicao[1]

        if linha_navio < 0 or linha_navio >= 10:
            return False

        if coluna_navio < 0 or coluna_navio >= 10:
            return False

        for nome_navio in frota:
            for navio in frota[nome_navio]:
                if posicao in navio:
                    return False

    return True

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

