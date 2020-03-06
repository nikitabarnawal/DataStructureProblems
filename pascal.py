#print pascals triangle
def solve(A):
    res = []
    final = []
    for i in range(1,A+1):
        C = 1
        for j in range(1, i+1):
            res.append(C)
            if(i==j):
                break
            else:
                C = int(C*(i-j)/j)
                
        if res != []:
            final.append(res)
        res = []           
        

    return final

print(solve(5))


