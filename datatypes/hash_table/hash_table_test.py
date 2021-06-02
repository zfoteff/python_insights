from hash_table import *
import unittest as ut

class TestHashMethods (ut.TestCase):

    def test_correct_size (self):
        print ("\nCorrect size test ---------------\n")
        list = HashTable()

        self.assertEqual(list.size(), 0)
        list.insert(1, 'a')
        list.insert(2, 'b')
        list.insert(3, 'c')
        list.insert(4, 'd')
        list.insert(5, 'e')

        list.print()

        self.assertEqual(list.size(), 5)
        print ("\nEnd correct size test -------------")

    def test_ins_no_chaining (self):
        print ("\nInsert test (no chaining) ---------")
        list = HashTable()

        self.assertEqual(list.size(), 0)

        list.insert(16, 'a')
        self.assertTrue(list.find(16))
        self.assertEqual(list.size(), 1)

        list.insert(9, 'b')
        self.assertTrue(list.find(9))
        self.assertEqual(list.size(), 2)

        list.insert(10, 'c')
        self.assertTrue(list.find(10))
        self.assertEqual(list.size(), 3)

        list.insert(13, 'd')
        self.assertTrue(list.find(13))
        self.assertEqual(list.size(), 4)

        list.print()
        print ("\nEnd insert test (no chaining) -----")

    def test_ins_with_chaining (self):
        print ("\nInsert test (chaining) ------------")
        list = HashTable()

        self.assertEqual(list.size(), 0)

        list.insert(8, 'a')
        self.assertTrue(list.find(8))
        self.assertEqual(list.size(), 1)

        list.insert(4, 'b')
        self.assertTrue(list.find(4))
        self.assertEqual(list.size(), 2)

        list.insert(2, 'c')
        self.assertTrue(list.find(2))
        self.assertEqual(list.size(), 3)

        list.insert(3, 'd')
        self.assertTrue(list.find(3))
        self.assertEqual(list.size(), 4)

        list.insert(5, 'e')
        self.assertTrue(list.find(5))
        self.assertEqual(list.size(), 5)

        list.print()
        print("\nEnd insert test (chaining) ----------")

    def test_del_no_chaining (self):
        print ("\nDelete test (no chaining) --------")
        list = HashTable()

        list.insert(16, 'a')
        list.insert(9, 'b')
        list.insert(10, 'c')
        list.insert(13, 'd')
        list.insert(3, 'e')

        print("Initial list")
        self.assertTrue(list.find(16))
        self.assertTrue(list.find(9))
        self.assertTrue(list.find(10))
        self.assertTrue(list.find(13))
        self.assertTrue(list.find(3))
        self.assertEqual(list.size(), 5)
        list.print()

        list.delete(16)
        self.assertFalse(list.find(16))
        self.assertTrue(list.find(9))
        self.assertTrue(list.find(10))
        self.assertTrue(list.find(13))
        self.assertTrue(list.find(3))
        self.assertEqual(list.size(), 4)
        print("Delete 16")
        list.print()

        list.delete(9)
        self.assertFalse(list.find(16))
        self.assertFalse(list.find(9))
        self.assertTrue(list.find(10))
        self.assertTrue(list.find(13))
        self.assertTrue(list.find(3))
        self.assertEqual(list.size(), 3)
        print("Delete 9")
        list.print()

        list.delete(10)
        self.assertFalse(list.find(16))
        self.assertFalse(list.find(9))
        self.assertFalse(list.find(10))
        self.assertTrue(list.find(13))
        self.assertTrue(list.find(3))
        self.assertEqual(list.size(), 2)
        print("Delete 10")
        list.print()

        list.delete(13)
        self.assertFalse(list.find(16))
        self.assertFalse(list.find(9))
        self.assertFalse(list.find(10))
        self.assertFalse(list.find(13))
        self.assertTrue(list.find(3))
        self.assertEqual(list.size(), 1)
        print("Delete 13")
        list.print()

        list.delete(3)
        self.assertFalse(list.find(16))
        self.assertFalse(list.find(9))
        self.assertFalse(list.find(10))
        self.assertFalse(list.find(13))
        self.assertFalse(list.find(3))
        self.assertEqual(list.size(), 0)
        print("Delete 3")
        list.print()

        print ("\nDelete test (no chaining) -----")

    def test_del_with_chaining (self):
        print ("\nDelete test (chaining) --------")
        list = HashTable()

        list.insert(1, 'a')
        list.insert(2, 'b')
        list.insert(3, 'c')
        list.insert(4, 'd')
        list.insert(5, 'e')

        print("Initial list")
        self.assertTrue(list.find(1))
        self.assertTrue(list.find(2))
        self.assertTrue(list.find(3))
        self.assertTrue(list.find(4))
        self.assertTrue(list.find(5))
        self.assertEqual(list.size(), 5)
        list.print()

        list.delete(1)
        self.assertFalse(list.find(1))
        self.assertTrue(list.find(2))
        self.assertTrue(list.find(3))
        self.assertTrue(list.find(4))
        self.assertTrue(list.find(5))
        self.assertEqual(list.size(), 4)
        print("Delete 1")
        list.print()

        list.delete(2)
        self.assertFalse(list.find(1))
        self.assertFalse(list.find(2))
        self.assertTrue(list.find(3))
        self.assertTrue(list.find(4))
        self.assertTrue(list.find(5))
        self.assertEqual(list.size(), 3)
        print("Delete 2")
        list.print()

        list.delete(3)
        self.assertFalse(list.find(1))
        self.assertFalse(list.find(2))
        self.assertFalse(list.find(3))
        self.assertTrue(list.find(4))
        self.assertTrue(list.find(5))
        self.assertEqual(list.size(), 2)
        print("Delete 3")
        list.print()

        list.delete(4)
        self.assertFalse(list.find(1))
        self.assertFalse(list.find(2))
        self.assertFalse(list.find(3))
        self.assertFalse(list.find(4))
        self.assertTrue(list.find(5))
        self.assertEqual(list.size(), 1)
        print("Delete 4")
        list.print()

        list.delete(5)
        self.assertFalse(list.find(1))
        self.assertFalse(list.find(2))
        self.assertFalse(list.find(3))
        self.assertFalse(list.find(4))
        self.assertFalse(list.find(5))
        self.assertEqual(list.size(), 0)
        print("Delete 5")
        list.print()

        print("\nEnd delete test (chaining) -----")

    def test_delete_middle_of_chain(self):
        print("\nDelete middle of chain test ----")

        list = HashTable()

        list.insert(1, 'a')
        list.insert(2, 'b')
        list.insert(3, 'c')
        list.insert(4, 'd')
        list.insert(5, 'e')
        list.insert(15, 'f')

        print("Initial list")
        self.assertTrue(list.find(1))
        self.assertTrue(list.find(2))
        self.assertTrue(list.find(3))
        self.assertTrue(list.find(4))
        self.assertTrue(list.find(5))
        self.assertTrue(list.find(15))
        self.assertEqual(list.size(), 6)
        list.print()

        list.delete(2)
        list.delete(15)

        print ("Altered list")
        self.assertTrue(list.find(1))
        self.assertFalse(list.find(2))
        self.assertTrue(list.find(3))
        self.assertTrue(list.find(4))
        self.assertTrue(list.find(5))
        self.assertFalse(list.find(15))
        self.assertEqual(list.size(), 4)
        list.print()

        print ("\nEnd delete middle of chain test --")

    def test_resize_rehash (self):
        print ("\nResize and rehash test -----------")

        list = HashTable()

        list.insert(1, 'a')
        list.insert(2, 'b')
        list.insert(3, 'c')
        list.insert(4, 'd')
        list.insert(5, 'e')
        list.insert(6, 'f')
        list.insert(7, 'g')
        list.insert(8, 'h')
        list.insert(9, 'i')
        list.insert(10, 'j')
        list.insert(11, 'k')
        list.print()

        self.assertTrue(list.find(1))
        self.assertTrue(list.find(2))
        self.assertTrue(list.find(3))
        self.assertTrue(list.find(4))
        self.assertTrue(list.find(5))
        self.assertTrue(list.find(6))
        self.assertTrue(list.find(7))
        self.assertTrue(list.find(8))
        self.assertTrue(list.find(9))
        self.assertTrue(list.find(10))
        self.assertTrue(list.find(11))
        self.assertFalse(list.find(12))
        self.assertEqual(list.size(), 11)

        list.insert(12, 'l')
        list.print()

        self.assertTrue(list.find(1))
        self.assertTrue(list.find(2))
        self.assertTrue(list.find(3))
        self.assertTrue(list.find(4))
        self.assertTrue(list.find(5))
        self.assertTrue(list.find(6))
        self.assertTrue(list.find(7))
        self.assertTrue(list.find(8))
        self.assertTrue(list.find(9))
        self.assertTrue(list.find(10))
        self.assertTrue(list.find(11))
        self.assertTrue(list.find(12))
        self.assertEqual(list.size(), 12)

if __name__ == '__main__':
    ut.main()
