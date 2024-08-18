#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct node {
    int value;
    struct node* left;
    struct node* right;
} Node;

Node* create_node(int value) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->value = value;
    new_node->left = NULL;
    new_node->right = NULL;
    return new_node;
}

void insert(Node **root, int value)
{
    if ((*root) == NULL)
    {   
        (*root) = create_node(value);
    }

    else
    {
        if ((*root)->value > value){
            insert(&((*root)->left), value);
        }

        else{
            insert(&((*root)->right), value);
        }
    }
}

Node* search(Node* root, int number)
{
    if (root != NULL) {
        if (root->value == number){
            return root;
        }
        
        else if (number < root->value) {
            return search(root->left, number);
        
        }
        return search(root->right, number);
    }

    return NULL;
}

void free_tree(Node** root) {
    if ((*root) != NULL) {
        free_tree(&(*root)->left);
        free_tree(&(*root)->right);
        free((*root));
    }
}

int main(int argc, char **argv) {
    struct timespec end, start;
    unsigned int t, n;
    Node* root = NULL;

    n = atoi(argv[1]);
    srand(time(NULL));

    // melhor caso
    // int aux = (rand() % n) + 1;
    // insert(&root, aux);
    // for (int i = 1; i < n; i++) {
    //     int value = (rand() % n) + 1;
    //     insert(&root, value);
    // }

    // caso médio
    int aux;
    for (int i = 0; i < n; i++){
        aux = (rand() % n) + 1;
        insert(&root, aux);
    }

    // pior caso
    // int aux = n + 1;
    // for(int i = 0; i < n; i++) {
    //     insert(&root, i);
    // }

    clock_gettime(CLOCK_MONOTONIC, &start);

    search(root, aux);
    
    clock_gettime(CLOCK_MONOTONIC, &end);

    t = (end.tv_sec * 1e9 + end.tv_nsec) - (start.tv_sec * 1e9 + start.tv_nsec);

    printf("%u\n", t);

    free_tree(&root);

    return 0;
}
