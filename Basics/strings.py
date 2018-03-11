# Python Crash Course
# strings.py
# Created by Mauro José Pappaterra on 24 February 2017.

############################################ CREATE A STRING
print ("Hello World!")   # yea

string_1 = "This 'is' a String"
string_2 = 'This is "also" a String' # How to assign string to variable

string_3 = '''                This is a 
                multiple line string
                 on Python'''

print(string_1)
print(string_2)
print(string_3)

first_name = "Mauro"
middle_name = "Jose"
last_name = "Pappaterra"

print ("\nThis is a line jump\n\tThis is a tab\n")

############################################ CONCATENATE A STRING
my_name = 'My name is' + ' ' + first_name + " " + middle_name + " " + last_name # + concatenates
my_name+= ' and I was born in Argentina' # += concatenates

print(my_name)

print('I' * 5) # repetition operator * concatenates string x times

############################################ ITERATE A STRING

message = "It's wonderful to be here, it's certainly a dream"

print(message [0]) # 'I'
print(message [1]) # 't'
print(message [2]) # '''
print(message [3]) # 's'
print(message [4]) # ' '
#...
#print(message [34]) # Error out of bounds

print(message [-1]) # 'm'
print(message [-2]) # 'a'

# message[5] = 'X' # Error, strings are immutable

print ("wonderful" in message) # returns True if the word is found on the string
print ("Wonderful" in message) # it is case sensitive (does not need to be a whole word)

for character in message: # iterates every character on a string with a for loop
    print(character)

############################################ SLICE A STRING

sliceMe = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(sliceMe[1:4]) # slices string from index x up to and NOT including index y
print(sliceMe[:3]) # slices string from index 0 up to and NOT including index y
print(sliceMe[2:]) # slices string from index x  up to the last element on the tuple
print(sliceMe[:]) # returns string as it is, this is not very useful
print(sliceMe[-6:]) # slices string from index -2 up to the last element on the tuple
print(sliceMe[:-6]) # slices string from index 0 up to and NOT including index x

############################################ OTHER STUFF

print(my_name.lower()) # .lower() turns string to lowercase
print(my_name.islower()) # returns true if all characters are lowercase letters

print(my_name.upper()) # .upper() turns string to uppercase
print(my_name.isupper()) # returns true if all characters are uppercase letters


num_variable= 1000
float_variable = 2.0

string_3 =  "number five hundred = " + str(num_variable / float_variable) # cast number into string

print(string_3.title()) #.title() turns first char of each word to uppercase

string_4 = "This is not a String"

print(string_4.isalpha()) # true if alphanumeric string
print(string_4.isdigit()) # true if digit string
print(string_4.isspace()) # true if its an empty space

print(string_4.startswith('This')) # true if string starts with 'a'
print(string_4.endswith('String')) # true if string starts with 'b'
print(string_4.replace ('not', 'obviously')) # replaces all ocurrences of 'a' with 'b'

print(string_4.split('s')) # Splits the string with a chosen char creating a list of new substrings
print(string_4.split(' ')) # Splits the string with a space char creating a list of words
print (list(string_4)) # Splits the string into a list of chars

newList = ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'n', 'o', 'w', ' ', 'a', ' ', 'S', 't', 'r', 'i', 'n', 'g']
print ("".join(newList)) # Joins a list of chars into a string

newList = ['This','is','now','a','string']
print (" ".join(newList)) # This time each element is concatenated with a space character, it could be anything

print ("redrum"[::-1]) # reverse string