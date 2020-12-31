from numpy import random
def calc_cruzamentoUniforme(pop_pais, pop_filhos):

    len_mascara = pop_pais[0][1][0].__len__()
    mascara = ""
    random.seed()

    filho_1 = ["",""]
    filho_2 = ["",""]

    for i in range(len_mascara):
        mascara += str(random.randint(low=0, high=2))
    print(mascara)

    for index, elem in enumerate(mascara):
        if elem == str(0):
            # x
            filho_1[0] += pop_pais[0][1][0][index]
            filho_1[1] += pop_pais[0][1][1][index]
            # y
            filho_2[0] += pop_pais[1][1][0][index]
            filho_2[1] += pop_pais[1][1][1][index]

        else:
            # x
            filho_1[0] += pop_pais[1][1][0][index]
            filho_1[1] += pop_pais[1][1][1][index]
            # y
            filho_2[0] += pop_pais[0][1][0][index]
            filho_2[1] += pop_pais[0][1][1][index]

    print(str(filho_1))
    print(str(filho_2))

    pop_filhos.append(filho_1)
    pop_filhos.append(filho_2)

# pop_pais = [[0.976804032246384, ['a'*25, 'b'*25]], [0.542563009148137, ['c'*25, 'd'*25]]]
# pop_filhos = []
# calc_cruzamentoUniforme(pop_pais, pop_filhos)