#give diagonals
def diagonals(A):
    final = []

    for j in range(len(A)):
       i = 0
       res = []
       
       while (j>=0):
           res.append(A[i][j])
           i = i +1
           j = j -1

       final.append(res)

    

    for i in range(1,len(A)):   
        j = len(A) - 1
        res = []
        while(i < len(A)):
            res.append(A[i][j])
            i = i + 1
            j = j - 1
        final.append(res)

    return final
         
    


A=[[1,2,3],[4,5,6],[7,8,9]]
print(diagonals(A))
