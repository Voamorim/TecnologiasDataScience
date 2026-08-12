import random

# parte 1

numeros = []
for i in range(100):
    number = random.randint(0, 1000)
    numeros.append(number)

for i in numeros:
    if i & 1:
        continue
    print(i, end=' ')
print('')

# parte 2

def func(lista: list):
    maximo = -10000000000

    for num in lista:
        maximo = maximo if maximo > num else num

    return maximo

print(f'maximo da lista: {func(numeros)}')
