# Python Crash Course
# lists.py
# Created by Mauro José Pappaterra on 24 February 2017.

#Python Lists are just like Java arrays... but...

############################################ CREATE A LIST
my_list = ['a','b','c','e','f'] # can be a homogeneous list
my_list2 = ['a',2,True,5.6,"Hello World"] # or a heterogeneous list

size = 1000
empty_list = [None] * size # creates an empty list of size 1000

print(my_list)
print(my_list2)
print(empty_list)

############################################ RETURN ELEMENTS BY INDEX
print(my_list[0]) # returns first element
print(my_list[1]) # returns second element ...

# print(my_list[9]) # index out of range error

print(my_list[-1]) # returns last element
print(my_list[-2]) # returns second last element ...

#print(my_list[-9]) # index out of range error

############################################ ADD ELEMENTS
my_list.append('g') # add element to end of the list
my_list.insert(3,'d') # add element to index i, shift all following elements +1 to the right

new_elements = ['h','i','j','k']
my_list = my_list + new_elements + ['l','m','n','o']  # + concatenate two or more lists together

print(my_list)

############################################ MODIFY ELEMENTS
my_list[1] = '1' # replaces previous element with new element
print(my_list)

my_list[1] = 'b'
print(my_list)

############################################ REMOVE ELEMENTS

del my_list[6] # delete element on index x
del my_list[-1] # deletes last element on the list

my_list.remove('d') # deletes element by value, only one instance

list_with_ones = [1,2,1,1,1,1,1,1,1,1,3,4,5,6,7,8,1,1,1,1,99]
list_with_ones = [x for x in list_with_ones if x != 1] # delete all existing instances
print(list_with_ones)

create_set = set([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) # casting the list as a set eliminates repeats, leaving only [1,2]
print(create_set)

print("the last element of the list is the letter " + my_list.pop()) # returns last element, and then deletes it
print("the first element of the list is the letter " + my_list.pop(0)) # return element on index x, and then deletes it
print(my_list)

############################################ OTHER STUFF
my_list_2 = [100000,1222,566,2223,-23,3456,1,34,56,999,8888]
print(my_list_2)

print(sorted(my_list_2)) # temporarily sorts the list alphabetically without applying changes
print (my_list_2)

my_list_2.sort() # sorts list alphabetically modifying the list
print(my_list_2)

my_list_2.reverse() # reverses the list modifying the list
print(my_list_2)

print(len(my_list_2)) # returns the length of the list

newList = ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'n', 'o', 'w', ' ', 'a', ' ', 'S', 't', 'r', 'i', 'n', 'g']
print ("".join(newList)) # Joins a list of chars into a string

intList = [1,2,3,4,5,6,7,8,9,0]
charList = [str(x) for x in intList if True] # ONE-LINER: convert a list of integers into characters
print(intList)
print(charList)

############################################ ITERATE A LIST
numbers = range (100001,100100) # creates a list containing a range of numbers

for number in numbers: # iterates on each element on the list
    print (number)

for index, number in enumerate(numbers): # iterates on each element on the list with index
    print(str(index) + str(number))

############################################ SLICE A LIST
my_list_3 = ['John L.','Paul','Ringo','John H.']

print(my_list_3[1:4]) # slices list from index x up to and NOT including index y
print(my_list_3[:3]) # slices list from index 0 up to and NOT including index x
print(my_list_3[2:]) # slices list from index x  up to the last element on the list
print(my_list_3[:]) # returns list as it is, it is used for copying a list
print(my_list_3[-2:]) # slices list from index -2 up to the last element on the list
print(my_list_3[:-2]) # slices list from index 0 up to and NOT including index x

############################################ COPY A LIST
my_list_4 = my_list_3 # this does NOT work on Python, modifying either list would also modify the other

my_list_4.append('Mick')
print(my_list_3)

my_list_5 = my_list_3[:] # this will create a new independent list

my_list_5.append('Keith')
print(my_list_3)

############################################ CREATE A MATRIX
matrix = [[1.0,0.0,0.0], [0.3,0.2,0.5], [0.0,0.5,0.5]] # a matrix is a lsit of lists

print (matrix) # iterate a matrix, return complete matrix, raw and element respectively
print (matrix[1])
print (matrix[1][2])

new_matrix = [row[:] for row in matrix] # clone a matrix