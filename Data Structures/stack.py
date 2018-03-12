# Python Crash Course 
# stack_2.py
# Created by Mauro J. Pappaterra on 12 of March 2018.

# A Python implementation of a Stack
# A stack is a LIFO data structure.
# e.g.: base | centre | centre | centre | centre | top

class stack():

    def __init__(self, element = None):
        "Constructor Method"
        self.data = element
        self.bottom = None

    def push(self, element):
        "Push an element on top of the stack"

        if (self.data == None):
            self.data = element # if stack is empty save on current node
            return

        current = stack(self.data)
        current.bottom = self.bottom

        self.data = element
        self.bottom = current

    def pop(self):
        "Pops the top element out of the stack"
        if (self.data != None):
            data = self.data

            if (self.bottom == None): # pop last element on the stack
                self.data = None
                return data

            self.data = self.bottom.data
            self.bottom = self.bottom.bottom

            return data
        else:
            print("The Stack is empty!")

    def peek (self):
        "Returns the top element without removing it"
        if (self.data != None):
            return self.data
        else:
            print("The Stack is empty!")
        return None

    def size (self):
        "Return size of the stack"
        if (self.data == None):
            return 0

        counter = 1

        current = self
        while (current.bottom != None):
            counter += 1
            current = current.bottom

        return counter

    def is_empty (self):
        "Returns True is the stack is empty"
        return (self.data == None)

    def print_stack (self):
        "Prints contents of the stack"
        if (not self.data == None):
            elements = [self.data]

            current = self
            while (current.bottom != None):
                current = current.bottom
                elements.append(current.data)

            printout = ''
            for element in elements[::-1]:
                printout += str(element) + ' | '

            print(printout[0:-3])
        else:
            print("The stack is empty!")

# ALL TESTS
s1 = stack("base")
s1.push("centre")
s1.push("top")

s1.print_stack()

print(s1.peek())
print(s1.peek())
print(s1.size())
print(s1.is_empty())

s1.print_stack()

print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())

print(s1.is_empty())
s1.print_stack()

s2 = stack()
s2.print_stack()
print(s2.size())