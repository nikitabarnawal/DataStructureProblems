def findLongestConseqSubseq(arr, n):
    # code here
    count = 1
    maxCount = 1
    B = sorted(arr)
    B = list(map(int,B))
    for i in range(n-1):
        if B[i+1] == B[i]:
            continue
        
        if B[i+1] == B[i] + 1:
            count += 1
        
            if count > maxCount:
                maxCount = count
                
        else:
            count = 1
        
    return maxCount



n = int(input())
arr = input().split()
print(findLongestConseqSubseq(arr,n))
