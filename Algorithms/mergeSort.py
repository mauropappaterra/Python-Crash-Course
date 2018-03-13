# Python Crash Course 
# mergeSort.py
# Created by Mauro J. Pappaterra on 12 of March 2018.

def mergeSort (array):
    leftStart = 0
    rightEnd = len(array) -1
    temp = [None] * len(array)
    recursiveSort(array, temp, leftStart, rightEnd)

def recursiveSort (array, temp, leftStart, rightEnd):
    if (leftStart >= rightEnd): # end recursion
        return

    middle = int((leftStart + rightEnd) / 2)

    recursiveSort(array, temp, leftStart, middle)
    recursiveSort(array, temp, middle + 1, rightEnd)
    merge(array, temp, leftStart, rightEnd)

def merge(array, temp, leftStart, rightEnd):
    leftEnd = int((rightEnd + leftStart) / 2)
    rightStart = leftEnd + 1

    left = leftStart
    right = rightStart
    index = leftStart

    while (left <= leftEnd and right <= rightEnd):

        if (array[left] <= array[right]): # copy the smaller element of each half of the array
            temp [index] = array[left] # copy left
            left += 1
        else:
            temp[index] = array[right] # or copy right
            right += 1
        index += 1

    # copy the remaining elements from the left and right side, only one will occur
    remaining = leftEnd - left + 1
    while (remaining > 0):
        temp[index] = array[left]
        index += 1
        left +=1
        remaining -=1

    remaining = rightEnd - right + 1
    while (remaining > 0):
        temp[index] = array[right]
        index += 1
        right += 1
        remaining -= 1

    # now copy everything back to the original array!
    size = rightEnd - leftStart + 1
    while (size > 0):
        array[leftStart] = temp [leftStart]
        leftStart += 1
        size -= 1

# ALL TESTS
# Example lists (arrays) to sort out:
integers = [100,23,45,5,98,200,75,339,-30,3000,12,-100,999,0,200,98]
floats = [10.0,0.313,2.3,3.45,33.45,0.0001,2.00,0.75,3.99,-3.0,3.0,1.2,-10.0,9.99,-2.0,0.0]
strings = ['potatoes','charlie','rode island','alameda','zoo','x','hedgehog','vermin','quest','apple','terrace','castle','warrior','dog','igloo','utah','appliances','yellow','ornament','bar','foo','zebra','gracious','san francisco','hernia','mountains','jamaica','llamas','nicaragua','kilo']
booleans = [True,False,True,False,True,False,True,False,True,False,True,False]

print(integers)
mergeSort(integers)
print(integers)
print('\n')

print(floats)
mergeSort(floats)
print(floats)
print('\n')

print(strings)
mergeSort(strings)
print(strings)
print('\n')

print(booleans)
mergeSort(booleans)
print(booleans)
print('\n')