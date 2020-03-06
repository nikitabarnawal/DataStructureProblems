class Solution(object):

    def SquareSortedArr(self,A):

        return sorted(x*x for x in A)
        

A = [-4,-1,0,3,10]
obj = Solution()
print(obj.SquareSortedArr(A))
            
