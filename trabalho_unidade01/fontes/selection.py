import sys
import time
from gerarVetor import VetorAleatorio

def selectionSort(vetor: list[int], n: int):
    for i in range(0, (n - 1)):
        m = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[m]:
                m = j
        vetor[i], vetor[m] = vetor[m], vetor[i]

if __name__ == "__main__":
    input = int(sys.argv[1])
    vetor = VetorAleatorio(input)
    n = len(vetor)
    start = time.time_ns()
    selectionSort(vetor, n)
    end = time.time_ns()
    final_time = end - start
    print(final_time)
