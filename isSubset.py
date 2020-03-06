#array subset of another
def isSubset(arr1,arr2,m,n):

    for i in range(n):
        for j in range(m):
            if(arr2[i] == arr1[j]):
                break
            else:
                if (j== m-1):
                    return 0
        

    return 1


if __name__ == "__main__":

    arr1 = [11,7,21,3,1]
    arr2 = [11,3,7,1]

    m = len(arr1)
    n = len(arr2)

    print(isSubset(arr1,arr2,m,n))
