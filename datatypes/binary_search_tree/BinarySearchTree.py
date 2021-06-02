#!/usr/env/python3

class Node:

    def __init__(self, key="None", val="None"):
        self.key = key
        self.value = val
        self.left = None
        self.right = None

    def set_left(self, node=None):
        self.left = node

    def set_right(self, node=None):
        self.right = node

    def __str__ (self):
        return ("["+str(self.key)+", "+str(self.value)+"]")


class BinarySearchTree:

    def __init__ (self):
        self.length = 0
        self.hash_table = []
        self.root = None

    def insert(self, key, value):
        new_ins = Node(key, value)

        if self.root is None:
            root = new_ins
            self.length += 1
            return

        if self.root.left is None and self.root.right is None:
            if key < self.root.key:
                self.root.set_left(new_ins)

            else:
                self.root.set_right(new_ins)

            self.length += 1
            return

        cur = self.root

        while cur is not None:
            if key < cur.key:
                cur = cur.left

            else:
                cur = cur.right

        if key < cur.key:
            cur.set_left(new_ins)

        else:
            cur.set_right(new_ins)

        self.length += 1

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = delete(root.left, key)

        if key >= root.key:
            root.right = delete(root.right, key)

        else:
            if root.left is None and root.right is None:
                root = None
                self.length -= 1

            elif root.left is None:
                root = root.right
                root.right = None
                self.length -= 1
                return root

            elif root.right is None:
                root = root.left
                root.left = None
                self.length -= 1
                return root

            else:
                temp = find_inorder_successor(root)
                root = temp
                self.length -= 1
                return root


    def find_inorder_successor(self, root):
        while root.left is not None:
            root = root.left

        return root

    def inorder_print(self, root):
        return_str = ""

        if root is not None:
            inorder_print(root.left)
            return_str.append(str(root)+" ")
            inorder_print(root.right)

        return return_str

    def print (self):
        print (self.root)


    def size (self):
        return self.length

    def __len__(self):
        return self.length

    def __str__ (self):
        return self.inorder_print(self.root)
