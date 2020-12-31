import random


tamanho_populacao = 8
taxa_cruz = int(input("Entre com a taxa de cruzamento: "))
# n_cruzamentos = round(len(defesas)*taxa_cruz/100)
n_cruzamentos = round(8*taxa_cruz/100)
print('n_cruzamentos: ', n_cruzamentos)
mascara = []
n_caracteristicas = 2

for i in range(n_caracteristicas):
	random.seed()
	mascara.append(random.randint(0, 1))
print('mascara: ', mascara)

defesas = [[1,2], [3,4], [5,6], [7,8], [4,9], [5,8], [3,7], [0,4]]
agente = [6,5]
print(defesas)
print(agente)

# considerando que toda a populacao vai cruzar
pop_pais = [[1,2], [3,4], [5,6], [7,8], [4,9], [5,8], [3,7], [0,4]]

pop_filhos = []
#cruzamento
for i in range(len(pop_pais)):
    pop_filhos.append([])

print('tamanho_populacao: ', tamanho_populacao)

contador = 0
while contador < n_cruzamentos:

    print('contador: ', contador)

    for index, elem in enumerate (mascara):

        if elem == 0:
            pop_filhos[contador].append(pop_pais[contador][index])
            pop_filhos[contador+1].append(pop_pais[contador+1][index])
        else:
            pop_filhos[contador].append(pop_pais[contador +1][index])
            pop_filhos[contador + 1].append(pop_pais[contador][index])

    contador += 2
for elem in pop_filhos:
    defesas.append(elem)
print(pop_filhos)
print(defesas)

# calcula a fitness do populacao + filhos
fitness = []
for index, elem in enumerate(defesas):

	fitness_defesa = 0

	for i, defesa in enumerate(elem):
		fitness_defesa += abs(defesa - agente[i])

	fitness.append([fitness_defesa, index])

print("fitness: ", fitness)

# selecao

for index, elem in enumerate(fitness):
    print(elem)

ranking = (sorted(fitness))
print('ranking: ', ranking)


selecao = (ranking[0:int(tamanho_populacao/2)])

print('selecao: ', selecao)
