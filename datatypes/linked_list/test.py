import unittest as ut
from linked import *

class TestLinkedListMethods(ut.TestCase):

    def test_correct_size (self):
        list = LinkedList()

        self.assertEqual(list.size(), 0)

        list.insert_at_tail(1, 'a')
        list.insert_at_tail(2, 'b')
        list.insert_at_tail(3, 'c')

        self.assertEqual(list.size(), 3)

    def test_insert (self):
        list = LinkedList()

        self.assertEqual(list.size(), 0)
        self.assertFalse(list.find(1))

        list.insert_at_tail(1, 'a')
        self.assertEqual(list.size(), 1)
        self.assertTrue(list.find(1))

        list.insert_at_tail(2, 'b')
        self.assertEqual(list.size(), 2)
        self.assertTrue(list.find(1))
        self.assertTrue(list.find(2))

    def test_remove_from_end (self):
        list = LinkedList()

        list.insert_at_tail(1, 'a')
        list.insert_at_tail(2, 'b')
        list.insert_at_tail(3, 'c')

        self.assertEqual(list.size(), 3)
        self.assertTrue(list.find(1))
        self.assertTrue(list.find(2))
        self.assertTrue(list.find(3))

        list.remove_from_end()
        self.assertEqual(list.size(), 2)
        self.assertTrue(list.find(1))
        self.assertTrue(list.find(2))
        self.assertFalse(list.find(3))

    def test_remove_element(self):
        list = LinkedList()

        list.insert_at_tail(1, 'a')
        list.insert_at_tail(2, 'b')
        list.insert_at_tail(3, 'c')

        self.assertEqual(list.size(), 3)
        self.assertTrue(list.find(1))
        self.assertTrue(list.find(2))
        self.assertTrue(list.find(3))

        list.remove_element(2)
        self.assertEqual(list.size(), 2)
        self.assertTrue(list.find(1))
        self.assertFalse(list.find(2))
        self.assertTrue(list.find(3))

        list.remove_element(1)
        self.assertEqual(list.size(), 1)
        self.assertFalse(list.find(1))
        self.assertFalse(list.find(2))
        self.assertTrue(list.find(3))

        list.remove_element(3)
        self.assertEqual(list.size(), 0)
        self.assertFalse(list.find(1))
        self.assertFalse(list.find(2))
        self.assertFalse(list.find(3))


if __name__ == '__main__':
    ut.main()
