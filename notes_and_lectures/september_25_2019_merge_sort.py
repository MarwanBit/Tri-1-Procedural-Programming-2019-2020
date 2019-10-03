#We have learned about insertion sort (trickle down sort), bubble sort, selection sort. We
#will learn about Merge sort today.

#Bozo sort runs on factorial time! 

#Bubble Sort, comparisons of a list of n length is n-1 + n-2 + n-3 + ...  

import random

def zipper(x,y):
    '''This function zips two sorted lists together'''
    px = 0
    py = 0
    out = []
    while px < len(x) and py < len(y):
        if x[px] < y[py]:
            out.append(x[px])
            px += 1
        else:
            out.append(y[py])
            py += 1
    out += x[px:]
    out += y[py:]
    return out 

#Number of sublists of merge sort with a length of n is log(base 2)(n)
def mergeSort(x):
    if len(x) <= 1:
        return x 
    first = x[:len(x)//2]
    second = x[len(x)//2:]
    return zipper(mergeSort(first),mergeSort(second))

x = [1,3,8,9,16,21,44,101] 
y = [2,3,9,16,16,44,101,112]
print(zipper(x,y))
random.shuffle(x)
print(x)
print(mergeSort(x))
x = [random.randint(1,100000) for j in range(123213)]
print(mergeSort(x))