from random import randint

def VetorAleatorio(n):
    vetor = []
    for i in range(0, n):
        vetor.append(randint(1, 10000))
    return vetor

def VetorInvertido(n):
    vetor = []
    for i in range(n, -1, -1):
        vetor.append(i)
    return vetor

def VetorOrdenado(n):
    vetor = []
    for i in range(n):
        vetor.append(i)
    return vetor
