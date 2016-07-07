#-------------------------------Selection sort------------------------------------------------
#The selection sort improves on the bubble sort by making only one exchange for every pass through the list. 
#In order to do this, a selection sort looks for the largest value as it makes a pass and, after completing the pass, places it in the proper location. As with a bubble sort, 
#after the first pass, the largest item is in the correct place. After the second pass, the next largest is in place. 
#This process continues and requires n−1 passes to sort n items, since the final item must be in place after the (n−1)pass.

#-----------------------------------------------------------------------------------------------
#Selection Sort Code



def selectionSort(alist):
   for lot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,lot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[lot]
       alist[lot] = alist[positionOfMax]
       alist[positionOfMax] = temp

alist = [54,20,93,14,77,31,30,55,10]
selectionSort(alist)
print(alist)
