import numpy as np
import csv
w = csv.writer(open("dicionario_teste.csv", "w"))

import pickle
from time import sleep
file = open('dicionario_teste.pkl', 'wb')

lista = []
dicionario = {}

precisao = 0.00001
valor = 201
n_elementos = round(valor / precisao)

print(n_elementos)
# n_elementos = int(0b111111111111111111111111)


print(np.linspace(start=0, stop=3, num=n_elementos).__len__())
# n_elementos = 201
reais = np.linspace(start=-100, stop=100, num=n_elementos + 1)
contador = 0
for i, elem in enumerate(reais):
    contador += 1
    if contador == 100000:
        print('restam: ', n_elementos - i)
        sleep(0.000000001)
        contador = 0


    # real = float("%.5f" % elem)
    real = round(elem, 5)
    binario = bin(i)
    binario = binario[2:].zfill(24)
    # binario = '{:0>25}'.format(binario)
    # lista.append([binario, real])

    w.writerow([binario, real])
    dicionario.update({binario:real})

# print('convertendo a lista para dicionários')
# dicionario = dict(lista)

# for elem in dicionario.items(): print(elem)

pickle.dump(dicionario, file)
file.close()

print(dicionario["000000000000000000000000"])
print(dicionario["111111111111111111111111"])