from random import *
populacao  = [[4,'a'],[3,'b'],[2,'c'],[1,'d']]
pop_pais = []
pop_filhos = []
roleta = []
num_selecionados = 4

# roleta simples
for i in range(num_selecionados):
    if i == 0:
        roleta.append(float("%.6f" %populacao[0][0]))
    else:
        roleta.append((float("%.6f" %roleta[i - 1]) + float("%.6f" %populacao[i][0])))

print(roleta)

tc = 2
index_selecionado = 0

for i in range(tc):
    seed()
    num_aleatorio = float("%.6f" % uniform(0,roleta[-1]))
    for index_roleta, elem in enumerate(roleta):
        if index_roleta == 0:
            index_selecionado = index_roleta
        else:
            if num_aleatorio > elem:
                index_selecionado = index_roleta + 1
    print('selecionado: ', index_selecionado)
    pop_pais.append(populacao[index_selecionado])

print(populacao)
print(pop_pais)