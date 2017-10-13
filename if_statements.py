# Python Crash Course
# if_statements.py
# Created by Mauro José Pappaterra on 24 February 2017.


############################################ IF STATEMENTS
# Refer to booleans.py before reading this

#1
if (True): # iff whatever is in () happens to be true
    print("This will be executed.") # whatever line here will be executed

if True: # parenthesis are not necessary
    print("Yes.")

#2
if (True and True): # we can check multiple simultaneously statements using 'and'
    print("This too.")
#3
if (True and False):
    print("Not this.")
#4
if (True or False): # we can also check multiple simultaneously statements using 'or'
    print("This will do.")
#5
if ((True or False) and True): # we can also nest 'or' and 'and' statement as many times as we want
    print("This will do too.")

############################################ IF ELSE STATEMENTS

if (False): # iff what ever is in () is not True
    print ("This line will never be printed")
else:
    print("This will be executed instead") # whatever line here will be executed instead

############################################ IF ELIF ELSE CHAIN STATEMENTS

#1
if (False):
    print ("This line will never be printed")
elif (True):
    print ("This line will be executed instead")
else:
    print ("This line will never be printed")

#2
if (False):
    print ("This line will never be printed")
elif (False):
    print ("This line will never be printed")
else:
    print ("This line will be executed as a last alternative")

#3
if (False): # we can add as many elif statements as we wish, only ONE will be executed
    print ("This line will never be printed")
elif (False):
    print ("This line will never be printed")
elif (False):
    print("This line will never be printed")
elif (False):
    print ("This line will never be printed")
elif (True):
    print ("This line will be printed, among all alternatives")
else: # else statement could be ommited without any repercussions
    print ("This line will never be printed")
