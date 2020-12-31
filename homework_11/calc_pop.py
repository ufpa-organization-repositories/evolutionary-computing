def calc_pop(len_pop, x_inicial, x_final, y_inicial, y_final, i_experimento):
    from random import uniform, seed, random
    populacao = []

    for i in range(len_pop):
        seed((i + 1)* (i_experimento + 1))
        x = float("%.5f" % uniform(x_inicial, x_final))
        y = float("%.5f" % uniform(y_inicial, y_final))
        populacao.append([x, y])

    # calc_fitness(pop=populacao)
    # calc_fitness(pop=populacao)
    print(len(populacao), populacao)
    return populacao

len_pop = 100; x_inicial = -100; x_final = 100; y_inicial = -100; y_final = 100
i_experimento = 0

populacao = calc_pop(len_pop, x_inicial, x_final, y_inicial, y_final, i_experimento)
