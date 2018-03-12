# Python Crash Course 
# linkedList.py
# Created by Mauro J. Pappaterra on 11 of March 2018.

# A Python implementation of a Linked List

class linkedList():

    def __init__ (self, element = None):
        "Class Constructor"
        if (element != None):
            self.data = element
        else:
            self.data = None
        self.next = None

    def append (self, element):
        "Appends an element to the (right) end of the list"

        if (self.data == None):
            self.data = element
            return

        current = self
        while (current.next != None):
            current = current.next

        current.next = linkedList(element)

    def prepend (self, element):
        "Prepends an element to the (left) end of the list"
        if (self.data == None):
            self.data = element
            return

        currentHead = linkedList(self.data) # replicate values of current head
        currentHead.next = self.next

        self.data = element # replace head values with new values
        self.next = currentHead

    def deleteValue (self, value):
        "Deletes element of given value from the list"
        if (self.data == None):
            return # exit if linked list is empty

        if (self.data == value):
            if (self.next != None): # if there are more elements on the list
                self.data = self.next.data
                self.next = self.next.next
            else: # if we are deleting the last element on the list
                self.data = None
            return

        current = self

        while (current.next != None):
            if (current.next.data == value): # if found: cut node loose once the value is found
                current.next = current.next.next
                return
            current = current.next # otherwise: iterate next node

    def printList (self):
        "Print all contents of the linked list"
        if (self.data != None):
            printout = str(self.data) + ' ~ '

            current = self

            while (current.next != None):
                current = current.next
                printout += str(current.data) + ' ~ '

            print (printout[0:-3])
        else:
            print("The linked list is empty!")

# ALL TESTS

l = linkedList()

l.append('*')
l.append('&')
l.append('%')
l.printList()

l.deleteValue('*')
l.deleteValue('&')
l.printList()

l.deleteValue('%')
l.printList()

linked = linkedList(1)
linked.printList()

linked.append(2)
linked.append(3)
linked.append(8)
linked.append(4)
linked.append(5)

linked.printList()

linked.append(6)
linked.append(7)

linked.printList()

linked.deleteValue(1)
linked.deleteValue(8)
linked.deleteValue(7)
linked.printList()

linked.prepend(1)
linked.prepend(0)
linked.printList()