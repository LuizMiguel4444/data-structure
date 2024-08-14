import random
import sys
import time

import vetores


class HashTable:
    def __init__(self):

        self.size = 1
        self.table = [[]]

    def _hash_function(self, key):
        return key % self.size

        # pior caso

        # return 0

    def _re_hash(self):
        self.size = self.size * 2
        old_table = self.table
        self.table = [[] for _ in range(self.size)]
        for item in old_table:
            if item:
                if len(item) > 1:
                    for i in item:
                        self.insert(i)
                else:
                    self.insert(item[0])

    def insert(self, value):

        if len(self.table[self._hash_function(value)]) >= self.size:
            self._re_hash()

        self.table[self._hash_function(value)].append(value)

    def search(self, value):
        index = self._hash_function(value)
        if self.table[index]:
            for item in self.table[index]:
                if item == value:
                    return True
        return False


if __name__ == "__main__":

    n = int(sys.argv[1])
    # pior caso
    vet = vetores.sortv(n)
    # melhor caso
    # vet = vetores.parv(n)
    # caso medio
    # vet = vetores.randv(n)
    hasht = HashTable()
    for i in vet:
        hasht.insert(i)

    start = time.time_ns()
    # caso medio
    hasht.search(random.randint(1, 100000))
    # pior caso
    # hasht.search(n + 1)
    # melhor caso
    # hasht.search(2)
    end = time.time_ns()
    final_time = end - start
    print(final_time)
