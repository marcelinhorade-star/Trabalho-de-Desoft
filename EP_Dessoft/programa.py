from funcoes import posicao_valida, preenche_frota, posiciona_frota, faz_jogada, afundados, monta_tabuleiros
import random
frota = {}

nomes = ['porta-aviões', 'navio-tanque', 'contratorpedeiro', 'submarino']
tamanhos = [4, 3, 2, 1]
quantidades = [1, 2, 3, 4]

i = 0
while i < len(nomes):
    nome = nomes[i]
    tamanho = tamanhos[i]
    quantidade = quantidades[i]

    contador = 0
    while contador < quantidade:
        print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')

        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))

        if nome != 'submarino':
            escolha = int(input('Orientação: '))

            if escolha == 1:
                orientacao = 'vertical'
            else:
                orientacao = 'horizontal'
        else:
            orientacao = 'vertical'

        if posicao_valida(frota, linha, coluna, orientacao, tamanho):
            frota = preenche_frota(
                frota, nome, linha, coluna, orientacao, tamanho
            )
            contador += 1
        else:
            print('Esta posição não está válida!')

    i += 1

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

jogando = True

while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    posicao_nova = False

    while not posicao_nova:
        linha = int(input('Linha: '))

        while linha < 0 or linha > 9:
            print('Linha inválida!')
            linha = int(input('Linha: '))

        coluna = int(input('Coluna: '))

        while coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            coluna = int(input('Coluna: '))

        if tabuleiro_oponente[linha][coluna] == 'X' or tabuleiro_oponente[linha][coluna] == '-':
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        else:
            posicao_nova = True

# jogar meu ataque no tabuleiro do cara, ai ver se derrubei os 10 dele e se sim, cabar com o jogo 
# se ainda nao, sorteia os ataques do cara,faz a conferencia se a posicao ja foi, quando escolher uma 
# posicao q dá mostra no terminal pra mim qq ele atacou, ai marca no meu c ele errou ou matou um meu
# vê se ele acertou todos os meus e se sim F

        tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False

    else:
        linha_oponente = random.randint(0, 9)
        coluna_oponente = random.randint(0, 9)

        while tabuleiro_jogador[linha_oponente][coluna_oponente] == 'X' or tabuleiro_jogador[linha_oponente][coluna_oponente] == '-':
            linha_oponente = random.randint(0, 9)
            coluna_oponente = random.randint(0, 9)

        print(f'Seu oponente está atacando na linha {linha_oponente} e coluna {coluna_oponente}')

        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha_oponente, coluna_oponente)

        if afundados(frota, tabuleiro_jogador) == 10:
            print('Xi! O oponente derrubou toda a sua frota =(')
           
            jogando = False
