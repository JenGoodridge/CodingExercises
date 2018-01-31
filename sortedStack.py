# Code a stack that sorts the integers within.
import unittest
class Item():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack():
    def __init__(self):
        self.head = None

    def pop(self):  # Remove item from the top of the stack
        self.head = self.head.next

    def push(self, data):  # Push new item onto stack
        self.head = Item(data, self.head)

    def peek(self):
        return self.head

    def isEmpty(self):
        return self.head is None

    def __str__(self):
        string = "["
        current = self.head
        while current is not None:
            string += str(current.data)
            current = current.next
            if current is not None:
                string += ","

        return string + "]"


class Sorted_Stack():
    def __init__(self):
        self.temporaryStack = Stack()
        self.mainStack = Stack()

    def pop(self):
        self.mainStack.pop()

    def push(self, data):
        if self.mainStack.isEmpty():
            self.mainStack.push(data)

        elif self.mainStack.head.data >= data:
            self.mainStack.push(data)

        else:
            while not self.mainStack.isEmpty()and self.mainStack.head.data < data:
                self.temporaryStack.push(self.mainStack.head.data)
                self.mainStack.pop()

            self.mainStack.push(data)

            while not self.temporaryStack.isEmpty():
                self.mainStack.push(self.temporaryStack.head.data)
                self.temporaryStack.pop()

    def peek(self):
        return self.mainStack.peek()

    def isEmpty(self):
        return self.mainStack.isEmpty()
    
    def printStack(self):
        string = "["
        current = self.mainStack.head
        while current is not None:
            string += str(current.data)
            current = current.next
            if current is not None:
                string += ","

        return string + "]"


#setup for testing
test = Sorted_Stack()
test.push(1)
test.push(5)
test.push(6)
test.push(9)
test.pop()
test.push(-3)
test.push(0)
test.pop()
test.push(-1)



class Test(unittest.TestCase):
    def test_SortedStack(self):
        self.assertEqual(test.printStack(), "[-1,0,5,6,9]")
        test.pop()
        test.push(5)
        self.assertEqual(test.printStack(),"[0,5,5,6,9]")
        test.push(7)
        self.assertEqual(test.printStack(),"[0,5,5,6,7,9]")
        test.pop()
        test.pop()
        test.pop()
        self.assertEqual(test.printStack(),"[6,7,9]")
        
        
unittest.main()
    
    
