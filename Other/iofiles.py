# Python Crash Course 
# iofiles.py
# Created by Mauro J. Pappaterra on 29 of September 2017.

############################################ DEFINE FILE PATH
from pathlib import Path # import Path module from library

path = "path\your_file.txt"
mode = "r" # read mode
mode = "w" # write mode
mode = "a" # append mode (writes on existing file)
mode = "b" # binary mode


############################################ OPEN FILE ON READ MODE

mode = "r"
myFile = open (path, mode)

myFile.read() # reads the entire file, returns contents as a string
myFile.readlines() # reads the entire file and returns it as a list, each line a new element
myFile.readline() # reads the next line on the file, returns as a string

myFile.close() # close file

#as a single loop
with open (path, mode) as newFile:
    samples = (newFile.readline())
    print(samples)

############################################ OPEN FILE ON WRITE/APPEND MODE

path = "path/example_1.txt"
mode = "w"

with open (path, mode) as file:
    file.write ("Create a new file and write this line on it (Overwrite if the file already exists).")

mode = "a" # change to append mode
#path = "path/example_2.txt"
with open (path, mode) as file:
    file.write ("\nAppend this line to the previously existent file (Create if the file does not exist)")

example_3 = open ("path/example_3.txt", "w") # path, mode
example_3.write ("Create a new file and write this line on it (Overwrite if the file already exists).")

example_3 = open ("path/example_3.txt", "a") # changed to append mode
example_3.write ("\nAppend this line to the previously existent file (Create if the file does not exist)")

import codecs # to open text files in different encoding import this

with codecs.open(path, mode, encoding='utf8') as myFile:
    full_text = myFile.readlines()  # saves each line of the text into a list
    print(full_text)