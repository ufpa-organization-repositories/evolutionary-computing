global pop_filhos
from to_decimal import to_decimal

def calc_pontoCorte(pop_pais, pop_filhos):
    from random import random, seed, randrange

    seed(random() * random())

    pai1_x = pop_pais[0][1][0]
    pai1_y = pop_pais[0][1][1]

    pai2_x = pop_pais[1][1][0]
    pai2_y = pop_pais[1][1][1]

    erro = True
    x1 = []
    x2 = []
    y1 = []
    y2 = []

    # x
    while erro:
        i_pontoCorte = randrange(1, len(pop_pais[0][1][0]))
        x1 = pai1_x[:i_pontoCorte] + pai2_x[i_pontoCorte:]
        x2 = pai2_x[:i_pontoCorte] + pai1_x[i_pontoCorte:]
        try:
            to_decimal(x1)
            to_decimal(x2)
            erro = False
            if Exception == "Numero binario com mais de uma virgula":
                pass
        except:
            erro = True


    # y
    erro = True
    while erro:
        i_pontoCorte = randrange(1, len(pop_pais[0][1][0]))
        y1 = pai1_y[:i_pontoCorte] + pai2_y[i_pontoCorte:]
        y2 = pai2_y[:i_pontoCorte] + pai1_y[i_pontoCorte:]
        try:
            to_decimal(y1)
            to_decimal(y2)
            erro = False
            if Exception == "Numero binario com mais de uma virgula":
                pass
        except:
            erro = True

    filho1 = [x1, y1]
    filho2 = [x2, y2]
    # print('Par de filhos retornados')
    # print(filho1)
    # print(filho2)
    pop_filhos.append(filho1)
    pop_filhos.append(filho2)

    # else:
    # print('Não realizou o cruzamento')

    return 0
# pop_filhos = []
# pop_pais = [[0.976804032246384, ['0.01111100100110000101111', '10.11111011010010110111001']], [0.542563009148137, ['-1.01100111010110000011101', '0.01110001010110110101011']]]
#
#
# len_pop = 2
#
# calc_pontoCorte(pop_pais,pop_filhos)
# print(pop_filhos)