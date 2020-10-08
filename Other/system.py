# Python Crash Course
# system.py
# Created by Mauro J. Pappaterra on 08 of October 2020.
import os

path_1 = "path/1/"
path_2 = "path/2/"

# List file in folder

allFiles = os.listdir(path_1) # Creates list with all files names an extensions

for file in allFiles:
    print(file)

# Check if file/folder exists
exists = os.path.exists(path_1 + "example_1.txt") # true if it exists

if (exists):
    os.remove(path_1 + "example_2.txt") # Delete file
    os.rename(path_1 + "example_3.txt", path_1 + "new name.txt") # Rename file
    os.rename(path_1 + "example_1.txt", path_2 + "example_1.txt") # Move file

