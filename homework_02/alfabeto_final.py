# from trabalho2.floatToBin_bugada import floatToBin

from trabalho2.modules import to_decimal, to_binary
def calc_alfabeto():
    alfabeto = []

    simbolo = -1
    simbolo = float("%.6f " % simbolo)
    alfabeto.append(simbolo)
    # simbolo_binario = to_binary(simbolo)
    # list_individuos.append(simbolo_binario)
    print(simbolo)
    num_simbolos = 3000000
    # num_individuos = 3000



    for i in range(num_simbolos):
        # print('simbolo: ', i)
        # simbolo += 0.000001
        simbolo += float("%.6f " % (3/num_simbolos)) # 3 porque o intervalo vai é [-1,2], ou seja, tem tamanho 3
        simbolo = float("%.6f " % simbolo)
        alfabeto.append(simbolo)
        # simbolo_binario = to_binary(simbolo)
        # list_individuos.append(simbolo_binario)
    print(simbolo)
    # for simb in list_individuos:
    #     print(simb)

    for i in range(len(alfabeto)):
        alfabeto[i] = to_binary(alfabeto[i])

    return alfabeto