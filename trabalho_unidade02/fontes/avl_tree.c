#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct node {
    int value;
    unsigned int height;
    
    struct node* left;
    struct node* right;
    struct node* parent;
} Node;

int height(Node* node) {
    return (node == NULL) ? 0 : node->height;
}

int max(int a, int b) {
    return (a > b) ? a : b;
}

Node* create_node(int value) {
    Node* new_node = (Node*)malloc(sizeof(Node));

    new_node->value = value;
    new_node->height = 1;

    new_node->left = NULL;
    new_node->right = NULL;
    new_node->parent = NULL;

    return new_node;
}

int getBalance(Node* node) {
    return (node == NULL) ? 0 : height(node->left) - height(node->right); 
}

Node* find_root(Node* root) {
    if (root->parent != NULL) {
        return find_root(root->parent);
    } else {
        return root;
    }
}

void calculate_height(Node* root) {
    if (root != NULL) {
        root->height = 1 + max(height(root->left), height(root->right));
        calculate_height(root->parent);
    }
}

Node* rotate_left(Node* x) {
    Node* y = x->right;
    Node* C_TREE = y->left;

    y->left = x;
    x->right = C_TREE;

    y->parent = x->parent;
    x->parent = y;

    Node* parent = y->parent;
    if (parent != NULL) {
        if(parent->left == x) {
            parent->left = y;
        } else {
            parent->right = y;
        }   
    }

    if(C_TREE != NULL) {
        C_TREE->parent = x;
    }

    x->height = max(height(x->left), height(x->right)) + 1;
    y->height = max(height(y->left), height(y->right)) + 1;

    return y;
}

Node* rotate_right(Node* x) {
    Node* y = x->left;
    Node* C_TREE = y->right;

    y->right = x;
    x->left = C_TREE;

    y->parent = x->parent;
    x->parent = y;

    Node* parent = y->parent;
    if (parent != NULL) {
        if(parent->left == x) {
            parent->left = y;
        } else {
            parent->right = y;
        }   
    }

    if(C_TREE != NULL) {
        C_TREE->parent = x;
    }

    x->height = max(height(x->left), height(x->right)) + 1;
    y->height = max(height(y->left), height(y->right)) + 1;

    return y;
}

void balance_tree(Node* root) {
    int balance = getBalance(root);

    // Caso Esquerda-Esquerda (LL) ou Caso 01
    if(balance > 1 && getBalance(root->left) >= 0) {
        root = rotate_right(root);
    }

    // Caso Direita-Direita (RR) ou Caso 02
    if(balance < -1 && getBalance(root->right) <= 0) {
        root = rotate_left(root);
    }

    // Caso Esquerda-Direita (LR) ou Caso 03
    if(balance > 1 && getBalance(root->left) < 0) {      
        root->left = rotate_left(root->left);
        root = rotate_right(root);
    }

    // Caso Direita-Esquerda (RL) ou Caso 04
    if(balance < -1 && getBalance(root->right) > 0) {    
        root->right = rotate_right(root->right);
        root = rotate_left(root);
    }
}

void insert_node(Node** root, int value) {
    if ((*root) != NULL) {
        if((*root)->value > value) {
            insert_node(&(*root)->left, value);
            (*root)->left->parent = (*root);
        } else {
            insert_node(&(*root)->right, value);
            (*root)->right->parent = (*root);
        }
        
        calculate_height((*root));

        balance_tree((*root));
    } else {
        (*root) = create_node(value);
    }
}

Node* binary_search(Node* root, int number) {
    if (root != NULL) {
        if(root->value == number) {
            return root;
        }

        if(root->value > number) {
            return binary_search(root->left, number);
        }

        return binary_search(root->right, number);
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
    Node* root = NULL;

    unsigned int n = atoi(argv[1]);

    srand(time(NULL));

    int aux;
    for(int i = 0; i < n; i++) {
        aux = (rand() % (n*10)) + 1;
        insert_node(&root, aux);
        root = find_root(root);
    }

    struct timespec start, end;

    clock_gettime(CLOCK_MONOTONIC, &start);
    
    // pior caso
    // binary_search(root, 0);
    
    // caso médio
    binary_search(root, aux);
    
    // melhor caso
    // binary_search(root, root->value);

    clock_gettime(CLOCK_MONOTONIC, &end);

    unsigned time = (end.tv_sec * 1e9 + end.tv_nsec) - (start.tv_sec * 1e9 + start.tv_nsec);

    printf("%u\n", time);

    free_tree(&root);

    return 0;
}
