# AG: agente externo vs defesa disputando pela célula
import random

# alfabeto = list(range(-30,31))
# print(alfabeto, type(alfabeto[1]))

agente = []
defesas = []
fitness = []

# n_celulas = int(input("Entre com o numero de celulas: "))
tamanho_populacao = int(input("Entre com o tamanho da populacao: "))
n_caracteristicas = int(input("Entre com o numero de características da célula: "))
n_geracoes = int(input("Entre com o numero de geracoes: "))
taxa_cruz = int(input("Entre com a taxa de cruzamento: "))
taxa_mut = int(input("Entre com a taxa de mutacao: "))

for index in range(tamanho_populacao):
	random.seed()
	defesa = []

	for j in range(n_caracteristicas):
		defesa.append(random.randint(0, 10))

	defesas.append(defesa)

for index in range(len(defesas[0])):
	agente.append(random.randint(0, 10))

print('agente', '\n', agente, '\n')
print('defesas', '\n', defesas, '\n')

for geracao in range(n_geracoes):
	# fitness
	for index, elem in enumerate(defesas):

		fitness_defesa = 0

		for i, defesa in enumerate(elem):
			fitness_defesa += abs(defesa - agente[i])

		fitness.append([fitness_defesa, index])

	print("fitness: ", fitness)

	# selecao
	# for index, elem in enumerate(fitness):
	# 	print(elem)

	ranking = (sorted(fitness))
	print('ranking: ', ranking)

	n_cruzamentos = round(len(defesas)*taxa_cruz/100)
	if not n_cruzamentos == 0:
		# selecao = (ranking[0:n_cruzamentos])

		# print('selecao: ', selecao)

		# selecao dos individuos

		posicoes = []
		for index,elem in enumerate(ranking):
			posicoes.append(elem[1])

		pop_pais = []
		for i in posicoes:
			# print('posicao: ', i)
			# print(defesas[i])
			pop_pais.append(defesas[i])
		# print('posicoes: ', posicoes)
		print('selecao: ', pop_pais)

		melhor_individuo = pop_pais[0]

		# cruzamento: mascara binaria
		pop_filhos = []
		for i in range(len(pop_pais)):
			pop_filhos.append([])

		mascara = []
		for i in range(n_caracteristicas):
			random.seed()
			mascara.append(random.randint(0, 1))
		print('mascara: ', mascara)

		contador = 0
		while contador < n_cruzamentos:

			# print('contador: ', contador)

			for index, elem in enumerate(mascara):

				if elem == 0:
					pop_filhos[contador].append(pop_pais[contador][index])
					pop_filhos[contador+1].append(pop_pais[contador+1][index])
					# print(pop_filhos)

				else:
					pop_filhos[contador].append(pop_pais[contador + 1][index])
					pop_filhos[contador + 1].append(pop_pais[contador][index])
					# print(pop_filhos)

			contador += 2

		# defesas = []
		# defesas.append(pop_pais)
		# defesas.append(pop_filhos)
		for elem in pop_filhos:
			defesas.append(elem)
		print('defesas antigas + novas(filhos): ', defesas)

	# mutacao
	n_mutacoes = round(len(defesas)*taxa_mut/100)

	if not n_mutacoes == 0:
		for i in range(n_mutacoes):
			random.seed()
			defesa = random.choice(defesas)

			# print('defesa: ', defesa)
			locus = random.randint(0, n_caracteristicas -1)
			alelo = random.randint(0, 10)
			# print('locus, alelo: ',locus , alelo)

			defesa[locus] = alelo

		print('defesas + filhos (mutacoes): ', defesas)

	# fitness novamente
	for index, elem in enumerate(defesas):

		fitness_defesa = 0

		for i, defesa in enumerate(elem):
			fitness_defesa += abs(defesa - agente[i])

		fitness.append([fitness_defesa, index])

	print("fitness: ", fitness)

	ranking = (sorted(fitness))
	print('ranking: ', ranking)

	posicoes = []
	for index,elem in enumerate(ranking):
		posicoes.append(elem[1])

	pop_final_aux = []
	for i in posicoes:
		# print('posicao: ', i)
		# print(defesas[i])
		pop_final_aux.append(defesas[i])
	# print('posicoes: ', posicoes)
	print('pop_final_aux: ', pop_final_aux)

	posicoes = []

	defesas = pop_final_aux[0:tamanho_populacao]
	if not n_cruzamentos == 0:
		defesas.insert(0, melhor_individuo)
		defesas.pop(-1)
	else:
		fitness_melhor = 0

	print('')
	print('geracao: ', geracao)
	print('agente:  ', agente)
	print('defesas: ', defesas)
	fitness_melhor = 0
	for i, elem in enumerate(defesas[0]):
		fitness_melhor += abs(elem - agente[i])
	print(fitness_melhor)
	print('-------------')
