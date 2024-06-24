import sys
import time
from gerarVetor import VetorAleatorio
from gerarVetor import VetorInvertido

def partition(v: list[int], s: int, e: int) -> int:
    d = s - 1
    for j in range(s, e):
        if v[j] <= v[e]:
            d += 1
            v[j], v[d] = v[d], v[j]
    v[e], v[(d + 1)] = v[(d + 1)], v[e]
    return (d + 1)

def quickSort(v: list[int], s: int, e: int):
    if (s < e):
        p = partition(v, s, e)
        quickSort(v, s, (p - 1))
        quickSort(v, (p + 1), e)

if __name__ == "__main__":
    input = int(sys.argv[1])
    
    # para o caso medio tire o comentario da linha abaixo e comente os demais
    vetor = VetorAleatorio(input)

    # para o pior caso tire o comentario da linha abaixo e comente os demais
    # vetor = VetorInvertido(input)

    e = len(vetor) - 1
    start = time.time_ns()
    quickSort(vetor, 0, e)
    end = time.time_ns()
    final_time = end - start
    print(final_time)
