def c_h1(l_atual, l_meta):  # calcula o custo de h1
    cont = 0
    for i in range(len(l_atual)):
        if l_atual[i] != 0:
            if l_atual[i] != l_meta[i]:
                cont += 1
    return cont


def c_h2(l_atual, l_meta):  # calcula o custo de h2
    cont = 0
    for i in range(len(l_atual)):
        if l_atual[i] != 0:
            #  print('numero procurado: ', l_atual[i])
            p1 = qual_posicao(i)  # procura a posicao x,y da lista atual
            #  print('posição na lista atual: ', p1)
            p2 = qual_posicao(l_meta.index(l_atual[i]))  # procura a posição x,y de um elementa da lista meta
            #  print('posição na lista meta: ', p2)
            p3 = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])  # quantidade de movimentos para chegar a posicao meta
            #  print('movimentos necessarios: ', p3)
            cont += p3  # acumulador de todos os movimentos necessarios
    return cont


def qual_posicao(posicao):
    p = posicao
    if p == 0:
        return [2, 0]
    elif p == 1:
        return [2, 1]
    elif p == 2:
        return [2, 2]
    elif p == 3:
        return [1, 0]
    elif p == 4:
        return [1, 1]
    elif p == 5:
        return [1, 2]
    elif p == 6:
        return [0, 0]
    elif p == 7:
        return [0, 1]
    elif p == 8:
        return [0, 2]


def heuristica(l_atual, l_meta):
    custo_total = c_h1(l_atual, l_meta) + c_h2(l_atual, l_meta)
    return custo_total

l_a = [0, 6, 3, 1, 4, 2, 8, 7, 5]
l_m = [1, 2, 3, 4, 5, 6, 7, 8, 0]
h = heuristica(l_a, l_m)
print('valor da heuristica para esse problema: ', h)