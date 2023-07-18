#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        prod = 1
        count = 0
        i =0
        for num in nums :
            if num != 0:
                prod = prod * num
            else :
                index = i
                count +=1
            i +=1
                
        if count >1:
            sol = [0 for x in range(n)]
            return(sol)
        elif count == 1:
            sol = [0 for x in range(n)]
            sol[index] = prod
        else :
            sol = []
            for num in nums :
                sol.append(int(prod/num))
        
        return(sol)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())

    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]

        ans=Solution().productExceptSelf(arr,n)
        print(*ans)
# } Driver Code Ends