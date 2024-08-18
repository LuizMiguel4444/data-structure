#include <stdlib.h>
#include <stdio.h>
#include <time.h>

struct node {
    int value;
    struct node* next;
};

struct hash_table {
    struct node** table;
    unsigned int size;
    unsigned int n;
};

struct hash_table* createHashTable(int size) {
    struct hash_table* hashTable = (struct hash_table*)malloc(sizeof(struct hash_table));

    hashTable->size = size;
    hashTable->n = 0;
    hashTable->table = (struct node**)malloc(sizeof(struct node*) * size);

    for (int i = 0; i < size; i++) {
        hashTable->table[i] = NULL;
    }

    return hashTable;
}

int hashFunction(int key, int size) {
    return key % size;
}

float loadFactor(struct hash_table* hashTable) {
    return (float)hashTable->n / hashTable->size;
}

struct node* create_node(int value) {
    struct node* node = (struct node*)malloc(sizeof(struct node));

    node->value = value;
    node->next = NULL;

    return node;
}

void rehash(struct hash_table* hashTable) {
    int oldSize = hashTable->size;
    int newSize = oldSize * 2;
    struct node** oldTable = hashTable->table;

    hashTable->size = newSize;
    hashTable->table = (struct node**)malloc(sizeof(struct node*) * newSize);

    for (int i = 0; i < newSize; i++) {
        hashTable->table[i] = NULL;
    }

    for (int i = 0; i < oldSize; i++) {
        struct node* item = oldTable[i];
        while (item != NULL) {
            struct node* next = item->next;
            int index = hashFunction(item->value, newSize);
            item->next = hashTable->table[index];
            hashTable->table[index] = item;
            item = next;
        }
    }

    free(oldTable);
}

void insert(struct hash_table* hashTable, int value) {
    if (loadFactor(hashTable) >= 1.0) {
        rehash(hashTable);
    }

    int index = hashFunction(value, hashTable->size);

    struct node* newNode = (struct node*)malloc(sizeof(struct node));
    newNode->value = value;
    newNode->next = NULL;

    if (hashTable->table[index] == NULL) {
        hashTable->table[index] = newNode;
    } else {
        struct node* current = hashTable->table[index];
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newNode;
    }

    hashTable->n++;
}

unsigned int hash(int value, int m) {
    return value % m < 0 ? (value % m) + m : value % m;
}

void insert_worst(struct hash_table* hashTable, int value) {
    unsigned int key = hash(value, hashTable->size);

    // Como ser é o pior caso, então não há o rehash.
    if(1) {
        unsigned int index = hash(key, hashTable->size);

        struct node* new_node = create_node(value);

        if(hashTable->table[index] == NULL) {
            hashTable->table[index] = new_node;
        } else {
            struct node* index_node = hashTable->table[index];
            while(index_node->next != NULL) {
                index_node = index_node->next;
            }
            index_node->next = new_node;
        }

        hashTable->n++;

    } else {
        rehash(hashTable);
        insert_worst(hashTable, value);
    }
}

int search(struct hash_table* hashTable, int key) {
    int index = hashFunction(key, hashTable->size);
    struct node* item = hashTable->table[index];
    
    while (item != NULL) {
        if (item->value == key) {
            return 1;
        }
        item = item->next;
    }

    return 0;
}

void delete_table(struct hash_table* hashTable) {
    for(int i=0; i < hashTable->size; i++) {
        struct node* current_node = hashTable->table[i];

        while(current_node != NULL) {
            struct node* aux_node = current_node;
            current_node = current_node->next;
            free(aux_node);
        }
    }

    free(hashTable->table);
    free(hashTable);
}

int main(int argc, char **argv) {
    struct timespec end, start;
    unsigned int t, n;
    
    n = atoi(argv[1]);

    // caso médio
    struct hash_table* hashTable = createHashTable(n);

    // pior caso
    // struct hash_table* hashTable = createHashTable(1);

    srand(time(NULL));

    int aux;
    for (int i = 0; i < n; i++) {
        aux = (rand() % (n * 10)) + 1;

        // caso médio
        insert(hashTable, aux);

        // pior caso
        // insert_worst(hashTable, aux);
    }

    clock_gettime(CLOCK_MONOTONIC, &start);
    search(hashTable, aux);
    clock_gettime(CLOCK_MONOTONIC, &end);

    t = (end.tv_sec * 1e9 + end.tv_nsec) - (start.tv_sec * 1e9 + start.tv_nsec);

    printf("%u\n", t);

    delete_table(hashTable);

    return 0;
}
