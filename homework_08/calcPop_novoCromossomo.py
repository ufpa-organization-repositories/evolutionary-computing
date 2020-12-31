from random import seed
from numpy import random

def calc_pop(len_pop, dicionario, i_experimento):
    from calc_fitness_novoCromossomo import calc_fitness
    populacao = []

    for i in range(len_pop):
        seed(i * (i_experimento + 1))

        x = bin(round(random.uniform(low=0, high=int(0b111111111111111111111111))))
        x = x[2:].zfill(24)

        y = bin(round(random.uniform(low=0, high=int(0b111111111111111111111111))))
        y = y[2:].zfill(24)

        populacao.append([x, y])

    calc_fitness(pop=populacao, dicionario=dicionario)
    return populacao

# import pickle
#
# dicionario = pickle.load(open("dicionario_final.pkl", "rb"))
# dicionario_copy = dicionario.copy()
#
# len_pop = 100
# n_experimentos = 1
#
# for experimento in range(n_experimentos):
#     populacao = calc_pop(len_pop, dicionario, i_experimento=experimento)
#     print('experimento: ', experimento)
#     print(populacao.__len__())
#     print(populacao)