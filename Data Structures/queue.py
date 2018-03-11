# Python Crash Course 
# queue.py
# Created by Mauro J. Pappaterra on 11 of March 2018.


class queue():

    def __init__(self, element = None):
        if (element != None):
            self.data = [element]
        else:
            self.data = []

    def queue (self, element):
        self.data.insert(0,element)

    def unqueue (self):
        if (not self.is_empty()):
            return self.data.pop(len(self.data) - 1)
        else:
            return None

    def is_empty (self):
        return (len(self.data) == 0)

    def print_queue (self):
        "Prints contents of the stack"
        if (not self.is_empty()):
            printout = '|- '

            for element in self.data:
                printout += str(element) + ' -> '

            print(printout[0:-3])
        else:
            print("The queue is empty!")

# ALL TESTS
q = queue()

q.queue(1)
q.queue(2)
q.queue(3)
q.queue(4)
q.queue(5)

q.print_queue()

print(q.unqueue())
print(q.unqueue())
print(q.unqueue())

q.print_queue()

print(q.unqueue())
print(q.unqueue())
print(q.unqueue())

q.print_queue()











