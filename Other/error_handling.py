# Python Crash Course 
# error_handling.py
# Created by Mauro J. Pappaterra on 10 of October 2017.

############################################ ERROR HANDLING
my_array = [1,2,3]

try:
  print(my_array[99])
except:
  print("ERROR!")