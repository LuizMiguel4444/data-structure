import sys
import time
from gerarVetor import VetorAleatorio

def distributionSort(vetor: list[int], n):
    maiorElemento = max(vetor)
    vetorAux = [0] * (maiorElemento + 1)
    vetorResultante = [0] * n

    for i in range(n):
        vetorAux[vetor[i]] += 1

    for i in range(1, maiorElemento + 1):
        vetorAux[i] += vetorAux[i - 1]

    for i in range(n - 1, -1, -1):
        vetorResultante[vetorAux[vetor[i]] - 1] = vetor[i]
        vetorAux[vetor[i]] -= 1

    for i in range(n):
        vetor[i] = vetorResultante[i]

if __name__ == "__main__":
    input = int(sys.argv[1])
    vetor = VetorAleatorio(input)
    n = len(vetor)
    start = time.time_ns()
    distributionSort(vetor, n)
    end = time.time_ns()
    final_time = end - start
    print(final_time)
