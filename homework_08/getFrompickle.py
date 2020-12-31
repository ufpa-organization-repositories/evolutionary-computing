import pickle
dicionario = pickle.load(open("dicionario_final.pkl", "rb"))
print(dicionario["000000000000000000000000"])
print(dicionario["111111111111111111111111"])

# print(len(dicionario))

# for key,val in dicionario.items():
#     print(key, val)
#     break

