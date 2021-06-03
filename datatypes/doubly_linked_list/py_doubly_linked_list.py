#!/usr/env/python3

class Node:

    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.last = None
        self.next = None


    def set_next (self, node):
        self.next = node


    def set_last (self, node):
        self.last = node


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def ins_at_tail (self, key, val):
        cur = Node(key, val)

        if self.length == 0:
            self.head = cur
            self.tail = cur
            self.length += 1
            return

        cur.set_last(self.tail)
        self.tail.set_next(cur)
        self.tail = cur
        self.length += 1


    def ins_at_head (self, key, val):
        cur = Node (key, val)

        if self.length == 0:
            self.head = cur
            self.tail = cur
            self.length += 1
            return

        cur.set_next(self.head)
        self.head.set_last(cur)
        self.head = cur
        self.length += 1


    def delete_head(self):
        if self.length == 0:
            print("\nList already empty")
            return

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return

        next_node = self.head.next
        next_node.last = None
        self.head = None
        self.head = next_node
        self.length -= 1
        return


    def delete_tail (self):
        if self.length == 0:
            print("\nList already empty")
            return

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return

        if self.length == 2:
            single_node = self.head
            single_node.next = None
            self.head = single_node
            self.tail = single_node
            self.length -= 1
            return

        last_node = self.tail.last
        last_node.next = None
        self.tail = None
        self.tail = last_node
        self.length -= 1
        return


    def delete_at (self, index):
        if self.length == 0:
            print ("\nList aready empty")
            return

        if index > (self.length - 1) or index < 0:
            print ("\nIndex out of bounds")
            return

        if index == 0:
            self.delete_head()
            return

        if index == (self.length - 1):
            self.delete_tail()
            return

        i = 1
        cur = self.head.next
        while i < index:
            cur = cur.next
            i += 1

        cur.last.next = cur.next
        cur = None
        self.length -= 1
        return


    def delete_key (self, key):
        if self.length == 0:
            print ("\nList already empty")
            return

        if self.head.key == key:
            self.delete_head()
            return

        if self.tail.key == key:
            self.delete_tail()
            return

        cur = self.head.next

        while cur.next != self.tail:
            if cur.key == key:
                cur.last.next = cur.next
                cur = None
                self.length -= 1
                return

            cur = cur.next

        print ("\nKey not found in list")
        return


    def size (self):
        return self.length


    def isEmpty (self):
        if self.length == 0:
            return True

        return False


    def clear (self):
        while not self.isEmpty():
            self.delete_tail()


    def find (self, key):
        if self.length == 0:
            return False

        cur = self.head

        while cur is not None:
            if cur.key == key:
                return True

            cur = cur.next

        return False


    def get (self, index):
        if self.length == 0:
            print ("\nList is empty")
            return

        cur = self.head
        i = 0

        while i < index:
            cur = cur.next
            i += 1

        return str(cur.key)


    def print (self):
        cur = self.head
        print('')
        print("[ ", end='')
        while cur is not None:
            print(cur.value+" ", end='')
            cur = cur.next

        print("]\n", end='')
