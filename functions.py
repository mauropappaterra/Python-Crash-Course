# Python Crash Course
# functions.py
# Created by Mauro José Pappaterra on 24 February 2017.


############################################ CREATE AND CALL FUNCTIONS

def myFunction(): # defines a function
    "Documentation on the function"
    print ('your functions goes here')

myFunction() # calls a function

def myFunction_2( parameter_1, parameter_2, parameter_3 ): # define a function with parameters
    "Example Function 2"
    print_me = parameter_3 + 100
    print ('you have entered ' + parameter_1 + ' and ' + parameter_2
           + '\n also your number + 100 = ' + str(print_me))

myFunction_2('house', 'dog', 100) # call function without specifying parameters (order of parameters matters)

myFunction_2(parameter_1 = 'car',parameter_3 = 400, parameter_2 = 'window') # call function specifying parameters
                                                                            # with a keyword (order does not matter))

def print_card (value, suit ='spades'): # define function with default parameter
    "Prints card parameters needed value an suit, default suit_ spades"
    print('you have played a ' + value + ' of ' + suit)

print_card('ace')
print_card('four', 'diamonds')
# myFunction_3() # missing parameters error

first_name = 'john'
middle_name = 'fritzgerald'
last_name = 'kennedy'

def say_my_name (first, middle =''): # define a function with an optional parameter
    print ('My name is ' +first + ' ' + middle)

say_my_name(first_name)
say_my_name(first_name, middle_name)

def return_name_caps (first, last, middle =''): # define a function with a return value
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()

print ('My name is ' + return_name_caps(first = first_name, middle= middle_name, last= last_name))

def return_dictionary (first, last, middle =''): # this function returns a dictionary
    dictionary = {'first name': first, 'middle name': middle, 'last name': last}
    return dictionary

my_friends = ['Hannibal','Athila','Heron','Julius']

def say_hello (names): # this function takes a list as a parameter and implements a for loop
    for name in names:
        message = 'Hello ' + name + '!'
        print (message)

say_hello(my_friends)

def list_friends (*friends): # this function takes any arbitrary number of parameters
    print (friends)          # the * indicates that a tuple call 'friends' containing all
                             # parameters shall be created

list_friends('Mitch','Mickey','Manny','Moe','Jerry','Bobby','Jesse')

def create_profile (first_name,last_name,**info):# this function takes any arbitrary number of parameters too
    profile = {'first name': first_name, 'last name': last_name} # the ** indicates that a dictionary called 'info'
                                                                 # containing all key=>value parameters is to be
    for key,value in info.items():                               # created.
        profile[key] = value

    return profile

johnson = create_profile('andrew', 'johnson', born= 1808, where = 'NC', president = '1865-1869', diseased= True)
jefferson = create_profile('thomas', 'jefferson', born=1743 , diseased= True)
washington = create_profile('george', 'washington', born= 1732, where = 'VI', president = '1789-1797')
obama = create_profile('barack', 'obama', president = '2009-2017', where = 'HI', diseased= False)

print (johnson)
print (jefferson)
print (washington)
print (obama)

############################################ EXPORT FUNCTIONS

# Functions in Python can be exported
# import ALL functions from a module by adding 'import module_name' to the file header
# call function like this: module_name.function_name()
# you can import only ONE function by adding 'from module_name import function_name' to the file header
# call the function later like this: function_name()
# you can rename the function by adding an alias e.g.: from module_name import function_name as alias
# you can call the function like this: alias()
# you can import all function in a module by adding 'from module_name import *'