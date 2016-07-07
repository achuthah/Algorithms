#-------------------------------Bubble sort------------------------------------------------
#The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of order.
#Each pass through the list places the next largest value in its proper place. 
#In essence, each item “bubbles” up to the location where it belongs.
#-----------------------------------------------------------------------------------------------
#Bubble Sort Code

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]: #Swapping / Exchange happens here
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)