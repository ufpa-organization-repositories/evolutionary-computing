from random import random, seed

def calc_mutacao(pop_filhos):
    tm = 1
    for index, filho in enumerate(pop_filhos):
        seed(random() * random())

        # para a variavel x
        x = filho[0]
        for index_bit, bit in enumerate(x):

            # probabilidade de 1% de mutacao
            if not (bit == '-' or bit == '.'):
                if (random() * 100) <= tm:
                    x_aux = list(x)
                    if bit == '0':
                        x_aux[index_bit] = '1'
                    else:
                        x_aux[index_bit] = '0'
                    x_aux = ''.join(x_aux)
                    pop_filhos[index][0] = x_aux

        # para a variavel y
        y = filho[1]
        for index_bit, bit in enumerate(y):

            # probabilidade de 1% de mutacao
            if not (bit == '-' or bit == '.'):
                if (random() * 100) <= tm:
                    y_aux = list(y)
                    if bit == '0':
                        y_aux[index_bit] = '1'
                    else:
                        y_aux[index_bit] = '0'
                    y_aux = ''.join(y_aux)
                    pop_filhos[index][1] = y_aux

    return 0
# pop_filhos= [['1.11', '1.11'], ['0.00', '0.00'] ]
# calc_mutacao(pop_filhos)
# print(pop_filhos)