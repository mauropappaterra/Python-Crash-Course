# Python Crash Course 
# quickSort.py
# Created by Mauro J. Pappaterra on 12 of March 2018.

def quickSort (array):
    left = 0
    right = len(array) - 1
    recursiveSort(array, left, right)

def recursiveSort (array, left, right):
    # FOR TESTING PURPOSES
    # print(array)
    if (left >= right):
        return

    pivot = int((left + right) /2)
    index = swap (array, left, right, array[pivot]) # swap elements & find partition

    recursiveSort(array, left, index - 1) # call recursively on each half
    recursiveSort(array, index, right)

def swap (array, left, right, pivot):
    while (left <= right):

        while (array[left] < pivot):
            left += 1

        while (array[right] > pivot):
            right -= 1

        if (left <= right):
            # FOR TESTING PURPOSES
            # print(array[right])
            # print(array[left])
            aux = array[right]
            array[right] = array[left]
            array[left] = aux

            left += 1
            right -= 1

    return left # return partition

# ALL TESTS
# Example lists (arrays) to sort out:
integers = [100,23,45,5,98,200,75,339,-30,3000,12,-100,999,0,200,98]
floats = [10.0,0.313,2.3,3.45,33.45,0.0001,2.00,0.75,3.99,-3.0,3.0,1.2,-10.0,9.99,-2.0,0.0]
strings = ['potatoes','charlie','rode island','alameda','zoo','x','hedgehog','vermin','quest','apple','terrace','castle','warrior','dog','igloo','utah','appliances','yellow','ornament','bar','foo','zebra','gracious','san francisco','hernia','mountains','jamaica','llamas','nicaragua','kilo']
booleans = [True,False,True,False,True,False,True,False,True,False,True,False]

print(integers)
quickSort(integers)
print(integers)
print('\n')

print(floats)
quickSort(floats)
print(floats)
print('\n')

print(strings)
quickSort(strings)
print(strings)
print('\n')

print(booleans)
quickSort(booleans)
print(booleans)
print('\n')