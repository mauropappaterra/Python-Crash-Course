# Python Crash Course 
# stack_3.py
# Created by Mauro J. Pappaterra on 11 of March 2018.

# A Python implementation of a Stack
# A stack is a LIFO data structure.
# e.g.: base | centre | centre | centre | centre | top

# This stack uses a Python 'List' data structure

class stack():

    def __init__(self, element = None):
        "Constructor Method"
        if (element != None):
            self.data = [element]
        else:
            self.data = []

    def push(self, element):
        "Push an element on top of the stack"
        self.data.append(element)

    def pop(self):
        "Pops the top element out of the stack"
        if (not self.is_empty()):
            return self.data.pop()
        return None

    def peek (self):
        "Returns the top element without removing it"
        if (not self.is_empty()):
            return self.data[-1]
        return None

    def size (self):
        "Return size of the stack"
        return (len(self.data))

    def is_empty (self):
        "Returns True is the stack is empty"
        return (self.size() < 1)

    def print_stack (self):
        "Prints contents of the stack"
        if (not self.is_empty()):
            printout = ''

            for element in self.data:
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