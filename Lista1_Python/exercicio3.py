from random import uniform

# parte 1

dicionario = dict()
dicionario["notas"] = [uniform(0.0, 10.0) for i in range(0, 10)]

print("antes: ", dicionario)

copia = dicionario.copy()

for i in range(len(copia["notas"])):
    copia["notas"][i] = uniform(0.0, 10.0)

print("depois: ")

print(dicionario)
print(copia)

print(f'media dicionario: {sum(dicionario["notas"]) / len(dicionario["notas"])}')
print(f'media copia: {sum(copia["notas"]) / len(copia["notas"])}')

