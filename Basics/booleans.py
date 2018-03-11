# Python Crash Course
# booleans.py
# Created by Mauro José Pappaterra on 24 February 2017.

############################################ CREATE A BOOLEAN VARIABLE
flag = True # assign a boolean value directly to a variable
selected = False

x = 4
even = (x % 2 == 0) # or indirectly, using boolean operations
odd = (x % 2 != 0)
smaller = (x < 100)
larger = (x > 0)
is_not = (x != 4)
equals = (x == 256)
#... etc

print(flag)
print(selected)
print(even)
print(odd)
print(smaller)
print(larger)
print(is_not)
print(equals)

############################################ OPERATIONS RETURNING BOOLEAN VALUES

print (flag == True) # check for equality
print (selected != False) # check for inequality
print (not False) # negative Flase: returns True
print (not True) # negative True: returns False

print ((True and False)) # follows tables of truth logic for all possible cases

my_age = 27
                     # NUMERICAL COMPARISONS
print (my_age == 27) # x equals y
print (my_age > 30)  # x larger than y
print (my_age < 30)  # x smaller than y
print (my_age >= 29) # x larger or equal to y
print (my_age <= 27) # x smaller or equal to y

                                          # CONDITIONAL COMPARISONS
print ((1 + 1 == 2) and (10/2 + 5 != 10)) # and
print ((1 + 1 == 2) or (10/2 + 5 != 10))  # or
print (((1 + 1 == 2) and (10/2 + 5 != 10)) or (10%5 == 1)) # nested and, or

                      # LOGICAL OPERATORS (short-circuit)
print (True or False) # OR
print (False | True)

print (True and False) # AND
print (False & True)
