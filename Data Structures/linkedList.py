# Python Crash Course 
# linkedList.py
# Created by Mauro J. Pappaterra on 11 of March 2018.

# A Python implementation of a Linked List
# e.g.: 0 ~ 1 ~ 2 ~ 3 ~ 4 ~ 5 ~ 6

class linkedList():

    def __init__ (self, element = None):
        "Class Constructor"
        self.data = element
        self.next = None

    def append (self, element):
        "Appends an element to the (right) end of the list"
        if (self.data == None):
            self.data = element # if list is empty append to head node
            return

        current = self
        while (current.next != None):
            current = current.next

        current.next = linkedList(element)

    def prepend (self, element):
        "Prepends an element to the (left) end of the list"
        if (self.data == None):
            self.data = element # if list is empty prepend to head
            return

        currentHead = linkedList(self.data) # replicate values of current head
        currentHead.next = self.next

        self.data = element # replace head values with new values
        self.next = currentHead

    def deleteValue (self, value):
        "Deletes single element of a given value from the list"
        if (self.data == None):
            return # exit if linked list is empty

        if (self.data == value):
            if (self.next != None): # if there are more elements on the list
                self.data = self.next.data
                self.next = self.next.next
            else: # if we are deleting the last element on the linked list
                self.data = None
            return

        current = self

        while (current.next != None):
            if (current.next.data == value): # if found: cut node loose once the value is found
                current.next = current.next.next
                return
            current = current.next # otherwise: iterate next node

    def isEmpty(self):
        "Returns True if the linked list is empty"
        return (self.data == None)

    def size (self):
        "Returns size of the linked list"
        if (self.data != None):
            counter = 1

            current = self
            while (current.next != None):
                counter += 1
                current = current.next
            return counter
        else:
            return 0

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
l1 = linkedList()

l1.append('*')
l1.append('&')
l1.append('%')
l1.printList()

l1.deleteValue('*')
l1.deleteValue('&')
print(l1.isEmpty())
print (l1.size())
l1.printList()


l1.deleteValue('%')
print(l1.isEmpty())
print (l1.size())
l1.printList()

l2 = linkedList(1)
l2.printList()

l2.append(2)
l2.append(3)
l2.append(8)
l2.append(4)
l2.append(5)

l2.printList()

l2.append(6)
l2.append(7)

l2.printList()

l2.deleteValue(1)
l2.deleteValue(8)
l2.deleteValue(7)
l2.printList()

l2.prepend(1)
l2.prepend(0)
l2.printList()
print (l2.size())

l3 = linkedList()

l3.append("This")
l3.append("is")
l3.append("a")
l3.append("linked")
l3.append("list")

l3.printList()
print (l3.size())