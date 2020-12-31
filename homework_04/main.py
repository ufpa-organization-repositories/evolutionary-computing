# Algoritmo genético n°3
from random import random, seed
import numpy as np
from matplotlib import pyplot as plt
from math import sqrt
from calc_pop import calc_pop
from calc_roletaSimples import calc_roletaSimplesProporcional
from calc_pontoCorte import calc_pontoCorte
from calc_fitness import calc_fitness
from calc_mutacao import calc_mutacao
from to_decimal import to_decimal
from curvaNivel import plotCurvaNivel

from numpy import reshape
melhores_fitness = []

n_experimentos = 50
n_geracoes = 100
ensaio = []
experimento_temp = []
geracoes =[]
populacao = []
fitness_media = 0
desvio_padrao = 0

#graficos
y_fitness = []
y_fitness_media = []
y_desvio_padrao = []
y_nivel_diversidade = []
populacoes = []
populacoes_experimento = []

y_fitness_geral = []
y_fitness_media_geral = []
y_desvio_padrao_geral = []
y_nivel_diversidade_geral = []


# plota a f6
# cp = plotCurvaNivel(x_inicial=-5, x_final=5, y_inicial=-5, y_final=5, n=1000)
# plt.colorbar(cp)
# plt.title('Curvas de nível da função F6(x, y)')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()


for experimento in range(n_experimentos):
    seed(experimento)
    # inicializa a populacao e calcula a fitnesse de cada cromossomo ao mesmo tempo
    populacao = calc_pop(len_pop=100, x_inicial=-100, x_final=100, y_inicial=-100, y_final=100, i_experimento=experimento)
    # populacoes_experimento.append(populacao) # sera usado em trabalhos futuros
    #organiza a populacao pelo ranking: melhor aptidão para pior
    populacao = sorted(populacao, reverse=True)
    print(populacao)
    pop_filhos = []
    pop_pais = []

    for geracao in range(n_geracoes):
        seed(experimento * geracao)

        while not len(pop_filhos) == len(populacao):
            # seleciona um par de pais atraves do metodo de selecao roleta simples
            calc_roletaSimplesProporcional(populacao, num_selecionados=2, incremento=1000)
            # gera par de filhos com o par de pais selecionados atraves do metodo de cruzamento ponto de corte

            # 75% de ocorrer cruzamento
            if (random() * 100) <= 75:
                # print('\n' + 'cruzando')
                calc_pontoCorte(populacao, pop_filhos)
                # print('\n' + 'pop_filhos incrementada')
                # print(len(pop_filhos), pop_filhos)
            # else:
            # print('\n' + 'cruzamento não realizado')

        # faz a mutação nos filhos
        calc_mutacao(pop_filhos)

        # calcula a fitness dos filhos e retorna a fitness dos filhos na lista pop_filhos
        calc_fitness(pop=pop_filhos)
        # print('pop_filhos orndenada pela fitness')
        # print(len(pop_filhos), sorted(pop_filhos, reverse=True))

        # reset das variaveis
        populacao = sorted(pop_filhos, reverse=True)
        pop_filhos = []

        # media
        fitness_media = 0
        for elem in populacao:
            fitness_media += elem[0]
        fitness_media = fitness_media / len(populacao)

        # desvio padrao
        numerador = 0
        for elem in populacao:
            numerador += elem[0] ** 2
        argumento_raiz = numerador / len(populacao)
        desvio_padrao = sqrt(argumento_raiz)

        geracoes.append([populacao[0][0], fitness_media, desvio_padrao, populacao[0][1][0],populacao[0][1][1], str(experimento + 1), str(geracao + 1)], )


        print('Experimento: ', experimento + 1, '. Geracao: ', geracao + 1)
        # print('Populacao final: ', populacao)

    experimento_temp.append(geracoes)
    ensaio.append(experimento_temp)
    geracoes = []
    experimento_temp = []


# graficos
#fitness do melhor, media e desvio padrao de 50 experimentos
melhor_individuo = [0, 0, 0, 0, 0, 0, 0] #[fitness, media, desvio padrao, x, y, experimento, geracao]
i_melhor_experimento = 0
i_melhor_populacao = 0

# busca o melhor indivíduo de todos
for i, experimento in enumerate(ensaio):

    for i_geracao, geracao in enumerate(experimento):

        for i_individuo, individuo in enumerate(geracao):
            if individuo[0] > melhor_individuo[0]:
                melhor_individuo = [individuo[0], individuo[1], individuo[2], 'x =' + str(float("%.5f" % to_decimal(individuo[3]))), 'y =' + str(to_decimal(individuo[4])) ,'experimento=' + str(float("%.5f" % float(float(individuo[5])))), 'geracao=' + str(individuo[6])]
                i_melhor_experimento = i
                i_melhor_populacao = i_individuo

print('melhor individuo: ', melhor_individuo)
print('experimento: ', i_melhor_experimento + 1)
print('populacao: ', i_melhor_populacao + 1)

# grafico do melhor individuo
for i, experimento in enumerate(ensaio):

    # plota os gráficos só do melhor experimento
    if i == i_melhor_experimento:

        for geracao in experimento:
            # medida de diversidade do experimento
            medida_diversidade = 0
            for j in range(len(populacao)):
                # medida_diversidade = 0
                for index in range(len(populacao)):
                    # soma as diferenças em x e em y
                    medida_diversidade += abs(to_decimal(populacao[j][1][0]) - to_decimal(populacao[index][1][0]))
                    medida_diversidade += abs(to_decimal(populacao[j][1][1]) - to_decimal(populacao[index][1][1]))

                y_nivel_diversidade.append(medida_diversidade)


            # normalizacao do nível de diversidade para 0 e 1
            # maximo = max(y_nivel_diversidade)
            # for index, nivel in enumerate(y_nivel_diversidade):
            #     y_nivel_diversidade[index] = (nivel / maximo)

            for pop in geracao:
                y_fitness.append(pop[0])
                y_fitness_media.append(pop[1])
                y_desvio_padrao.append(pop[2])

        # melhor fitness
        x = np.arange(1, len(y_fitness) + 1, 1)
        fig, ax = plt.subplots()
        ax.plot(x, y_fitness)
        fig.suptitle('Média das aptidões dos melhores individuos do experimento ' + str(i + 1))  # Add a title so we know which it is
        plt.xlabel('Geracão')
        plt.ylabel('Fitness média dos melhores indivíduos')
        plt.show()

        # fitness_media
        x = np.arange(1, len(y_fitness_media) + 1, 1)
        fig, ax = plt.subplots()
        ax.plot(x, y_fitness_media)
        fig.suptitle('Média das aptidões médias do experimento ' + str(i + 1))  # Add a title so we know which it is
        plt.xlabel('Geracão')
        plt.ylabel('Média da Fitness média')
        plt.show()

        # desvio_padrao
        x = np.arange(1, len(y_desvio_padrao) + 1, 1)
        fig, ax = plt.subplots()
        ax.plot(x, y_desvio_padrao)
        fig.suptitle('Média dos desvios padrões das aptidões do experimento ' + str(i + 1))  # Add a title so we know which it is
        plt.xlabel('Geracão')
        plt.ylabel('Desvio padrão médio')
        plt.show()

        # medida_diversidade
        x = np.arange(1, len(y_nivel_diversidade) + 1, 1)
        fig, ax = plt.subplots()
        ax.plot(x, y_nivel_diversidade)
        fig.suptitle('Medida de diversidade do experimento ' + str(i + 1))  # Add a title so we know which it is
        plt.xlabel('População')
        plt.ylabel('Nível de diversidade')
        plt.show()

# print(ensaio)

# grafico geral do ensaio
fitness = []
media = []
desvio = []

from matplotlib import pyplot as plt
import numpy as np

for index, experimento in enumerate(ensaio):
    for populacao in experimento:
        for x, individuo in enumerate(populacao):
            fitness.append(individuo[0])

        x = np.arange(1, fitness.__len__() + 1)
        plt.plot(x, fitness)
    fitness = []

plt.suptitle('Fitness do melhor cromossomo por experimento')
plt.xlabel('Experimento')
plt.ylabel('Fitness')
plt.show()

for index, experimento in enumerate(ensaio):
    for populacao in experimento:
        for x, individuo in enumerate(populacao):
            media.append(individuo[1])

        x = np.arange(1, media.__len__() + 1)
        plt.plot(x, media)
    media = []

plt.suptitle('Fitness média por experimento')
plt.xlabel('Experimento')
plt.ylabel('Fitness')
plt.show()

for index, experimento in enumerate(ensaio):
    for populacao in experimento:
        for x, individuo in enumerate(populacao):
            desvio.append(individuo[2])

        x = np.arange(1, desvio.__len__() + 1)
        plt.plot(x, desvio)
    desvio = []

plt.suptitle('Desvio padrão médio')
plt.xlabel('Geração')
plt.ylabel('Fitness')
plt.show()
