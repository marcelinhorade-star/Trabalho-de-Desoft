from funcoes import posicao_valida, preenche_frota

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

print(frota)