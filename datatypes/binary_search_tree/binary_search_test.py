from BinarySearchTree import *
import unittest as ut

class TestBinarySearchTreeMethods (ut.TestCase):
    def test_node_print(self):
        print ("\nNode print test \t ------------------")
        n1 = Node()
        n2 = Node(1)
        n3 = Node(2, "a")
        print(n1)
        print(n2)
        print(n3)

    def test_tree_print(self):
        print ("\nTree print test 1 \t ------------------")
        t1 = BinarySearchTree()
        t1.insert(2, "a")
        print(t1)
        t1.insert(1, "b")
        print(t1)
        t1.insert(3, "c")
        print(t1)

    def test_preorder_print(self):
        print ("\nTree print test 2 \t ------------------")
        t1 = BinarySearchTree()
        t1.insert(2, "a")
        t1.inorder_print(t1.root)
        t1.insert(1, "b")
        t1.inorder_print(t1.root)
        t1.insert(3, "c")
        t1.inorder_print(t1.root)

    def test_correct_size (self):
        print ("\nCorrect size test\t ------------------")
        list = BinarySearchTree()

        self.assertEqual(list.get_size(), 0)
        list.insert(3, 'c')
        list.insert(1, 'a')
        list.insert(2, 'b')
        list.insert(4, 'd')
        list.insert(5, 'e')
        self.assertEqual(list.get_size(), 5)

    def test_correct_height (self):
        print("\nCorrect height test\t ------------------")
        list = BinarySearchTree()
        self.assertEqual(list.height(), 0)

        #   Insert root node
        list.insert(5, "a")
        self.assertEqual(list.height(), 1)

        #   Insert left node
        list.insert(2, "b")
        self.assertEqual(list.height(), 2)

        #   Insert right node --> should still be same height
        list.insert(7, "c")
        self.assertEqual(list.height(), 2)

        list.insert(8, "d")
        self.assertEqual(list.height(), 3)

    def test_correct_get_retrieval(self):
        print("\nCorrect get test\t ------------------")
        list = BinarySearchTree()
        list.insert(5, "a")
        list.insert(8, "b")
        list.insert(3, "c")
        list.insert(1, "d")

        self.assertEqual(list.get(5), "a")
        self.assertEqual(list.get(8), "b")
        self.assertEqual(list.get(3), "c")
        self.assertEqual(list.get(1), "d")

    def test_correct_delete(self):
        print("\nCorrect delete test\t ------------------")
        list = BinarySearchTree()
        list.insert(5, "a")
        list.insert(8, "b")
        list.insert(3, "c")
        list.insert(1, "d")

        self.assertEqual(list.get_size(), 4)

        list.delete(8)
        self.assertEqual(list.get_size(), 3)

if __name__ == '__main__':
    ut.main()
