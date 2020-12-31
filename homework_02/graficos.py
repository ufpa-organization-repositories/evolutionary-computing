from matplotlib import pyplot as plt
import numpy as np
fitness_melhor = []

populacao = [[2.85, 'a'], [2.84, 'b'], [2.6, 'c'], [2.3, 'd']]
melhor_individuo = populacao[0][0]
fitness_melhor.append(populacao[0][0])

for i in range(len(populacao)):
    melhor_individuo = populacao[0][0]
    fitness_melhor.append(populacao[0][0])

x = np.arange(0, len(fitness_melhor), 1)
y = fitness_melhor
fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()