# Python Crash Course
# tuples.py
# Created by Mauro José Pappaterra on 24 February 2017.


############################################ CREATE A TUPLE
my_band = ('John L.', 'Paul', 'Ringo', 'John H.') # Works just like a list
print(my_band)

############################################ RETURN ELEMENTS
print(my_band[0]) # returns first element
print(my_band[1]) # returns second element ...

# print(my_band[9]) # index out of range error

print(my_band[-1]) # returns last element
print(my_band[-2]) # returns second last element ...

#print(my_band[-9]) # index out of range error

############################################ ADD ELEMENTS
# Tuples cannot be modified

############################################ MODIFY ELEMENTS
# Tuples cannot be modified

############################################ REMOVE ELEMENTS
# Tuples cannot be modified

############################################ OTHER STUFF
print(sorted(my_band)) # temporarily sorts the tuple alphabetically without applying changes

print (my_band)

print(len(my_band)) # returns the length of the tuple

############################################ ITERATE A TUPLE
for member in my_band: # iterates on each element on the tuple
    print (member)

############################################ SLICE A TUPLE
print(my_band[1:4]) # slices tuple from index x up to and NOT including index y
print(my_band[:3]) # slices tuple from index 0 up to and NOT including index y
print(my_band[2:]) # slices tuple from index x  up to the last element on the tuple
print(my_band[:]) # returns tuple as it is, it is used for copying a tuple
print(my_band[-2:]) # slices tuple from index -2 up to the last element on the tuple
print(my_band[:-2]) # slices tuple from index 0 up to and NOT including index y