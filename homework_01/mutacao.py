# mutacao
import random
defesas = [[1,2,3], [4,5,6]]
n_caracteristicas = 3
taxa_mut = int(input("Entre com a taxa de mutacao"))
n_mutacoes = round(len(defesas)*taxa_mut/100)
print(len(defesas)*taxa_mut/100)
print(n_mutacoes)

defesas_alteradas = []

for i in range(n_mutacoes):
    random.seed()
    # print('defesa ', i)
    defesa = random.choice(defesas)

    print('defesa: ', defesa)
    locus = random.randint(0, n_caracteristicas -1)
    alelo = random.randint(0, 10)
    print('locus, alelo: ',locus , alelo)

    # defesas[i][locus] = alelo
    defesa[locus] = alelo

print(defesas)


