from random import choice, seed, randint

# list_individuos = [1,2,3,4,5,6,7,8,9,10]
# len_pop = 4
global list_individuos
global len_pop

def calc_populacao(alfabeto, len_pop):
    populacao = []
    if len_pop >= 3000000:
        len_pop = 3000000

    if not len_pop % 2 == 0:
        len_pop += 1

    for i in range(round(len_pop)):
        seed()
        populacao.append(choice(alfabeto))

    return populacao

# populacao = calc_populacao(list_individuos, len_pop)
# print(populacao)