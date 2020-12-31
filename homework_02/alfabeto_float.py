# list_individuos em inteiro
list_individuos = []

simbolo = -1
simbolo = float("%.6f " % simbolo)
list_individuos.append(simbolo)
print(simbolo)
num_simbolos = 3000000


for i in range(num_simbolos):
    simbolo += 0.000001
    simbolo = float("%.6f " % simbolo)
    list_individuos.append(simbolo)
print(simbolo)
# for simb in list_individuos:
#     print(simb)
#     print(bin(simb))

