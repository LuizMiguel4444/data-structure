import sys
import time
from gerarVetor import VetorAleatorio
from gerarVetor import VetorInvertido
from gerarVetor import VetorOrdenado

def insertionSort(vetor: list[int], n):
    for i in range(1, n):
        x = i
        while (x > 0) and vetor[x - 1] > vetor[x]:
            vetor[x], vetor[x - 1] = vetor[x - 1], vetor[x]
            x -= 1

if __name__ == "__main__":
    input = int(sys.argv[1])

    # para o caso medio use a linha abaixo e comente as demais
    vetor = VetorAleatorio(input)

    # para o pior caso tire o comentario da linha abaixo e comente as demais
    # vetor = VetorInvertido(input)

    # para o melhor caso tire o comentario da linha abaixo e comente as demais
    # vetor = VetorOrdenado(input)

    n = len(vetor)
    start = time.time_ns()
    insertionSort(vetor, n)
    end = time.time_ns()
    final_time = end - start
    print(final_time)
