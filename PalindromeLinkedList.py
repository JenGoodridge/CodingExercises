# Given a string and using linked lists
# determine whether the string is a palindrome


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

        self.length += 1

    def append_node(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

        self.length += 1

    def prepend(self, data):
        self.head = Node(data, self.head)
        self.length += 1

    def prepend_node(self, noded):
        noded.next = self.head
        self.head = noded

    def __str__(self):
        string = "["
        current = self.head
        while current is not None:
            string += str(current.data)
            current = current.next
            if current is not None:
                string += ","

        return string + "]"


class Palindrome():
    def Palindrome_check(list1):
        list2 = LinkedList()
        current = list1.head
        while current is not None:
            list2.prepend(current.data)
            current = current.next
        print(list2)
        current1 = list1.head
        current2 = list2.head
        while current1 is not None:
            if current1.data is not current2.data:
                return False
                break
            current1 = current1.next
            current2 = current2.next
        return True

    list1 = LinkedList()
    list1.append("a")
    list1.append("b")
    list1.append("a")
    print(Palindrome_check(list1))
    list2 = LinkedList()
    list2.append("a")
    list2.append("a")
    list2.append("q")
    list2.append("w")
    list2.append("t")
    print(Palindrome_check(list2))
