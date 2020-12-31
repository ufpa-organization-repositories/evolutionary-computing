# Algoritmo genético

from trabalho2.modules import calc_individuos, to_binary, to_decimal, calc_populacao
len_pop = 30
num_simbolos = 3000

list_individuos = calc_individuos(num_simbolos)
populacao = calc_populacao(list_individuos, len_pop)
fitness = []
roleta = []
pop_pais = []
num_selecionados = 0
tc = 99
tm = 10

from math import  sin, pi
# global fitness
def calc_fitness(populacao, fitness):
    for index, individuo in enumerate(populacao):
        senoide = to_decimal(individuo) * sin(10 * pi * to_decimal(individuo)) + 1
        # fitness.append(2.85 - abs(senoide)) # maximo - obtido
        # populacao[index] = [(2.85 - abs(senoide)), individuo] # maximo - obtido
        populacao[index] = [(abs(senoide)), individuo] # maximo - obtido

    return 0

calc_fitness(populacao, fitness)

for geracao in range(150):
    print("------------------")
    print("Geracao: ", geracao)

# selecao: roleta simples
populacao = sorted(populacao, reverse=True) # ordenando a populacao pela fitness

num_selecionados = round((tc/100)*len_pop)
if not num_selecionados % 2 == 0:
    num_selecionados +=1
