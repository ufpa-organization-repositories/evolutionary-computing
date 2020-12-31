# Algoritmo genético n°8
# aumentar a taxa de mutacao quando a diversidade for baixa
# diminuir a taxa de mutacao quando a diversidade for alta
# diversidade: dostancia de hamming

from random import random, seed
import numpy as np
from matplotlib import pyplot as plt
from math import sqrt
# from calc_pop import calc_pop
from calcPop_novoCromossomo import calc_pop
from calc_roletaSimples import calc_roletaSimplesProporcional
# from calc_pontoCorte import calc_pontoCorte
from calc_pontoCorte import calc_pontoCorte
from calc_pontoCorte_novoCromossomo import calc_pontoCorte

# from calc_fitness import calc_fitness
from calc_fitness_novoCromossomo import calc_fitness
from calc_mutacao import calc_mutacao
from to_decimal import to_decimal
from curvaNivel import plotCurvaNivel

import pickle

print('Pegando dicionário que mapeia os binários para reais')
dicionario = pickle.load(open("dicionario_final.pkl", "rb"))
dicionario_copy = dicionario.copy()

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
y_nivel_diversidade_geral = []
populacoes = []
populacoes_experimento = []

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
    # populacao = calc_pop(len_pop=100, x_inicial=-100, x_final=100, y_inicial=-100, y_final=100, i_experimento=experimento)
    populacao = calc_pop(len_pop=100, dicionario=dicionario, i_experimento=experimento)
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
            pop_pais = calc_roletaSimplesProporcional(populacao, num_selecionados=2)
            # gera par de filhos com o par de pais selecionados atraves do metodo de cruzamento ponto de corte

            # 75% de ocorrer cruzamento
            if (random() * 100) <= 75:
                calc_pontoCorte(pop_pais, pop_filhos, n_pontos=2)

        # diversidade de hamming
        melhor = [0, 0, 0]
        pior = [1, 1, 1]
        print(melhor)
        for i in range(len(populacao)):
            print(i, populacao[i])
            if populacao[i][0] > melhor[0]: melhor = populacao[i]
            if populacao[i][0] < pior[0]:   pior = populacao[i]

        print("Experimento: ", experimento, " Geracao :", geracao)
        print("melhor e pior ",melhor, pior)

        diversidade_hamming_x = 0
        diversidade_hamming_y = 0

        for i in range(24):
            diversidade_hamming_x += abs(int(melhor[1][0][i]) - int(pior[1][0][i]))
            diversidade_hamming_y += abs(int(melhor[1][1][i]) - int(pior[1][1][i]))
        print(diversidade_hamming_x, diversidade_hamming_y)

        calc_mutacao(pop_filhos)
        calc_fitness(pop=pop_filhos, dicionario=dicionario)

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

        geracoes.append(populacao)

    ensaio.append(geracoes)
    geracoes = []

print("Ensaios: ", ensaio.__len__())
for i in range(ensaio.__len__()):
    for j in range(ensaio[i].__len__()):
        print("Experimento: " + str(i + 1) + ". Geracao: " + str(j + 1))

        melhor = [0, 0, 0]
        pior = [1, 1, 1]
        for individuo in ensaio[i][j]:
            if individuo[0] > melhor[0]:
                melhor = individuo

            if individuo[0] < pior[0]:
                pior = individuo

        print(ensaio[i][j].__len__(), ensaio[i][j])
        print("melhor e pior")
        print(melhor, pior)
        nivel_diversidade = 0
        for k in range(24):
            nivel_diversidade += abs(int(melhor[1][0][k]) - int(pior[1][0][k]))
            nivel_diversidade += abs(int(melhor[1][1][k]) - int(pior[1][1][k]))
        print(nivel_diversidade)
