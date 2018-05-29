# Python Crash Course 
# user_input.py
# Created by Mauro J. Pappaterra on 29 of January 2018.

MIN_LENGTH = 0
MAX_LENGTH = 9999

# Ask user for integer in between a determined range
# (POSITIVE VALUES ONLY)
print("Give a number between 0 and 9999")
number = input()
while (not (number.isdigit()) or not (MIN_LENGTH <= int(number) <= MAX_LENGTH)):
    print("ERROR MESSAGE")
    number = input()

# Ask user for integer in between a determined range
# (POSITIVE AND NEGATIVE VALUES)
MIN_LENGTH = -9999
print("Give a number between -9999 and 9999")
number = input()
while (not (number.lstrip("-").isdigit()) or not (MIN_LENGTH <= int(number) <= MAX_LENGTH)):
    print("ERROR MESSAGE")
    number = input()

# Ask user for integer in between a determined range (as method)
def ask_int (min, max):
    print("Give a number between"+ str(min) +" and " + str(max))
    number = input()

    while (not (number.lstrip("-").isdigit()) or not (min <= int(number) <= max)):
        print("ERROR MESSAGE")
        number = input()

    return number

# Let user choose among specific character, string or number
print("Choose '1','2','3','a','b' or 'this string'")
entry = input().lower()
while (entry != '1' and entry != '2' and entry != '3' and entry != 'a' and entry != 'b' and entry != 'this string'):
    print("ERROR MESSAGE")
    entry = input().lower()


# Ask user to enter path to external file
from pathlib import Path

print("Enter path to external file:")
path = input()
path = Path(path)

while (not path.is_file()):
    path = input("\nERROR: NOT A VALID FILE PATH! \nEnter path to external file: ")
    path = Path(path)

# Ask user to enter a multi-line text
def text_input():
    """Get user input right in the console, return as single string"""
    text = ""
    line = ""

    print ("Enter text, ina new line write <done> and press enter to finish")

    while (line != "<done>"):
        line = input()
        text += line + "\n"

    return text[:-8] # or use 7 to include line jump '\n'

# Use a loop to execute code over and over
again = True
while (again):
    # The code you wanna loop goes here
    again = input("\nWant to play again? y/n\n").lower()
    while (again != 'y' and again != 'n'):
        again = input("Not a valid option. Enter 'y' for yes or 'n' for no!").lower()
    again = (again == 'y')
print("\n-EXIT BY USER-")