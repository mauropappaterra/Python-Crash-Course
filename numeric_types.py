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

print (randint(1, 100)) # print a random number between and including 1 and 100


# Check if an input is an integer in between a determined range
number = input("Give a number between 1 and 9999")
while (not (number.isdigit()) or not(1 <= int(number) <= 9999)):
    number = input("Not a valid input. Give a number between 1 and 9999.")
print(number)