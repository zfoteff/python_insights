from py_doubly_linked_list import *
import unittest as ut

class TestDoublyLinkedMethods (ut.TestCase):

    def test_correct_size (self):
        print ("\nCorrect Size Test -------------")
        list = DoublyLinkedList()

        self.assertEqual(list.size(), 0)
        list.ins_at_tail(1, 'a')
        list.ins_at_tail(2, 'b')
        list.ins_at_tail(3, 'c')
        list.print()

        self.assertEqual(list.size(), 3)
        print ("\nEnd Correct Size Test ----------")


    def test_ins_head (self):
        print ("\nHead insert test ---------------")

        list = DoublyLinkedList()
        list.print()

        self.assertEqual(list.size(), 0)

        self.assertFalse(list.find('a'))
        list.ins_at_head(1, 'a')
        self.assertTrue(list.find(1))
        self.assertEqual(list.size(), 1)
        self.assertEqual(list.get(0), "1")
        list.print()

        self.assertFalse(list.find('b'))
        list.ins_at_head(2, 'b')
        self.assertTrue(list.find(2))
        self.assertEqual(list.size(), 2)
        self.assertEqual(list.get(0), "2")
        list.print()

        self.assertFalse(list.find('c'))
        list.ins_at_head(3, 'c')
        self.assertTrue(list.find(3))
        self.assertEqual(list.size(), 3)
        self.assertEqual(list.get(0), "3")
        list.print()

        print ("\nEnd Head insert test ------------")


    def test_ins_tail (self):
        print ("\nTail insert test ----------------")

        list = DoublyLinkedList()
        list.print()

        self.assertEqual(list.size(), 0)

        self.assertFalse(list.find('a'))
        list.ins_at_tail(1, 'a')
        self.assertTrue(list.find(1))
        self.assertEqual(list.size(), 1)
        self.assertEqual(list.get(list.size() - 1), "1")
        list.print()

        self.assertFalse(list.find('b'))
        list.ins_at_tail(2, 'b')
        self.assertTrue(list.find(2))
        self.assertEqual(list.size(), 2)
        self.assertEqual(list.get(list.size() - 1), "2")
        list.print()

        self.assertFalse(list.find('c'))
        list.ins_at_tail(3, 'c')
        self.assertTrue(list.find(3))
        self.assertEqual(list.size(), 3)
        self.assertEqual(list.get(list.size() - 1), "3")
        list.print()

        print ("\nEnd Tail insert test -------------")


    def test_del_head (self):
        print ("\nHead deletion test ---------------")

        list = DoublyLinkedList()

        list.ins_at_tail(1, 'a')
        list.ins_at_tail(2, 'b')
        list.ins_at_tail(3, 'c')
        list.print()

        self.assertEqual(list.size(), 3)
        self.assertTrue(list.find(1))
        list.delete_head()
        self.assertFalse(list.find(1))
        self.assertEqual(list.size(), 2)
        list.print()

        self.assertTrue(list.find(2))
        list.delete_head()
        self.assertFalse(list.find(2))
        self.assertEqual(list.size(), 1)
        list.print()

        self.assertTrue(list.find(3))
        list.delete_head()
        self.assertFalse(list.find(3))
        self.assertEqual(list.size(), 0)
        list.print()

        self.assertTrue(list.isEmpty())

        print ("\nEnd Head deletion test ------------")


    def test_del_tail (self):
        print ("\nTail deletion test ----------------")

        list = DoublyLinkedList()

        list.ins_at_tail(1, 'a')
        list.ins_at_tail(2, 'b')
        list.ins_at_tail(3, 'c')
        list.print()

        self.assertEqual(list.size(), 3)
        self.assertTrue(list.find(3))
        list.delete_tail()
        self.assertFalse(list.find(3))
        self.assertEqual(list.size(), 2)
        list.print()

        self.assertTrue(list.find(2))
        list.delete_tail()
        self.assertFalse(list.find(2))
        self.assertEqual(list.size(), 1)
        list.print()

        self.assertTrue(list.find(1))
        list.delete_tail()
        self.assertFalse(list.find(1))
        self.assertEqual(list.size(), 0)
        list.print()

        self.assertTrue(list.isEmpty())

        print ("\nEnd tail deletion test -------------")


    def test_del_at (self):
        print ("\nDelete at test ---------------------")

        list = DoublyLinkedList()

        list.ins_at_tail(1, 'a')
        list.ins_at_tail(2, 'b')
        list.ins_at_tail(3, 'c')
        list.ins_at_tail(4, 'd')
        list.ins_at_tail(5, 'e')
        list.print()

        self.assertTrue(list.find(1))
        self.assertTrue(list.find(2))
        self.assertTrue(list.find(3))
        self.assertTrue(list.find(4))
        self.assertTrue(list.find(5))
        self.assertEqual(list.size(), 5)

        list.delete_at(3)                   # Delete index 3
        list.print()

        self.assertTrue(list.find(1))
        self.assertTrue(list.find(2))
        self.assertTrue(list.find(3))
        self.assertFalse(list.find(4))
        self.assertTrue(list.find(5))
        self.assertEqual(list.size(), 4)

        list.delete_at(0)                   # Delete index 0
        list.print()

        self.assertFalse(list.find(1))
        self.assertTrue(list.find(2))
        self.assertTrue(list.find(3))
        self.assertFalse(list.find(4))
        self.assertTrue(list.find(5))
        self.assertEqual(list.size(), 3)

        list.delete_at(1)                   # Delete index 1
        list.print()

        self.assertFalse(list.find(1))
        self.assertTrue(list.find(2))
        self.assertFalse(list.find(3))
        self.assertFalse(list.find(4))
        self.assertTrue(list.find(5))
        self.assertEqual(list.size(), 2)

        list.delete_at(1)                   # Delete index 1
        list.print()

        self.assertFalse(list.find(1))
        self.assertTrue(list.find(2))
        self.assertFalse(list.find(3))
        self.assertFalse(list.find(4))
        self.assertFalse(list.find(5))
        self.assertEqual(list.size(), 1)

        list.delete_at(0)                   # Delete index 0
        list.print()

        self.assertFalse(list.find(1))
        self.assertFalse(list.find(2))
        self.assertFalse(list.find(3))
        self.assertFalse(list.find(4))
        self.assertFalse(list.find(5))
        self.assertEqual(list.size(), 0)

        self.assertTrue(list.isEmpty())

        print ("\nEnd delete at test ----------------")


    def test_del_key (self):
        print ("\nDelete key test -------------------")

        list = DoublyLinkedList()
        list.ins_at_tail(1, 'a')
        list.ins_at_tail(2, 'b')
        list.ins_at_tail(3, 'c')
        list.ins_at_tail(4, 'd')
        list.ins_at_tail(5, 'e')
        list.print()

        self.assertTrue(list.find(1))
        self.assertTrue(list.find(2))
        self.assertTrue(list.find(3))
        self.assertTrue(list.find(4))
        self.assertTrue(list.find(5))
        self.assertEqual(list.size(), 5)

        list.delete_key(3)                   # Delete key 3
        list.print()

        self.assertTrue(list.find(1))
        self.assertTrue(list.find(2))
        self.assertFalse(list.find(3))
        self.assertTrue(list.find(4))
        self.assertTrue(list.find(5))
        self.assertEqual(list.size(), 4)

        list.delete_key(1)                   # Delete key 1 (head)
        list.print()

        self.assertFalse(list.find(1))
        self.assertTrue(list.find(2))
        self.assertFalse(list.find(3))
        self.assertTrue(list.find(4))
        self.assertTrue(list.find(5))
        self.assertEqual(list.size(), 3)

        list.delete_key(5)                   # Delete key 5 (tail)
        list.print()

        self.assertFalse(list.find(1))
        self.assertTrue(list.find(2))
        self.assertFalse(list.find(3))
        self.assertTrue(list.find(4))
        self.assertFalse(list.find(5))
        self.assertEqual(list.size(), 2)

        list.delete_key(2)                   # Delete key 5 (tail)
        list.print()

        self.assertFalse(list.find(1))
        self.assertFalse(list.find(2))
        self.assertFalse(list.find(3))
        self.assertTrue(list.find(4))
        self.assertFalse(list.find(5))
        self.assertEqual(list.size(), 1)

        list.delete_key(4)                   # Delete key 5 (tail)
        list.print()

        self.assertFalse(list.find(1))
        self.assertFalse(list.find(2))
        self.assertFalse(list.find(3))
        self.assertFalse(list.find(4))
        self.assertFalse(list.find(5))
        self.assertEqual(list.size(), 0)

        self.assertTrue(list.isEmpty())

        print ("\nEnd delete key test ---------------")


    def test_illegal_commands (self):
        print ("\nIllegal commands test--------------")

        list = DoublyLinkedList()
        list.ins_at_tail(1, 'a')
        list.ins_at_tail(2, 'b')
        list.ins_at_tail(3, 'c')
        list.ins_at_tail(4, 'd')
        list.ins_at_tail(5, 'e')
        list.print()

        # Try to delete a element that exceeds the index bounds
        list.delete_at(5)
        self.assertTrue(list.find(1))
        self.assertTrue(list.find(2))
        self.assertTrue(list.find(3))
        self.assertTrue(list.find(4))
        self.assertTrue(list.find(5))
        self.assertEqual(list.size(), 5)

        # Try to delete a element that exceeds the index bounds
        list.delete_at(5)
        self.assertTrue(list.find(1))
        self.assertTrue(list.find(2))
        self.assertTrue(list.find(3))
        self.assertTrue(list.find(4))
        self.assertTrue(list.find(5))
        self.assertEqual(list.size(), 5)

        # Try to delete a key that doesn't exist
        self.assertFalse(list.find(8))
        list.delete_key(8)

        # Try to delete from an empty list
        list.clear()
        list.print()
        list.delete_at(0)
        list.delete_key(1)
        list.delete_head()
        list.delete_tail()

        # Try to get key in an empty list
        list.get(1)

        print ("\nEnd illegal commands test --------")


    def test_clear (self):
        print ("\nClear command test ----------------")
        list = DoublyLinkedList()
        list.ins_at_tail(1, 'a')
        list.ins_at_tail(2, 'b')
        list.ins_at_tail(3, 'c')

        self.assertTrue(list.find(1))
        self.assertTrue(list.find(2))
        self.assertTrue(list.find(3))

        list.print()
        list.clear()
        list.print()

        self.assertFalse(list.find(1))
        self.assertFalse(list.find(2))
        self.assertFalse(list.find(3))
        print ("\nEnd clear command test ------------")


    def test_indeces (self):
        print("\nIndex value test -------------------")
        list = DoublyLinkedList()
        list.ins_at_tail(1, 'a')
        list.ins_at_tail(2, 'b')
        list.ins_at_tail(3, 'c')

        self.assertEqual(list.get(0), "1")
        self.assertEqual(list.get(1), "2")
        self.assertEqual(list.get(2), "3")
        print("\nEnd index value test ---------------")


if __name__ == '__main__':
    ut.main()
