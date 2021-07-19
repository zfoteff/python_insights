#!/usr/env/python3

#   Node class for binary search tree
class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.value = val
        self.left = None
        self.right = None
        
    def set_left(self, node=None):
        self.left = node

    def set_right(self, node=None):
        self.right = node

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def __str__ (self):
        return ("["+str(self.key)+", "+str(self.value)+"]")

#   Binary Search Tree object definition
class BinarySearchTree:
    def __init__ (self):
        self.size = 0
        self.root = Node()

    def insert(self, key, value):
        new_ins = Node(key, value)

        if self.root.key is None:
            self.root = new_ins
            self.size += 1
            return

        if self.root.left is None and self.root.right is None:
            if key < self.root.key:
                self.root.set_left(new_ins)
            else:
                self.root.set_right(new_ins)

            self.size += 1
            return

        # Record root node for iteration
        curr_node = self.root
        parent_node = Node()

        # Navigate to leaf level
        while curr_node is not None:
            parent_node = curr_node

            if key < curr_node.key:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        if key < parent_node.key:
            parent_node.set_left(new_ins)
        else:
            parent_node.set_right(new_ins)

        self.size += 1

    def _delete(self, root, key):
        if root is None:
            return root

        elif key < root.key:
            root.left = self._delete(root.left, key)

        elif key > root.key:
            root.right = self._delete(root.right, key)

        else:
            if root.left is None and root.right is None:
                root = None
                self.size -= 1

            elif root.left is None:
                root = root.right
                root.right = None
                self.size -= 1
                return root

            elif root.right is None:
                root = root.left
                root.left = None
                self.size -= 1
                return root

            else:
                temp = find_inorder_successor(root)
                root = temp
                self.size -= 1
                return root

    def _get(self, key, subtree):
        curr_node = subtree

        if curr_node is None:
            return None
        elif curr_node.key == key:
            return curr_node.value
        elif key < curr_node.key:
            return self._get(key, curr_node.left)
        else:
            return self._get(key, curr_node.right)

    def find_inorder_successor(self, root):
        while root.left is not None:
            root = root.left

        return root

    def _height(self, subtree):
        curr_node = subtree
        if curr_node is None or (curr_node.left is None and curr_node.right is None) and curr_node.key is None:
            return 0

        lhs_height = 1 + self._height(curr_node.left)
        rhs_height = 1 + self._height(curr_node.right)

        if (lhs_height > rhs_height):
            return lhs_height
        return rhs_height

    def inorder_print(self, subtree):
        curr_node = subtree
        if curr_node is not None:
            self.inorder_print(curr_node.left)
            print(curr_node)
            self.inorder_print(curr_node.right)

    def preorder_print(self, subtree):
        curr_node = subtree
        if curr_node is not None:
            print(curr_node)
            self.preorder_print(curr_node.left)
            self.preorder_print(curr_node.right)

    def get_size(self):
        return self.size

    def delete(self, key):
        self._delete(self.root, key)


    def height(self):
        return self._height(self.root)

    def get(self, key):
        return self._get(key, self.root)

    def __len__(self):
        return self.size

    def __str__ (self):
        return str(self.inorder_print(self.root))
