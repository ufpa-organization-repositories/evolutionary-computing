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
populacao = [['a','1.11111111111111111111'],['b','1.11111111111111111111'],['c','1.11111111111111111111'],['d','1.11111111111111111111']]
print(populacao)
tm = 1
n_mutacoes = 1
calc_mutacoes(populacao, n_mutacoes)
