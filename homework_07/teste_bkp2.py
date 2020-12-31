from numpy import linspace
binarios = []
reais = []
precisao = 0.00001
valor = 201
n_elementos = int(valor / precisao)
dicionario = {}
print(n_elementos)
lista = []
print(linspace(start=-100, stop=100, num=n_elementos).__len__())
lens = []
for i, elem in enumerate(linspace(-100, 100, n_elementos)):
    print(n_elementos - i)
    real = ("%.5f" % elem)
    binario = bin(i)
    lens.append(len(binario))
    lista.append([binario[2:], real])

dicionario = dict(lista)
lens.sort(reverse=True)
print(lens)

print(dicionario.values())
print(dicionario.keys)

for elem in dicionario.items():
    print(elem)