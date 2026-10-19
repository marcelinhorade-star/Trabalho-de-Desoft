grid = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]

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