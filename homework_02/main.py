# Algoritmo genético

from trabalho2.modules import calc_individuos, calc_populacao, calc_fitness, calc_fitness_filhos, calc_roletaSimplesProporcional, calc_pontoCorte, calc_mutacoes
from random import seed
from matplotlib import pyplot as plt
import numpy as np
len_pop = 100
num_individuos = 3000000
print('Tamanho da populacao: ', len_pop)

list_individuos = calc_individuos(num_individuos)
populacao = calc_populacao(list_individuos, len_pop)
fitness = []
roleta = []
pop_pais = []
pop_filhos = []
num_selecionados = 0
tc = 25
tm = 1

fitness_melhores = []
fitness_media = []

print('Taxa de cruzamento: ', tc, " %")
print('Taxa de mutacao: ', tm, " %")

calc_fitness(populacao)

for geracao in range(150):
    seed()
    print("------------------")
    print("Geracao: ", geracao)

    # ordenando a populacao pela fitness
    populacao = sorted(populacao, reverse=True)

    # define o numero de individuos da populacao de pais
    num_selecionados = int((tc/100)*len_pop)

    if num_selecionados < 2:
        num_selecionados = 2

    if not num_selecionados % 2 == 0:
        num_selecionados +=1

    # define a populacao de pais
    pop_pais = calc_roletaSimplesProporcional(populacao,num_selecionados)

    # cruzamento
    pop_filhos = calc_pontoCorte(pop_pais,num_selecionados)

    calc_fitness_filhos(pop_filhos)

    for filho in pop_filhos:
        populacao.append(filho)

    #elitismo
    populacao = sorted(populacao, reverse=True)
    melhor_individuo = populacao[0]

    n_mutacoes = int((tm / 100) * len(populacao))
    if n_mutacoes < 1:
        n_mutacoes = 1
    print('n_mutacoes: ', n_mutacoes)

    calc_mutacoes(populacao, n_mutacoes)

    calc_fitness(populacao)

    populacao = sorted(populacao, reverse=True)

    # elitismo
    populacao.insert(0, melhor_individuo)

    populacao = populacao[:len_pop]

    print("POPULACAO PARCIAL:")
    print(populacao)

    fitness_melhores.append(populacao[0][0])

    fitness_media_temp = 0
    for elem in populacao:
        fitness_media_temp += elem[0]

    fitness_media.append(fitness_media_temp/len_pop)

print("----------------------------------")
print("populacao final:" + '\n')
print(populacao)

#grafico: fitness do melhor ao longo das geracoes
x = np.arange(0, len(fitness_melhores), 1)
y = fitness_melhores
fig, ax = plt.subplots()
ax.plot(x, y)
fig.suptitle('Fitness do melhor individuo por geração')  # Add a title so we know which it is
plt.show()

#grafico: fitness media
x = np.arange(0, len(fitness_media), 1)
y = fitness_media
fig, ax = plt.subplots()
ax.plot(x, y)
fig.suptitle('Fitness do média da população por geração')  # Add a title so we know which it is
plt.show()
