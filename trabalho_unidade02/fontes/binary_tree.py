import random
import sys
import time

import vetores


class Node:
    def __init__(self, key=None,
                 left=None,
                 right=None,
                 parent=None,
                 height=1) -> None:

        self.key = key
        self.right = right
        self.left = left
        self.parent = parent
        self.height = height

    def __str__(self):
        return f'{self.key}'


class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        newnode = Node(key=value)
        self.__recursive_insert(root=self.root, value=newnode)

    def __recursive_insert(self, root, value):

        if self.root is None:

            self.root = value

        else:
            value.parent = root
            if root.key < value.key:
                if root.right is None:
                    root.right = value
                else:
                    self.__recursive_insert(root.right, value)
                self.__balance(root)

            else:
                if root.left is None:
                    root.left = value
                else:
                    self.__recursive_insert(root.left, value)

                self.__balance(root)
            root.height = self.__max_child(root)

    def print_tree(self):
        self.__recursive_print(self.root)

    def __recursive_print(self, root):
        if root is not None:
            self.__recursive_print(root.left)
            print(root.key)
            self.__recursive_print(root.right)

    def ascending_order(self):
        self.__ascending_order(self.root)

    def __ascending_order(self, root):
        if root is not None:
            self.__ascending_order(root.left)
            print(root.key)
            self.__ascending_order(root.right)

    def decreasing_order(self):
        self.__decreasing_order(self.root)

    def __decreasing_order(self, root):
        if root is not None:
            self.__decreasing_order(root.right)
            print(root.key)
            self.__decreasing_order(root.left)

    def search(self, key):
        self.__recursive_search(root=self.root, key=key)

    def __recursive_search(self, root, key):

        if root is None:
            return False

        elif root.key == key:
            return True

        elif root.key < key:
            return self.__recursive_search(root.right, key)
        else:
            return self.__recursive_search(root.left, key)

    def __max_child(self, node: Node):
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0
        return max(left_height, right_height) + 1

    def __balance_factor(self, node):

        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0
        return left_height - right_height

    def __balance(self, node):
        if node is None:
            return

        self.__balance(node.left)
        self.__balance(node.right)
        balance_factor = self.__balance_factor(node)
        if balance_factor > 1:
            if self.__balance_factor(node.left) < 0:
                self.__left_rotation(node.left)
            self.__right_rotation(node)
        elif balance_factor < -1:
            if self.__balance_factor(node.right) > 0:
                self.__right_rotation(node.right)
            self.__left_rotation(node)

    def __left_rotation(self, node):
        pivot = node.right
        node.right = pivot.left
        if pivot.left:
            pivot.left.parent = node
        pivot.parent = node.parent
        if not node.parent:
            self.root = pivot
        elif node == node.parent.left:
            node.parent.left = pivot
        else:
            node.parent.right = pivot
        pivot.left = node
        node.parent = pivot

    def __right_rotation(self, node):
        pivot = node.left
        node.left = pivot.right
        if pivot.right:
            pivot.right.parent = node
        pivot.parent = node.parent
        if not node.parent:
            self.root = pivot
        elif node == node.parent.left:
            node.parent.left = pivot
        else:
            node.parent.right = pivot
        pivot.right = node
        node.parent = pivot

    def tree_print_dot_body(self, r, filename):
        with open(filename, 'w') as file:
            file.write("digraph Tree {\n")
            self._tree_print_dot_body_helper(r, file)
            file.write("}\n")

    def _tree_print_dot_body_helper(self, r, file):
        if r is not None:
            self._tree_print_dot_body_helper(r.left, file)
            file.write(f'  "{id(r)}" [label="{{{id(r)}|{r.height}|{r.key}|{{'
                       f'{id(r.left)}|{id(r.right)}}}}}"];\n')
            if r.left:
                file.write(f'  "{id(r)}" -> "{id(r.left)}";\n')
            if r.right:
                file.write(f'  "{id(r)}" -> "{id(r.right)}";\n')
            self._tree_print_dot_body_helper(r.right, file)


if __name__ == "__main__":

    n = int(sys.argv[1])
    # caso medio e melhor
    vet = vetores.randv(n)
    # pior
    # vet = vetores.sortv(n)
    tree = Tree()
    for i in vet:
        tree.insert(i)

    start = time.time_ns()
    # caso medio
    tree.search(random.randint(1000, 10000))
    # melhor caso
    # tree.search(tree.root.key)
    # pior caso
    # tree.search(10000000)
    end = time.time_ns()
    final_time = end - start
    print(final_time)
