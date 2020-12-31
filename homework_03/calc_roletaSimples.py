from random import uniform, seed
global pop_pais
global len_pop
global pop_filhos
# len_pop = 4
# par_pais = []

def calc_roletaSimplesProporcional(populacao, num_selecionados):
    roleta = []
    pop_pais = []

    for i in range(len(populacao)):
        if i == 0:
            roleta.append(float("%.5f" %populacao[0][0]))
        else:
            roleta.append((float("%.5f" %roleta[i - 1]) + float("%.5f" %populacao[i][0])))

    # print(roleta)

    index_selecionado = 0
    for i in range(num_selecionados):
        seed()
        num_aleatorio = (uniform(0, roleta[-1]))
        for index_roleta, elem in enumerate(roleta):
            if index_roleta == 0:
                index_selecionado = index_roleta
            else:
                if num_aleatorio > elem:
                    index_selecionado = index_roleta + 1
        # print('selecionado: ', index_selecionado)
        pop_pais.append(populacao[index_selecionado])

    # print('tamanho da pop_pais: ', len(pop_pais), end='\n' + str(pop_pais))

    return 0

# populacao = [0.5, ['x1', 'y1']], [0.5, ['x2', 'y2']], [0.5, ['x3', 'y3']], [0.5, ['x4', 'y4']]
# pop_pais = []
# tc = 75


# pop_pais = calc_roletaSimplesProporcional(populacao=populacao, num_selecionados=2)

