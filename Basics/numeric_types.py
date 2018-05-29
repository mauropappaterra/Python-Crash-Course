# Python Crash Course
# numeric_types.py
# Created by Mauro José Pappaterra on 24 February 2017.

############################################ INTEGERS

uno = 1
dos = 2
tres = 3
cuatro = 2 + dos # sum
cinco = 10 / 2 # division
seis = tres * 2 # multiplication
siete = 10 - tres # rest
ocho = 8
nueve = 3 ** 2 # exponent
diez = 45 % 35 # returns reminder

diez += 1 # sums + x
diez -= 1 # rests - x

print (str(0)) # cast a number into a String to use print
print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)
print(seis)
print(siete)
print(ocho)
print(nueve)
print (diez)

############################################ FLOATS

integer = 20
float = 13/2

print (float)
print (integer)
print (integer + float)
print (float + integer)
print (integer + integer)
print (float + float)

print (round(0.123456789,0)) # round up round(number,digits)
print (round(0.123456789,1))
print (round(0.123456789,2))
print (round(0.123456789,3))
print (round(0.123456789,4))
print (round(0.123456789,5))
print (round(0.123456789,6))
print (round(0.123456789,7))
print (round(0.123456789,8))
print (round(0.123456789,9))



########################################### BINARY NUMBERS

binary = 0b11111111 # 0b for binary
binary_2 = bin(255) # converts integer in binary

print(binary) # will print as integer by default
print(bin(binary))

print(binary_2)

print(binary / 2) # operation between binary and integer (binary is retrieved as integer)
print(binary - 100) # result retrieved as integer

print(binary_2 + bin (10))

########################################### HEXADECIMAL NUMBERS

hexadecimal = 0xFF # 0x for hexadecimal
hexadecimal_2 = hex(255) # converts integer in hexadecimal

print(hexadecimal) # will print as integer by default
print(hex(hexadecimal))

print(hexadecimal_2) # this are printed as defined

########################################### OTHER
from random import *

print(random())
print(randint(1, 100)) # print a random integer number between and including 1 and 100
print(uniform(0.0,1.0)) # print a random float number between and including 0.0 and 1.0

# Ask user for input and check for integer in between a determined range
# (POSITIVE VALUES ONLY)
number = input("Give a number between 1 and 9999")
while (not (number.isdigit()) or not(1 <= int(number) <= 9999)):
    number = input("Not a valid input. Give a number between 1 and 9999.")
print(number)

# Ask user for input and check if the input is an integer in between a determined range
# (WITH NEGATIVE VALUES)
number = input("Give a number between -9999 and 9999")
while (not (number.lstrip("-").isdigit()) or not(-9999 <= int(number) <= 9999)):
    number = input("Not a valid input. Give a number between 1 and 9999.")
print(number)