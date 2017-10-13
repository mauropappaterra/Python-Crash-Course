# Python Crash Course
# while_loop.py
# Created by Mauro José Pappaterra on 25 February 2017.


############################################ WHILE LOOPS
number = 10

#1
while (number <= 25): # while this is true
    print (number) # this will continue to execute
    number += 1 # we need an exit statement otherwise we get an infinite loop

while number <= 30: # () are not mandatory
    print (number)
    number += 1

#2
while (1 > 100): # if this is false
    print("This line will never be executed") # this will never be executed

#3
while (number < 1000000000000000000000000): # this while statements implements an if statement
    print (number)
    number += 1
    if (number == 100):
        print(number)
        break # break exits the while loop

#4
number = 0

while (number <= 10):
    number += 1
    if number % 2 == 0:
        continue # continue interrupts the loop, restarting from the top without exiting the loop
    print(number) # this line will not be executed when 'number' is even

#5
while (True): # This is an infinite loop
    print('infinity')