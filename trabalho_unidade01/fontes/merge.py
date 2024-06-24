import sys
import time
from gerarVetor import VetorAleatorio

def merge(v: list[int], s: int, m: int, e: int) -> list[int]:
    i = s
    j = m + 1
    w: list[int] = []
    for k in range(0, (e - s + 1)):
        if (j > e) or ((i <= m) and (v[i] < v[j])):
            w.append(v[i])
            i += 1
        else:
            w.append(v[j])
            j += 1
    for k in range(0, (e - s + 1)):
        v[(s + k)] = w[k]

def mergeSort(v: list[int], s: int, e: int) -> list[int]:
    if (s < e):
        m: int = (s + e) // 2
        mergeSort(v, s, m)
        mergeSort(v, (m + 1), e)
        merge(v, s, m, e)

if __name__ == "__main__":
    input = int(sys.argv[1])
    vetor = VetorAleatorio(input)
    e = len(vetor) - 1
    start = time.time_ns()
    mergeSort(vetor, 0, e)
    end = time.time_ns()
    final_time = end - start
    print(final_time)
