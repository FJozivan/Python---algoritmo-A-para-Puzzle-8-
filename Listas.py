class Estado:
    puzzle = list();
    custo = 0
    caminho = 0


class Acao:
    direita = False
    esquerda = False
    cima = False
    baixo = False


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
            p1 = qual_posicao_Matriz(i)  # procura a posicao x,y da lista atual
            #  print('posição na lista atual: ', p1)
            p2 = qual_posicao_Matriz(l_meta.index(l_atual[i]))  # procura a posição x,y de um elementa da lista meta
            #  print('posição na lista meta: ', p2)
            p3 = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])  # quantidade de movimentos para chegar a posicao meta
            #  print('movimentos necessarios: ', p3)
            cont += p3  # acumulador de todos os movimentos necessarios
    return cont


def heuristica(l_atual, l_meta):
    custo_total = c_h1(l_atual, l_meta) + c_h2(l_atual, l_meta)
    return custo_total


def Verifica_acao(estado):
    p = qual_posicao_Matriz(estado.puzzle.index(0))
    a = Acao()

    if p == [0, 0]:
        a.baixo = True
        a.direita = True
        return a
    elif p == [0, 1]:
        a.esquerda = True
        a.baixo = True
        a.direita = True
        return a
    elif p == [0, 2]:
        a.esquerda = True
        a.baixo = True
        return a
    elif p == [1, 0]:
        a.cima = True
        a.baixo = True
        a.direita = True
        return a
    elif p == [1, 1]:
        a.cima = True
        a.baixo = True
        a.direita = True
        a.esquerda = True
        return a
    elif p == [1, 2]:
        a.cima = True
        a.baixo = True
        a.esquerda = True
        return a
    elif p == [2, 0]:
        a.cima = True
        a.direita = True
        return a
    elif p == [2, 1]:
        a.cima = True
        a.direita = True
        a.esquerda = True
        return a
    elif p == [2, 2]:
        a.cima = True
        a.esquerda = True
        return a


def gerar_filho(estado, p1, p2):
    filho = Estado()

    filho.puzzle = estado.puzzle[:]
    filho.caminho = estado.caminho

    aux = filho.puzzle[p1]
    filho.puzzle[p1] = filho.puzzle[p2]
    filho.puzzle[p2] = aux

    filho.caminho = filho.caminho + 1;
    t = [1, 2, 3, 4, 5, 6, 7, 8, 0];
    filho.custo = filho.caminho + heuristica(filho.puzzle, t)
    return filho


def executar_Acoes(estado, acao):
    estadoAtual = estado
    posicao_de_0_naLis_estadoAtual = estadoAtual.puzzle.index(0)
    p = qual_posicao_Matriz(posicao_de_0_naLis_estadoAtual)
    a = acao
    filhos = list()

    if a.cima:
        p2 = p[:]
        p2[0] = p2[0] - 1

        posicao_a_receber_0_naLis_filho = qual_posicao_Lista(p2)
        filhos.append(gerar_filho(estadoAtual, posicao_de_0_naLis_estadoAtual, posicao_a_receber_0_naLis_filho))

    if a.baixo:
        p2 = p[:]
        p2[0] = p2[0] + 1

        posicao_a_receber_0_naLis_filho = qual_posicao_Lista(p2)
        filhos.append(gerar_filho(estadoAtual, posicao_de_0_naLis_estadoAtual, posicao_a_receber_0_naLis_filho))

    if a.direita:
        p2 = p[:]
        p2[1] = p2[1] + 1

        posicao_a_receber_0_naLis_filho = qual_posicao_Lista(p2)
        filhos.append(gerar_filho(estadoAtual, posicao_de_0_naLis_estadoAtual, posicao_a_receber_0_naLis_filho))
    if a.esquerda:
        p2 = p[:]
        p2[1] = p2[1] - 1

        posicao_a_receber_0_naLis_filho = qual_posicao_Lista(p2)
        filhos.append(gerar_filho(estadoAtual, posicao_de_0_naLis_estadoAtual, posicao_a_receber_0_naLis_filho))

    return filhos


def fronteira(Estado, frontier):
    a = Estado.custo
    if not frontier:
        frontier.append(Estado)
    else:
        for i in range(len(frontier)):
            if a < frontier[i].custo:
                frontier.insert(i, Estado)
                break

    return frontier


def qual_posicao_Matriz(posicao):
    p = posicao
    if p == 0:
        return [0, 0]
    elif p == 1:
        return [0, 1]
    elif p == 2:
        return [0, 2]
    elif p == 3:
        return [1, 0]
    elif p == 4:
        return [1, 1]
    elif p == 5:
        return [1, 2]
    elif p == 6:
        return [2, 0]
    elif p == 7:
        return [2, 1]
    elif p == 8:
        return [2, 2]


def qual_posicao_Lista(posicaoMatriz):
    p = posicaoMatriz
    if p == [0, 0]:
        return 0
    elif p == [0, 1]:
        return 1
    elif p == [0, 2]:
        return 2
    elif p == [1, 0]:
        return 3
    elif p == [1, 1]:
        return 4
    elif p == [1, 2]:
        return 5
    elif p == [2, 0]:
        return 6
    elif p == [2, 1]:
        return 7
    elif p == [2, 2]:
        return 8


frontier = list()

a = Acao()
E = Estado()
filhos = list()

meta = [1, 2, 3, 4, 5, 6, 7, 8, 0]
E.puzzle = list(map(int, input().split(" ")))
E.custo = E.caminho + heuristica(E.puzzle, meta)
frontier = fronteira(E, frontier)

q = Estado()
lista_Explorados = list()

for w in range(1000000):

    if frontier[0].puzzle != meta:
        q = frontier[0]
        explo = False
        frontier.pop(0)
        # for g in range(len(lista_Explorados)):
        #     if lista_Explorados[g].puzzle == q.puzzle:
        #         explo = True

        # if explo == False:
        lista_Explorados.append(q)
        b = Verifica_acao(q)
        f = executar_Acoes(q, b)
        for i in range(len(f)):
            frontier = fronteira(f[i], frontier)
    else:
        print("Encontradp")

for i in range(len(frontier)):
    print("Filho: ", i)
    print(frontier[i].puzzle)
    print("caminho: ", frontier[i].caminho)
    print("custo: ", frontier[i].custo)

# Deeved, o codigo ainda nao esta encontrando o resultado temos que rever a heuristica
