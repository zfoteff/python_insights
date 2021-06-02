from BinarySearchTree import *
import unittest as ut

class TestBinarySearchTreeMethods (ut.TestCase):

    def test_correct_size (self):
        print ("\nCorrect size test ---------------\n")
        list = BinarySearchTree()

        self.assertEqual(list.size(), 0)
        list.insert(3, 'c')
        list.insert(1, 'a')
        list.insert(2, 'b')
        list.insert(4, 'd')
        list.insert(5, 'e')

        print(list)
        list.print()

        self.assertEqual(list.size(), 5)
        print ("\nEnd correct size test -------------")

if __name__ == '__main__':
    ut.main()
