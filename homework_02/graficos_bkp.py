from matplotlib import pyplot as plt
import numpy as np
fitness_melhor = []


# fig = plt.figure()  # an empty figure with no axes
# fig.suptitle('No axes on this figure')  # Add a title so we know which it is
#
# fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
# print('')
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