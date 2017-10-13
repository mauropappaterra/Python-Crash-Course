# Python Crash Course 
# iofiles.py
# Created by Mauro J. Pappaterra on 29 of September 2017.

############################################ IF ELIF ELSE CHAIN STATEMENTS

path = "C:\path\your_file.txt"
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
    samples = (newFile.readlines())
    print(samples)

############################################ OPEN FILE ON WRITE MODE

mode = "w"
