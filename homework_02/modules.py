PRECISION_BINARY = 22
import math

def to_binary(number_dec):
    def to_bin_virg(number_dec):
        list_bin = []
        # number = float('0.' + number_dec)
        number = float("%.6f" % (float('0.' + number_dec)))
        for i in range(PRECISION_BINARY - 2):  # para deixar dois caracteres para o primeiro bit e o '.'
            number *= 2
            if number != 1:
                int_bin = int(number)
                list_bin.append(str(int_bin))
                number -= int_bin
            else:
                list_bin.append(str(int(number)))
                break
        return ''.join(list_bin)

    dec_split = str(number_dec).split('.')
    integer = bin(int(float("%.6f" %float(dec_split[0])))).replace('0b', '')
    if len(dec_split) == 1:  # possui apenas a parte inteira
        return integer
    elif len(dec_split) == 2:  # possui a parte inteira e a parte real
        floating = to_bin_virg(dec_split[1])
        result = integer + '.' + floating
        return result
    else:  # possui numero errado de virgulas para representar o numero
        raise Exception('Numero Decimal com mais de uma virgula')


def to_decimal(number_bin):
    def to_dec_virg(number):
        sum_n = 0
        for ind, value in enumerate(number):
            sum_n += int(value) * math.pow(2, -1 * (ind + 1))
        return sum_n

    split = str(number_bin).split('.')

    integer = int(split[0], 2)

    if len(split) == 1:
        return integer

    elif len(split) == 2:
        floating = to_dec_virg(split[1])
        result = integer + floating
        return result

    else:
        raise Exception('Numero binario com mais de uma virgula')

# binario = to_binary(2.01)

from trabalho2.modules import to_decimal, to_binary

global num_simbolos
def calc_individuos(num_individuos):
    list_individuos = []

    cromossomo = -1
    cromossomo = float("%.6f " % cromossomo)
    list_individuos.append(cromossomo)
    # simbolo_binario = to_binary(cromossomo)
    # list_individuos.append(simbolo_binario)
    print(cromossomo)
    # num_individuos = 3000000
    # num_individuos = 3000

    for i in range(num_individuos):
        # print('cromossomo: ', i)
        # cromossomo += 0.000001
        cromossomo += float("%.6f " % (3 / num_individuos))  # 3 porque o intervalo vai é [-1,2], ou seja, tem tamanho 3
        cromossomo = float("%.6f " % cromossomo)
        list_individuos.append(cromossomo)
        # simbolo_binario = to_binary(cromossomo)
        # list_individuos.append(simbolo_binario)
    print(cromossomo)
    # for simb in list_individuos:
    #     print(simb)

    for i in range(len(list_individuos)):
        list_individuos[i] = to_binary(list_individuos[i])

    return list_individuos

from random import choice, seed

# list_individuos = [1,2,3,4,5,6,7,8,9,10]
# len_pop = 4
global list_individuos
global len_pop

def calc_populacao(list_individuos, len_pop):
    populacao = []
    if len_pop > len(list_individuos):
        len_pop = len(list_individuos)

    if not len_pop % 2 == 0:
        len_pop += 1

    for i in range(round(len_pop)):
        seed()
        populacao.append(choice(list_individuos))

    return populacao

# populacao = calc_populacao(list_individuos, len_pop)
# print(populacao)

global populacao
from math import sin, pi
def calc_fitness(populacao):
    for index, individuo in enumerate(populacao):
        senoide = to_decimal(individuo) * sin(10 * pi * to_decimal(individuo)) + 1
        populacao[index] = [senoide, individuo] # maximo - obtido

    return 0
# calc_fitness(populacao)

global pop_filhos
from math import sin, pi
def calc_fitness_filhos(pop_filhos):
    for index, individuo in enumerate(pop_filhos):
        print('filho: ', index + 1)
        senoide = to_decimal(individuo) * sin(10 * pi * to_decimal(individuo)) + 1
        pop_filhos[index] = [senoide, individuo] # maximo - obtido

    return 0
# calc_fitness(pop_filhos)

from random import *

global pop_pais
global populacao
global num_selecionados
global tc
# roleta simples
def calc_roletaSimplesProporcional(populacao, num_selecionados):
    pop_pais = []
    roleta = []

    for i in range(len(populacao)):
        if i == 0:
            roleta.append(float("%.6f" %populacao[0][0]))
        else:
            roleta.append((float("%.6f" %roleta[i - 1]) + float("%.6f" %populacao[i][0])))

    # print("roleta: ", roleta)

    index_selecionado = 0

    for i in range(num_selecionados):
        seed(i)
        num_aleatorio = float("%.6f" % uniform(0,roleta[-1]))
        for index_roleta, elem in enumerate(roleta):
            if index_roleta == 0:
                index_selecionado = index_roleta
            else:
                if num_aleatorio > elem:
                    index_selecionado = index_roleta + 1
        # print('selecionado: ', index_selecionado)
        pop_pais.append(populacao[index_selecionado])

    pop_pais = sorted(pop_pais, reverse=True)
    # print("populacao: ", populacao)
    print("pop_pais: ", pop_pais)
    return pop_pais

# populacao  = [[4,'a'],[3,'b'],[2,'c'],[1,'d']]
# pop_pais = []
# tc = 50
# num_selecionados = round((tc/100)*len(populacao))

# calc_roletaSimplesProporcional(populacao,pop_pais,num_selecionados)

from trabalho2.modules import to_decimal, to_binary, calc_fitness

global pop_pais
global num_selecionados

def calc_pontoCorte(pop_pais, num_selecionados):
    pop_filhos = []
    # i_pontoCorte = len(to_binary(0.25))# indice do ponto de corte na lista
    # print("i_pontoCorte: ", i_pontoCorte, end=' ou ' + to_binary(0.25) + '\n')
    i_pontoCorte = randrange(1, len(pop_pais[0][1]))
    print("i_pontoCorte: ", i_pontoCorte)

    i_pai = 0
    # o -1 é porque a contagem comeca no zero e vai ate o num_selecionados -1
    print('Total de cruzamentos: ', num_selecionados/2)
    while i_pai < num_selecionados - 1:
        # print(i_pai)
        # print(i_pai + 1)
        pai1 = pop_pais[i_pai][1]
        pai2 = pop_pais[i_pai + 1][1]

        filho1 = pai1[:i_pontoCorte] + pai2[i_pontoCorte:]
        filho2 = pai2[:i_pontoCorte] + pai1[i_pontoCorte:]
        pop_filhos.append(filho1)
        pop_filhos.append(filho2)
        # print('-------')
        i_pai += 2

    print("pop_pais: ", pop_pais)
    print("pop_filhos: ", pop_filhos)
    return pop_filhos

# pop_pais = [[2.647763334125383, '1.11111111111111111111'], [2.5674295261434503, '0.00000000000000000000'], [1.8389310236892902, '1.11111111111111111111'], [1.6476602390566724, '0.00000000000000000000']]
# num_selecionados = 4
# pop_filhos = calc_pontoCorte(pop_pais, num_selecionados)

from random import seed, randrange

global populacao
global n_mutacoes

def calc_mutacoes(populacao, n_mutacoes):
    for i in range(n_mutacoes):
        seed()
        i_individuo = randrange(0, len(populacao))
        i_gene = 1 # caso do ponto da casa decimal
        while i_gene == 1:
            i_gene = randrange(0, len(populacao[0][1]))

        print('individuo: ', i_individuo)
        print('gene: ', i_gene)

        #mutacao: troca de bit
        bit = int
        print('bit: ', populacao[i_individuo][1][i_gene])
        if populacao[i_individuo][1][i_gene] == '0':
            bit = '1'
        else:
            bit = '0'

        individuo_aux = list(populacao[i_individuo][1])
        individuo_aux[i_gene] = bit
        individuo_aux = ''.join(individuo_aux)
        populacao[i_individuo] = individuo_aux

        for i in range(len(populacao)):
            if len(populacao[i]) == 2:
                populacao[i] = populacao[i][1]

    print(populacao)

    return print("Mutações realizadas")
# populacao = [['a','1.11111111111111111111'],['b','1.11111111111111111111'],['c','1.11111111111111111111'],['d','1.11111111111111111111']]
# print(populacao)
# tm = 1
# n_mutacoes = 1
# calc_mutacoes(populacao, n_mutacoes)
