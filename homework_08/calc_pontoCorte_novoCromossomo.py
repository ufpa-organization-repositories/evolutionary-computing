global pop_filhos
from to_decimal import to_decimal

def calc_pontoCorte(pop_pais, pop_filhos, n_pontos):
    from random import random, seed, randrange

    seed(random() * random())

    pai1_x = pop_pais[0][1][0]
    pai1_y = pop_pais[0][1][1]

    pai2_x = pop_pais[1][1][0]
    pai2_y = pop_pais[1][1][1]

    x1 = ""
    x2 = ""
    y1 = ""
    y2 = ""

    if n_pontos == 1:
        ponto = randrange(0, len(pop_pais[0][1][0]))
        print('ponto: ', ponto)

        # x
        x1 = pai1_x[:ponto] + pai2_x[ponto:]
        x2 = pai2_x[:ponto] + pai1_x[ponto:]

        # y
        y1 = pai1_y[:ponto] + pai2_y[ponto:]
        y2 = pai2_y[:ponto] + pai1_y[ponto:]

    else:

        pontosCorte = []
        for i in range(n_pontos):
            ponto = randrange(0, len(pop_pais[0][1][0]))
            while ponto in pontosCorte:
                ponto = randrange(0, len(pop_pais[0][1][0]))
            pontosCorte.append(ponto)
        pontosCorte.sort()

        for index, ponto in enumerate(pontosCorte):
            # print('ponto: ', ponto)

            # primeiro
            if index == 0:
                # x
                x1 += pai1_x[:pontosCorte[0]] + pai2_x[ponto:pontosCorte[1]]
                x2 += pai2_x[:pontosCorte[0]] + pai1_x[ponto:pontosCorte[1]]

                # y
                y1 += pai1_y[:pontosCorte[0]] + pai2_y[ponto:pontosCorte[1]]
                y2 += pai2_y[:pontosCorte[0]] + pai1_y[ponto:pontosCorte[1]]

            # intermediarios
            elif not index == n_pontos - 1:

                if index % 2 == 0:
                    # x
                    x1 += pai2_x[ponto:pontosCorte[index + 1]]
                    x2 += pai1_x[ponto:pontosCorte[index + 1]]

                    # y
                    y1 += pai2_y[ponto:pontosCorte[index + 1]]
                    y2 += pai1_y[ponto:pontosCorte[index + 1]]

                else:
                    # x
                    x1 += pai1_x[ponto:pontosCorte[index + 1]]
                    x2 += pai2_x[ponto:pontosCorte[index + 1]]

                    # y
                    y1 += pai1_y[ponto:pontosCorte[index + 1]]
                    y2 += pai2_y[ponto:pontosCorte[index + 1]]

            #ultimo
            else:
                if n_pontos % 2 == 0:
                    # x
                    x1 += pai1_x[ponto:]
                    x2 += pai2_x[ponto:]

                    # y
                    y1 += pai1_y[ponto:]
                    y2 += pai2_y[ponto:]
                else:
                    # x
                    x1 += pai2_x[ponto:]
                    x2 += pai1_x[ponto:]

                    # y
                    y1 += pai2_y[ponto:]
                    y2 += pai1_y[ponto:]


    filho1 = [x1, y1]
    filho2 = [x2, y2]
    # print('Par de filhos retornados')
    # print(filho1)
    # print(filho2)
    pop_filhos.append(filho1)
    pop_filhos.append(filho2)

    return 0

# pop_filhos = []
# pop_pais = [[0.976804032246384, ['0000000000000000000000000', '0000000000000000000000000']], [0.542563009148137, ['1111111111111111111111111', '1111111111111111111111111']]]
# len_pop = 2
#
# calc_pontoCorte(pop_pais,pop_filhos, n_pontos=6)
# print(pop_filhos)