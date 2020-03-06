'''
merge two sorted list and give the output
'''

def mergeSortedlist(A,B):
    i = 0
    j = 0
    res = []

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            res.append(A[i])
            i = i + 1
        else:
            res.append(B[j])
            j = j + 1

    return res

A = [1,5,6,9,11]
B = [3,4,7,8,10]

print(mergeSortedlist(A,B))
