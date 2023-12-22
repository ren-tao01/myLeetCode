import random

def quickSort(input_array, start , stop):
    
    if(start < stop):
        p = partition(input_array, start, stop)
        quickSort(input_array, start, p-1)
        quickSort(input_array, p+1, stop)

    
    
def partition(array, left, right):
    r = random.randint(left, right)
    array[r], array[left] = array[left], array[r]

    pivot = left # pivot
     
    # a variable to memorize where the 
    i = left + 1
     
    # partition in the array lefts from.
    for j in range(left + 1, right + 1):
         
        # if the current element is smaller
        # or equal to pivot, shift it to the
        # left side of the partition.
        if array[j] <= array[pivot]:
            array[i] , array[j] = array[j] , array[i]
            i = i + 1
    array[pivot] , array[i - 1] =\
            array[i - 1] , array[pivot]
    pivot = i - 1
    return (pivot)

    # track swapping point
    # sp = right - 1

    # while(left<sp):

    #     if array[left] > array[right]:
    #         while(array[sp]>array[right]):
    #             sp-=1
    #         array[left], array[sp] = array[sp], array[left]
    #         sp -= 1

    #     left +=1
    
    # array[sp+1], array[right] = array[right], array[sp+1]

    # return sp+1
    
    
arr = [1,2,19,43,8,9,20] 
quickSort(arr,0,len(arr)-1) 


for i in range(len(arr)): 
    print(arr[i])