#User function Template for python3


class Solution:
    def minDiff(self,arr,N,k):
        arr.sort()
        diff = float("inf")
        for i in range (0,n-k+1):
            temp = arr[i+k-1]-arr[i]
            diff = min(temp,diff)

        return(diff)
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


#Initial Template for Python 3

t=int(input())
for _ in range(0,t):
    #n=int(input())
    x=list(map(int,input().split()))
    n=x[0]
    k=x[1]
    a = list(map(int,input().split()))
    ans=Solution().minDiff(a,n,k)
    print(ans)

# } Driver Code Ends