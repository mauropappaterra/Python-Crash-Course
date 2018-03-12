# Python Crash Course 
# BST.py
# Created by Mauro J. Pappaterra on 11 of March 2018.

# A Python implementation of a Binary Search Tree (BST)

class BST():

    def __init__(self, data = None):
        "Constructor method"
        self.data = data
        self.left = None
        self.right = None

    def insert (self, value):
        "Insert value into the BST"
        if (self.data == None):
            self.data = value
        else:
            if (value <= self.data):
                if (self.left == None):
                    self.left = BST(value)
                else:
                    self.left.insert(value) # recursive call
            else:
                if (self.right == None):
                    self.right = BST(value)
                else:
                    self.right.insert(value) # recursive call


    def contains (self, value):
        "Returns True if the value is found on the BST"
        if (self.data == value):
            return True

        if (self.data < value):
            if (self.left != None):
                return self.left.contains(value) # recursive call
            else:
                return False
        else:
            if (self.right != None):
                return self.right.contains(value) # recursive call
            else:
                return False

    def printTree (self):
        if (self.left != None):
            self.left.printTree() # print left node (if any)

        print(self.data) # print self

        if (self.right != None):
            self.right.printTree() # print right node (if any)

# ALL TESTS

int_trees = BST() # tree 1: int no initial value
int_trees.insert(10)
int_trees.insert(5)
int_trees.insert(15)
int_trees.insert(8)
int_trees.insert(25)
int_trees.insert(10)
int_trees.insert(-10)
int_trees.insert(50)
int_trees.insert(-99)

int_trees.printTree()

print(int_trees.contains(3))
print(int_trees.contains(10))
print(int_trees.contains(25))
print(int_trees.contains(50))
print(int_trees.contains(100))

int_trees2 = BST(8) # tree 2: int with initial value
int_trees2.insert(-99)
int_trees2.insert(50)
int_trees2.insert(10)
int_trees2.insert(25)
int_trees2.insert(-10)
int_trees2.insert(5)
int_trees2.insert(10)
int_trees2.insert(15)

int_trees2.printTree()

int_trees3 = BST() # tree 3: chars no initial value
int_trees3.insert('z')
int_trees3.insert('v')
int_trees3.insert('a')
int_trees3.insert('h')
int_trees3.insert('r')
int_trees3.insert('c')
int_trees3.insert('p')
int_trees3.insert('f')
int_trees3.insert('g')

int_trees3.printTree()

int_trees4 = BST() # tree 4: strings no initial value
int_trees4.insert('world war two')
int_trees4.insert('hello')
int_trees4.insert('darkness')
int_trees4.insert('my')
int_trees4.insert('old')
int_trees4.insert('friend')
int_trees4.insert('america')
int_trees4.insert('lower bound')
int_trees4.insert('netherlands')
int_trees4.insert('pollution rates')
int_trees4.insert('double cheeseburger')
int_trees4.insert('ancient temple')

int_trees4.printTree()