#Given an array of integers and a number K,
#the task is to reverse elements in every consecutive group of size K.

#Example
#Input Array=[1,2,3,4,5,6,7,8,9]
# k = 3
# Output = [3,2,1,6,5,4,9,8,7]

def reverseArray(arr,k):
    j = 0
    a = []
    b = 1
    while(j<k):
        a.append(arr[k-b])
        j = j+1
        b = b+1

        if j == k and k<len(arr):
            j = k
            k = k+3
            b = 1
    return a        
       


arr = [1,2,3,4,5,6,7,8,9]
k = 3
print(reverseArray(arr,k))
