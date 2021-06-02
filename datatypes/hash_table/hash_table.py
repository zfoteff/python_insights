#!/usr/env/python3

class Node:

    def __init__(self, key="None", val="None"):
        self.key = key
        self.value = val
        self.next = None


    def set_next (self, node):
        self.next = node


    def __str__ (self):
        return ("["+str(self.key)+", "+str(self.value)+"]")


class HashTable:

    def __init__ (self):
        self.length = 0
        self.capacity = 16
        self.hash_table = []

        self.init_table()


    def hash_func (self, key):
        return self.capacity % key


    def init_table (self):
        self.hash_table = []
        self.length = 0

        i = 0
        while i < self.capacity:
            self.hash_table.append(None)
            i += 1


    def _resize_and_rehash (self):
        self.capacity *= 2
        old_table = self.hash_table
        self.init_table()

        for each in old_table:
            if each is not None:
                self.insert(each.key, each.value)

                if each.next is not None:
                    while each.next is not None:
                        each = each.next
                        self.insert(each.key, each.value)


    def insert (self, key, val):
        new_ins = Node(key, val)
        slot = self.hash_table[self.hash_func(key)]

        if slot is not None:
            while slot.next is not None:
                slot = slot.next

            slot.next = new_ins
            self.length += 1

            if (float(self.length) / float(self.capacity)) >= 0.75:
                self._resize_and_rehash()

            return

        self.hash_table[self.hash_func(key)] = new_ins
        self.length += 1

        if (float(self.length) / float(self.capacity)) >= 0.75:
            print ("Here")
            self._resize_and_rehash()


    def delete (self, key):
        head = self.hash_table[self.hash_func(key)]

        if self.length == 0:
            print ("Table empty")
            return

        if head is None:
            print ("Empty")
            return

        if head.key != key:
            while head.next is not None:
                prev = head
                head = head.next

                if head.key == key:
                    prev.next = head.next
                    head = None
                    self.length -= 1
                    return

            return

        # If the first Node in the chain is the specified node
        if head.key == key:
            if head.next is None:
                self.hash_table[self.hash_func(key)] = None
                self.length -= 1
                return

            temp = head.next
            self.hash_table[self.hash_func(key)] = None
            self.hash_table[self.hash_func(key)] = temp
            self.length -= 1
            return

        print ("\nKey not found")


    def find (self, key):
        cur = self.hash_table[self.hash_func(key)]

        if cur is None:
            return False

        if cur.key == key:
            return True

        if cur.key != key:
            if cur.next is None:
                return False

            while cur.next is not None:
                cur = cur.next

                if cur.key == key:
                    return True

        return False


    def get (self, key):
        cur = self.head_table[self.hash_func(key)]

        if cur is None:
            print ("Key not found")
            return None


    def size(self):
        return self.length


    def print (self):
        index = 0

        for each in self.hash_table:
            print (str(index)+"\t| \t", end='')
            index += 1

            if each is None:
                print ("[ ]")
                continue

            print (str(each) + "--> ", end="")

            while each.next is not None:
                each = each.next
                print(str(each)+"--> ", end='')

            print ("")
        print("\n")
