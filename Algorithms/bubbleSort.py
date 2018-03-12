# Python Crash Course 
# bubbleSort.py
# Created by Mauro J. Pappaterra on 12 of March 2018.

def bubbleSort (array):
    flag = True # a flag to end the recursive call

    if (len(array) < 2): # list of 0 or 1 elements are already 'sorted'!
        return array

    for i, element in enumerate(array[0:-1]):
        j = i + 1
        # FOR TESTING PURPOSES
        #print(array)
        #print('i: ' + str(i) + ' j: ' + str(j) )
        #print('i: ' + str(array[i]))
        #print('j: ' + str(array[j]))
        if (array[i] > array[j]):
            flag = False # flag

            aux = array[j]
            array[j] = array[i]
            array[i] = aux

    if (not flag):
        #FOR TESTING PURPOSES
        #print("-> " + str(array))
        return bubbleSort(array) # recursive call

    return array

# ALL TESTS
# Example lists (arrays) to sort out:
integers = [100,23,45,5,98,200,75,339,-30,3000,12,-100,999]
floats = [10.0,0.313,2.3,3.45,33.45,0.0001,2.00,0.75,3.99,-3.0,3.0,1.2,-10.0,9.99,-2.0]
strings = ['charlie','alameda','zoo','hedgehog','apple','castle','warrior','dog','appliances','bar','foo']
booleans = [True,False,True,False,True,False]

print(integers)
bubbleSort(integers)
print(integers)
print('\n')

print(floats)
bubbleSort(floats)
print(floats)
print('\n')

print(strings)
bubbleSort(strings)
print(strings)
print('\n')

print(booleans)
bubbleSort(booleans)
print(booleans)
print('\n')
