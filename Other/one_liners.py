# Python Crash Course 
# one_liners.py
# Created by Mauro J. Pappaterra on 11 of March 2018.

############################################ LISTS
intList = [1,2,3,4,5,6,7,8,9,0]
addOne = [x + 1 for x in intList if True] # ONE-LINER: add +1 to every number in a list of integers
duplicate = [x * 2 for x in intList if True] # ONE-LINER: duplicate every number in a list of integers
evenList = [x for x in intList if (x % 2 == 0)] # ONE-LINER: create new list with even numbers only
oddList = [x for x in intList if (x % 2 != 0)] # ONE-LINER: create new list with odd numbers only

intList2 = [10,911,20,911,30,911,40,911,50,911,60,911,70,911,80,911,90,911,100,911]
removeAll = [x for x in intList2 if (x != 911)] # ONE-LINER: remove all instances of a given number

charList = [str(x) for x in intList if True] # ONE-LINER: convert a list of integers into characters

intList3 = ['1','2','3','4','5','6','7','8','9','0']
makeInt = [int(x) for x in intList3 if True] # ONE-LINER: convert a list of characters into integers

intString = "000000000000000"
stringToInt = [int(x) for x in intString if True] # ONE-LINER: convert a string of integers into a list of integers

intString2 = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"
stringToInt2 = [int(x) for x in intString2.split(' ') if True] # ONE-LINER: convert a string of integers into a list of integers

print(intList)
print(addOne)
print(duplicate)
print(evenList)
print(oddList)
print(charList)

print(intList2)
print(removeAll)

print(intList3)
print(makeInt)

print(intString)
print(stringToInt)

print(intString2)
print(stringToInt2)