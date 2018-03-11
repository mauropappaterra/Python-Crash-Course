# Python Crash Course 
# stack.py
# Created by Mauro J. Pappaterra on 11 of March 2018.

# A Python implementation of a Stack

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
my_stack = stack("base")
my_stack.push("centre")
my_stack.push("head")

my_stack.print_stack()

print(my_stack.peek())
print(my_stack.peek())
print(my_stack.size())
print(my_stack.is_empty())

my_stack.print_stack()

print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())
print(my_stack.pop())

my_stack.is_empty()
my_stack.print_stack()

my_stack2 = stack()
my_stack2.print_stack()