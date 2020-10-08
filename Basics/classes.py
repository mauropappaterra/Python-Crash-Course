# Python Crash Course
# classes.py
# Created by Mauro José Pappaterra on 24 February 2017.


############################################ CLASSES

class myClass (): # A Python class is created

    def __init__(self, attribute_1, attribute_2): # this method runs automatically whenever we
        "Documentation on the class"              # create an instance of the class it is the
        self.attribute_1 = attribute_1            # constructor method
        self.attribute_2 = attribute_2
        self.attribute_3 = 1000 # creates a default value

    def method_1 (self): # functions within a class are called methods
        print("your function goes here " + self.attribute_1)

    def method_2 (self): # all class methods must be call with attribute self
        print ("another function " + str(self.attribute_2))

    def method_3(self):
        print(str(5 + 5))

    # etc etc.

first = myClass ('green', 404) # creating objects of the class myClass
second = myClass('red', 100)
third = myClass ('pink', 6000)

print(first.attribute_1) # calling an attribute
print(first.attribute_2)
print(first.attribute_3)

second.method_1() # calling a method
third.method_3()

first.attribute_1 = 'yellow'  # modifies an attribute from a class instance

############################################ INHERITANCE

class mySubClass (myClass): # Creating a subclass on Python

    #def __init__(self, attribute_1, attribute_2):        # This is how we define a sublass on Python
        #super()
        #self.__init__(self, attribute_1, attribute_2) # all methods and attributes from the parent class
                                                         # myClass will be inherited!

    def set_attribute_1(self, color): # Setters and Getters
        attribute_1 = color     # these new methods belong only to the subclass instances!

    def get_attribute_1(self):
        return self.attribute_1

    def set_attribute_2(self, number): # self is always passed as an attribute when calling a class method
         attribute_2 = number

    def get_attribute_2(self):
        return self.attribute_2

    def method_1(self):  # you can override a method on the subclass
                         # by creating a method with the same signature on the subclass
        print("This method overrides method_1 from the parent class")