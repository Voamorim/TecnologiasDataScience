from random import randint, uniform 

# parte 1

aluno = {}
aluno["nome"] = "Leonardo"
aluno["idade"] = randint(12, 80)
aluno["notas"] = [uniform(3.0, 10.0) for i in range(0, 10)]

print(aluno)

# parte 2

def func(dicionario: dict):
    notas = 0.0

    for nota in dicionario["notas"]:
        notas += nota
    
    notas /= len(dicionario["notas"])
    return notas

print(f"media: {func(aluno)}")
