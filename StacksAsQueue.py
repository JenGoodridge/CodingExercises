class Item():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack():
    def __init__(self):
        self.head = None
        self.count = 0

    def pop(self):
        self.head = self.head.next
        self.count -= 1

    def push(self, data):
        self.head = Item(data, self.head)
        self.count += 1

    def peek(self):
        return self.head.data

    def isEmpty(self):
        return self.head == None

    def isFull(self):
        return self.count >= 5

    def __len__(self):
        return self.count

    def __str__(self):
        string = "["
        current = self.head
        while current != None:
            string += str(current.data)
            current = current.next
            if current != None:
                string += ","

        return string + "]"


class StacksAsQueue():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def add(self, data):
        self.stack1.push(data)
        while not self.stack1.isEmpty():
            self.stack2.push(self.stack1.peek())
            self.stack1.pop()

    def pop(self):
        self.stack2.pop()
        self.stack1 = Stack()

        print(self.stack2)

    def peek(self):
        return self.stack2.head

class Test():

    test = StacksAsQueue()
    test.add(0)
    test.add(1)
    test.pop()
    test.add(4)
    test.add(5)
    test.pop()
    test.pop()

