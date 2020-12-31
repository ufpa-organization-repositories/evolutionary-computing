def calc_fitness(pop):
    from to_decimal import to_decimal
    from math import sin, sqrt

    for index, elem in enumerate(pop):

        # só atribui a fitness a cromossomos que ainda não possuem fitness
        # print(elem[0], elem[1])
        x = to_decimal(elem[0])
        y = to_decimal(elem[1])
        # x = elem[0]
        # y = elem[1]
        f6_plus = 999.5 - ((sin(sqrt(x**2 + y**2)))**2 - 0.5) / (1 + 0.001 * (x**2 + y**2))**2 # F6 elevada
        pop[index] = [f6_plus, elem]

    return 0

# populacao = [[0,0],[-3,1]]
# calc_fitness(pop=populacao)
# print(populacao)

