# Python Crash Course
# for_loop.py
# Created by Mauro José Pappaterra on 25 February 2017.

############################################ FOR LOOPS

letters = ['a','b','c','e','f']

birthdays = {
    'Ann' : 1992,
    'Luke' : 1999,
    'Thomas' : 1985,
    'Mary' : 1976,
    'Bobby' : 1954,
    'Edward' : 1989,
    'Sarah' : 1985,
    'Sophie' : 2000,
    'Andrew' : 1992,
}

alphabet = {
    'a-f' : ['a','b','c','e','f'],
    'g-k' : ['g','h','u','j','k'],
    'l-p' : ['l','m','n','o','p'],
    'q-u' : ['q','r','s','t','u'],
    'v-z' : ['v','w','x','y','z']
}

#1
for letter in letters: # this for statement iterates a list
    print (letter) # your code goes here

#2
for key, value in birthdays.items(): # this for statement iterates a dictionary
    print(key + ' was born in ' + str(value)) # your code goes here

#3
for key, value in birthdays.items(): # this for statement implements an if statement
    if value >= 1980 or value <= 1989:
        print(key + ' was born in ' + str(value)) # your code goes here

#4
for key, value in alphabet.items(): # this for statements implements another for statement
    for letter in value:            # in order to iterate a list within a dictionary
        print(letter) # your code goes here

#5
for index, letter in enumerate (letters): # add an index to the for loop
    print ("On index # " + str(index) + " => " + letter)

#6
message = "You can iterate strings too!"
for character in message: # iterates every character on a string with a for loop
    print(character)