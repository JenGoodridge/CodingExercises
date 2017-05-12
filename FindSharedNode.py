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


class intersect_node():
    list1 = LinkedList()
    list1.append(1)
    list1.append(6)
    list2 = LinkedList()
    list2.append(2)
    list2.append(3)

    def insert_node(list1, list2):
        new_node = Node(79797)
        list1.append_node(new_node)
        list2.append_node(new_node)

    def check_intersect(list1, list2):
        current1 = list1.head
        while current1 is not None:
            current2 = list2.head
            while current2 is not None:
                if current2 == current1:
                    return current1
                current2 = current2.next
            current1 = current1.next

    insert_node(list1, list2)
    list2.append(4)
    list2.append(77)
    list2.append(59)
    list1.append(5)

    if check_intersect(list1, list2) != None:
        print(check_intersect(list1, list2).data)
