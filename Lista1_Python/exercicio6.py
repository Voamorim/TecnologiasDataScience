from random import randint

soma_lambda = lambda a, b: a + b

x = randint(0, 100)
y = randint(0, 100)

print(f"resultado da soma por funcao lambda: {soma_lambda(x, y)}")

# parte 1

mult3_lambda = lambda a: 3.0 * a

x = randint(0, 100)

print(f'numero: {x}, seu triplo por lambda: {mult3_lambda(x)}')

# parte 2

ehPar = lambda a: a % 2 == 0

lista = [randint(0, 100) for i in range(100)]
teste = list(filter(ehPar, lista))

print('lista: ', lista)
print('resultado: ', teste)

resultado = list(map(lambda a: 2.0 * a, lista))

print('lista: ', lista)
print('resultado dobro: ', resultado)
