from random import randint

# pior caso arvore


def sortv(n):
    vetor = []
    for i in range(1, n):
        vetor.append(i)
    return vetor


# caso médio arvore e avl

def randv(n):
    vetor = []
    for _ in range(n):
        new_value = 0
        while new_value == 0 or new_value in vetor:
            new_value = randint(1, 100000)
        vetor.append(new_value)
    return vetor


def parv(n):
    vetor = []
    for i in range(2, n, 2):
        vetor.append(i)
    return vetor
