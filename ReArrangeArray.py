#rearrange an array in maximum minimum order

def reArrange(A):
    c = []
    n = len(A)
    j = 0
    for i in range(len(A)):
        if i%2 == 0:
            c.append(A[n-j-1])
            j += 1
        else:
            c.append(A[j-1])
    return c

A = [1,2,3,4,5,6,7]
print(reArrange(A))
