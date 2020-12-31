def calc_pop(len_pop, x_inicial, x_final, y_inicial, y_final, i_experimento):
    from random import uniform, seed, random
    from to_binary import to_binary
    from calc_fitness import calc_fitness
    populacao = []

    for i in range(len_pop):
        seed(i * i_experimento)
        x = to_binary(float("%.5f" % uniform(x_inicial, x_final)))
        y = to_binary(float("%.5f" % uniform(y_inicial, y_final)))
        populacao.append([x, y])

    calc_fitness(pop=populacao)

    # print(len(populacao), populacao)
    return populacao

# len_pop = 100; x_inicial = -5; x_final = 5; y_inicial = -5; y_final = 5; populacao = []
# populacao = calc_pop(len_pop, x_inicial, x_final, y_inicial, y_final, i_experimento=1)
# print(populacao)

