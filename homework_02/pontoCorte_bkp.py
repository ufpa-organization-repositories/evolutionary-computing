from trabalho2.modules import to_decimal, to_binary, calc_fitness
from random import *
num_selecionados = 4
# pop_pais = [[2.647763334125383, '1.10100111000000100110'], [2.5674295261434503, '1.10101001001001001111'], [1.8389310236892902, '0.11011011010000000100'], [1.6476602390566724, '0.10100110000000000010']]
pop_pais = [[2.647763334125383, '1.11111111111111111111'], [2.5674295261434503, '0.00000000000000000000'], [1.8389310236892902, '1.11111111111111111111'], [1.6476602390566724, '0.00000000000000000000']]

pop_filhos = []
# i_pontoCorte = randrange(0, len(pop_pais[0][1]))
i_pontoCorte = len(to_binary(0.25) )# indice do ponto de corte na lista
print("i_pontoCorte: ", i_pontoCorte, end=' ou ' + to_binary(0.25))

i_pai = 0
# o -1 é porque a contagem comeca no zero e vai ate o num_selecionados -1
while i_pai < num_selecionados - 1:
    print( (i_pai) )
    print( (i_pai + 1))
    pai1 = pop_pais[i_pai][1]
    pai2 = pop_pais[i_pai + 1][1]
    # pop_filhos.append(pop_pais[i_pai][1][:i_pontoCorte])
    # pop_filhos.append(aux_pai[1][i_pontoCorte :])
    filho1 = [pai1[:i_pontoCorte] + pai2[i_pontoCorte:]]
    filho2 = [pai2[:i_pontoCorte] + pai1[i_pontoCorte:]]
    pop_filhos.append(filho1)
    pop_filhos.append(filho2)
    print('-------')
    i_pai += 2

print("pop_pais: ", pop_pais)
print("pop_filhos: ", pop_filhos)