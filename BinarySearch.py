# Algorithms
#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

number = 6  # number to search for
size = 10  # size of random array
array = random.sample(list(range(1, 20)), size)  # get some random numbers
array = sorted(array)  # sorted() returns a new list
print (number, array)  # show us what you've got


#    Search for number in array

def binary_search(
    number,
    array,
    lowest,
    highest,
    ):

    if highest < lowest:  # idhuku mela number ila
        return -1
    median = (lowest + highest) // 2  # nadupagudhi in array
    if number == array[median]:
        return median  # number found here
    elif number < array[median]:
        return binary_search(number, array, lowest, median - 1)  # try with residue
    else:
        return binary_search(number, array, median + 1, highest)  # try above here


def my_search(number, array):  # interface to binary_search()
    return binary_search(number, array, 0, len(array) - 1)


pos = my_search(number, array)
if pos < 0:
    print 'kedaiklyaaaee'
else:
    print ('maatnaan da ingae', pos)
