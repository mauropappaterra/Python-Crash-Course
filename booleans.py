# Python Crash Course
# booleans.py
# Created by Mauro José Pappaterra on 24 February 2017.


############################################ CREATE A BOOLEAN

flag = True # assign a boolean value to a variable
selected = False

print (flag)
print (selected)

############################################ OPERATIONS RETURNING BOOLEAN VALUES

print (flag == True) # check for equality
print (selected != False) # check for inequality
print (not False) # negative Flase: returns True
print (not True) # negative True: returns False

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