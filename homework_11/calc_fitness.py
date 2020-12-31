def calc_fitness(pop):
    from math import sin, sqrt

    # desvio padrao
    dp_x= 0
    dp_y = 0

    mean_x = 0
    mean_y = 0

    for index, elem in enumerate(pop):

        x = elem[0]
        y = elem[1]
        f6_plus = 999.5 - ((sin(sqrt(x**2 + y**2)))**2 - 0.5) / (1 + 0.001 * (x**2 + y**2))**2 # F6 elevada
        mean_x += elem[0]
        mean_y += elem[1]

        pop[index] = [f6_plus, elem]

    # desvio padrao
    mean_x = mean_x / len(pop)
    mean_y = mean_y / len(pop)
    numerador_x = 0
    numerador_y = 0

    for i in range(len(pop)):
        numerador_x += (float(pop[i][1][0]) - mean_x)**2
        numerador_y += (float(pop[i][1][1]) - mean_y)**2

    dp_x = sqrt(numerador_x / len(pop))
    dp_y = sqrt(numerador_y / len(pop))

    pop.insert(0, [mean_x, mean_y] + [dp_x, dp_y])

    print('media: ', mean_x, mean_y)
    print('desvio padrao: ', pop[-1])
    return pop

# populacao = [[10,10],[10,11]]
# calc_fitness(pop=populacao)
# print(populacao)
