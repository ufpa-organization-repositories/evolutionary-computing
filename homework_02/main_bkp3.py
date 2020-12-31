# Algoritmo genético

from trabalho2.modules import calc_individuos, calc_populacao, calc_fitness, calc_fitness_filhos, calc_roletaSimplesProporcional, calc_pontoCorte, calc_mutacoes
from random import seed
len_pop = 100
num_simbolos = 3000000
print('Tamanho da populacao: ', len_pop)

list_individuos = calc_individuos(num_simbolos)
populacao = calc_populacao(list_individuos, len_pop)
fitness = []
roleta = []
pop_pais = []
pop_filhos = []
num_selecionados = 0
tc = 25
tm = 1

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

    n_mutacoes = int((tm / 100) * len(populacao))
    if n_mutacoes < 1:
        n_mutacoes = 1
    print('n_mutacoes: ', n_mutacoes)

    calc_mutacoes(populacao, n_mutacoes)

    calc_fitness(populacao)

    populacao = sorted(populacao, reverse=True)
    populacao = populacao[:len_pop]

    print("POPULACAO PARCIAL:")
    print(populacao)

print("----------------------------------")
print("populacao final:" + '\n')
print(populacao)