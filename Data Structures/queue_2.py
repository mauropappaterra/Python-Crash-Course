# Python Crash Course 
# queue.py
# Created by Mauro J. Pappaterra on 11 of March 2018.

# A Python implementation of a Queue
# A queue is a FIFO data structure. This is a single ended queue.
# e.g.: 5 -> 4 -> 3 -> 2 -> 1

# This queue uses a Python 'List' data structure

class queue():

    def __init__(self, element = None):
        "Class constructor"
        if (element != None):
            self.data = [element]
        else:
            self.data = []

    def queue (self, element):
        "Adds element to the tail of the queue"
        self.data.insert(0,element)

    def unqueue (self):
        "Pops out element from the head of the queue"
        if (not self.is_empty()):
            return self.data.pop(len(self.data) - 1)
        else:
            return None

    def is_empty (self):
        "Returns True if the queue is empty"
        return (len(self.data) == 0)

    def size(self):
        "Returns size of the queue"
        return len(self.data)

    def print_queue (self):
        "Prints contents of the queue"
        if (not self.is_empty()):
            printout = ''

            for element in self.data:
                printout += str(element) + ' -> '

            print(printout[0:-3])
        else:
            print("The queue is empty!")

# ALL TESTS
q1 = queue()

q1.queue(1)
q1.queue(2)
q1.queue(3)
q1.queue(4)
q1.queue(5)

q1.print_queue()

print(q1.unqueue())
print(q1.unqueue())
print(q1.unqueue())

q1.print_queue()

print(q1.unqueue())
print(q1.unqueue())
print(q1.unqueue())

q1.print_queue()

q2 = queue("a")

q2.queue("b")
q2.queue("c")
q2.queue("d")
q2.queue("e")
q2.queue("f")
q2.queue("g")

q2.print_queue()

q2.queue("h")
q2.queue("i")
q2.queue("j")
q2.queue("k")

q2.print_queue()
print(q2.size())

print(q2.unqueue())
print(q2.unqueue())
print(q2.unqueue())
print(q2.unqueue())
print(q2.unqueue())
print(q2.unqueue())

q2.print_queue()
print(q2.size())

print(q2.unqueue())
print(q2.unqueue())
print(q2.unqueue())
print(q2.unqueue())
print(q2.unqueue())

q2.print_queue()
print(q2.unqueue())