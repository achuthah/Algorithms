# Binary Search
Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].
A simple approach is to do linear search, i.e., start from the leftmost element of arr[] and one by one compare x 
with each element of arr[], if x matches with an element, return the index. If x doesn’t match with any of elements, return -1.

Uses:
1) Binary search can be used to access ordered data quickly when memory space is tight. 
2) Doing fast substring lookup using suffix arrays, which contain all the suffixes of the set of searchable 
   strings in lexiographic ordering (I wanted to conserve memory and keep the implementation simple)
3)

Limitations:

1)Because it is very slow to update an ordered array (doing insertions or deletions), 
binary search is not useful when the array changes often.
