from numpy import linspace
binario = []
real = []
precisao = 0.1
valor = 10
n_elementos = int(valor / precisao)
print(n_elementos)
print(linspace(-100,100,n_elementos).__len__())
reais = linspace(-100,100,n_elementos)
aux = 0
i = -100
lista = []
for cont in range(n_elementos):
    aux = float("%.5f" % aux)
    lista.append([i, aux])
    i += 1
    aux += precisao

print(i)


# lista = dict([[1,2],[3,4]])
# print(lista)

d = dict(lista)
print(d)
