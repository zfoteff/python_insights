"""LinkedList data structure implemented in Python
"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None

    def set_next(self, next_node):
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert_at_tail (self, key, val):
        cur = Node(key, val)

        if self.length == 0:
            self.head = cur
            self.length += 1
            return

        last = self.head
        while last.next != None:
            last = last.next

        last.set_next(cur)
        self.length += 1

    def remove_from_end(self):
        cur = self.head

        if cur == None:
            print ("List is empty")
            return

        # List only has one element
        elif cur.next == None:
            self.head = None
            self.length -= 1
            return

        # Traverse to second to last element
        while cur.next.next != None:
            cur = cur.next

        cur.next = None
        self.length -= 1

    def remove_element (self, key):
        cur = self.head
        last = None

        if cur.key == key:
            last = cur.next
            cur = None
            self.head = last
            self.length -= 1
            return

        while cur.next != None:
            if cur.key == key:
                last.next = cur.next
                cur = None
                self.length -= 1
                return

            last = cur
            cur = cur.next

        print ("Element not found")

    def find (self, key):
        cur = self.head

        while cur != None:
            if cur.key == key:
                return True

            cur = cur.next

        return False

    def print (self):
        cur = self.head

        print("----------------------------")

        while cur != None:
            print(""+str(cur.key)+", "+cur.value)
            cur = cur.next

    def size (self):
        return self.length
